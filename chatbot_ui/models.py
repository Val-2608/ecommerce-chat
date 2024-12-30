from extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": self.category,
        }

    def __repr__(self):
        return f"<Product {self.name}>"


class Session(db.Model):
    __tablename__ = 'sessions'

    session_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String)  # Optional: If you implement user authentication
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    chat_logs = db.relationship('ChatLog', backref='session', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
        }

    def __repr__(self):
        return f"<Session {self.session_id}>"


class ChatLog(db.Model):
    __tablename__ = 'chat_logs'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String, db.ForeignKey('sessions.session_id', ondelete="CASCADE"))
    message = db.Column(db.Text, nullable=False)
    sender = db.Column(db.String, nullable=False)  # 'user' or 'bot'
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "session_id": self.session_id,
            "message": self.message,
            "sender": self.sender,
            "timestamp": self.timestamp.isoformat(),
        }

    def __repr__(self):
        return f"<ChatLog {self.id} from {self.sender}>"


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"
