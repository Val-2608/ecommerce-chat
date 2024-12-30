import os
import uuid
import logging
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import Product, Session, ChatLog, User
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(
    filename='chatbot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration for SQLite Database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'instance', 'ecommerce.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migrations
db.init_app(app)
migrate = Migrate(app, db)

# --- Routes ---
@app.route('/')
def home():
    return jsonify({"message": "API is running!"})

# --- Authentication Routes ---
@app.route('/api/register', methods=['POST'])
def register():
    """
    Handle user registration.
    Request JSON:
        {
            "email": "user@example.com",
            "password": "password123"
        }
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User  already exists"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User  registered successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    """
    Handle user login.
    Request JSON:
        {
            "email": "user@example.com",
            "password": "password123"
        }
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Create a new session for the user
    session_id = str(uuid.uuid4())
    new_session = Session(session_id=session_id, user_id=str(user.id))
    db.session.add(new_session)

    try:
        db.session.commit()
        logging.info(f"Session created: {session_id} for user: {user.id}")
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating session: {str(e)}")
        return jsonify({"error": "Failed to create session"}), 500

    return jsonify({"session_id": session_id, "message": "Login successful"}), 200

# --- Product Routes ---
@app.route('/products', methods=['GET'])
def get_products():
    """
    Fetch all products or filter products by category.
    Query Params:
        - category (optional): Filter products by category.
    """
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "price": p.price, "description": p.description, "category": p.category} for p in products]
    return jsonify(product_list)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch a specific product by its ID.
    """
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "category": product.category
    })

   
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        session_id = data.get('session_id')
        message = data.get('message')
        
        if not session_id or not message:
            return jsonify({"status": "error", "message": "Invalid session or message"}), 400

        # Log the user message
        new_chat_log = ChatLog(
            session_id=session_id,
            message=message,
            sender='user'
        )
        db.session.add(new_chat_log)
        db.session.commit()

        # Process the message
        message_lower = message.lower()
        bot_response = ""

        # Simple product search
        if 'product' in message_lower or 'search' in message_lower:
            # Get all products (limit to 5)
            products = Product.query.limit(5).all()
            if products:
                bot_response = "Here are some products:\n"
                for product in products:
                    bot_response += f"- {product.name}: ${product.price:.2f} ({product.category})\n"
            else:
                bot_response = "No products found in the database."

        # Category listing
        elif 'categories' in message_lower:
            categories = db.session.query(Product.category).distinct().all()
            if categories:
                bot_response = "Available categories:\n"
                bot_response += "\n".join([f"- {cat[0]}" for cat in categories])
            else:
                bot_response = "No categories found."

        # Price query
        elif 'price' in message_lower:
            price_stats = db.session.query(
                db.func.min(Product.price),
                db.func.max(Product.price)
            ).first()
            bot_response = f"Our products range from ${price_stats[0]:.2f} to ${price_stats[1]:.2f}"

        # Default response
        else:
            bot_response = (
                "I can help you with:\n"
                "1. Search products\n"
                "2. Show categories\n"
                "3. Check price ranges\n"
                "What would you like to know?"
            )

        # Log the bot response
        bot_chat_log = ChatLog(
            session_id=session_id,
            message=bot_response,
            sender='bot'
        )
        db.session.add(bot_chat_log)
        db.session.commit()

        return jsonify({
            "status": "success",
            "bot_response": bot_response
        })

    except Exception as e:
        app.logger.error(f"Error in chat route: {str(e)}")
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)