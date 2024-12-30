from models import Product
import logging


# Set up logging with a detailed format
logging.basicConfig(
    filename='chatbot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_user_interaction(message, response):
    """Log user interaction for analysis."""
    logging.info(f"User: {message} | Bot: {response}")

def extract_query(message):
    """Extract the search query from the user's message."""
    return message.replace("search", "").strip()

def fetch_products(query):
    """Fetch products based on the search query."""
    return Product.query.filter(Product.name.ilike(f"%{query}%")).all()

def fetch_product_details(product_id):
    """Fetch details of a specific product by its ID."""
    return Product.query.get(product_id)

def format_product_list(products):
    """Format the list of products for display."""
    return "\n".join([f"{p.name} - ${p.price}" for p in products])

def format_product_details(product):
    """Format the details of a single product for display."""
    return (
        f"Product Details:\n"
        f"Name: {product.name}\n"
        f"Price: ${product.price}\n"
        f"Description: {product.description}\n"
        f"Category: {product.category}"
    )

def validate_product_id(message):
    """Validate the product ID provided by the user."""
    product_id = ''.join(filter(str.isdigit, message))
    return product_id if product_id else None

def help_message():
    """Return the help message."""
    return (
        "You can ask me:\n"
        "- 'Search for [product name]': Find products by name.\n"
        "- 'Details of [product ID]': Get details of a specific product.\n"
        "- 'Help': See this help message."
    )

def process_user_message(message):
    """Process the user's message and generate a bot response."""
    message = message.lower()

    if "search" in message:
        query = extract_query(message)
        products = fetch_products(query)
        if products:
            response = "Here are the products I found:\n"
            response += format_product_list(products)
            log_user_interaction(message, response)
            return response
        response = f"Sorry, I couldn't find any products related to '{query}'."
        log_user_interaction(message, response)
        return response

    elif "details" in message:
        product_id = validate_product_id(message)
        if product_id:
            product = fetch_product_details(product_id)
            if product:
                response = format_product_details(product)
                log_user_interaction(message, response)
                return response
            response = f"Sorry, I couldn't find a product with ID {product_id}."
            log_user_interaction(message, response)
            return response
        response = "Please provide a valid product ID."
        log_user_interaction(message, response)
        return response

    elif "help" in message:
        response = help_message()
        log_user_interaction(message, response)
        return response

    else:
        response = "I'm not sure I understood that. Can you rephrase?"
        log_user_interaction(message, response)
        return response
