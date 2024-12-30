


# E-commerce Sales Chatbot

An AI-powered chatbot designed for an e-commerce platform to assist users in finding products, filtering by category and price, and providing a seamless shopping experience.

## Table of Contents

1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Installation](#installation)
4. [Technology Stack](#technology-stack)
5. [Database Schema](#database-schema)
6. [API Endpoints](#api-endpoints)
7. [Frontend Implementation](#frontend-implementation)
8. [Backend Implementation](#backend-implementation)
9. [Security Measures](#security-measures)
10. [Testing](#testing)
11. [Challenges and Solutions](#challenges-and-solutions)
12. [Future Improvements](#future-improvements)
13. [Deployment Guidelines](#deployment-guidelines)
14. [Maintenance](#maintenance)
15. [Contributing](#contributing)
16. [License](#license)

## Introduction

This project is an AI-driven e-commerce sales chatbot built to help customers find products, filter them by category, view product details, and engage in a seamless conversation about their shopping preferences. It leverages natural language processing (NLP) to understand customer queries and guide them effectively.

## System Architecture

The system architecture is composed of the following components:


E-commerce Chatbot
├── Frontend (React)
│   ├── Chat Interface
│   ├── Home Page
│   └── Login/Register
├── Backend (Flask)
│   ├── API Routes
│   ├── Database Models
│   └── Chat Logic
└── Database (SQLite)
    ├── Users
    ├── Products
    ├── Sessions
    └── ChatLogs
```

### Components Overview:
- Frontend: React-based chat interface for real-time interaction.
- Backend: Flask-based API for processing user queries, handling authentication, and managing product data.
- Database: SQLite to store user data, products, session information, and chat logs.

## Installation

### Prerequisites

- Node.js for the frontend
- Python 3.x for the backend
- SQLite for the database

### Steps for Setup

#### Frontend

1. Navigate to the frontend directory:
  
   cd chatbot_ui
   

2. Install dependencies:
   npm install
   

3. Start the React development server:
   
   npm start
   

#### Backend

1. Navigate to the backend directory:
   
   cd chatbot_ui
   

2. Activate the virtual environment:
  
   .\env\Scripts\activate
   

3. Run the Flask app:
   
   flask run(or python app.py)
   

## Technology Stack

- Frontend: React.js
- Backend: Flask (Python)
- Database: SQLite
- Authentication: JWT-based session management
- API: RESTful architecture
- Chatbot: Simple keyword-based routing and structured responses

## Database Schema

### Users Table
Stores user information such as email and hashed password.


CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL
);


### Products Table
Stores details of the products including name, price, description, and category.


CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50) NOT NULL
);

 Sessions Table
Tracks user sessions for authentication.


CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id VARCHAR(36) UNIQUE NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


### Chat Logs Table
Logs each interaction with the chatbot.


CREATE TABLE chat_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id VARCHAR(36) NOT NULL,
    message TEXT NOT NULL,
    sender VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


## API Endpoints

### Authentication Endpoints

- POST /api/register: Register a new user.
  - Payload: `{email, password}`
  
- POST /api/login: User login.
  - Payload: `{email, password}`
  - Returns: `{session_id, message}`

### Product Endpoints

- GET /products: Fetch all products, optional filter by category.
- GET /products/<product_id>: Fetch details of a specific product.

### Chat Endpoints

- POST /api/chat: Sends a message to the chatbot and processes the bot's response.
  - Payload: `{session_id, message}`
  - Returns: `{status, bot_response}`

## Frontend Implementation

### Key Components:
- Chat Container: Displays the conversation history.
- Message Display: Renders user and bot messages.
- Input Form: Captures user input for the chatbot.
- Session Management: Manages JWT tokens for authentication.

### State Management Example:

const [messages, setMessages] = useState([]);
const [sessionId, setSessionId] = useState(null);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);


## Backend Implementation

The backend is developed using Flask and contains the following components:

- models.py: Defines the database models (e.g., User, Product).
- routes.py: Handles API routes for user registration, login, and chatbot interactions.
- extensions.py: Contains configurations for Flask extensions like CORS and SQLAlchemy.

## Security Measures

- Password Hashing: Passwords are hashed using Werkzeug.
- Session-based Authentication: JWT tokens are used for maintaining authenticated sessions.
- CORS Protection: Configured to restrict unauthorized access.

## Testing

### API Testing:
- `/test-db`: Tests the database connection.
- `/add-test-product`: Adds a test product to the database.

### Chat Testing:
- Product queries
- Category browsing
- Price inquiries
- Error handling

## Challenges and Solutions

- Session Management: Ensuring that user sessions are maintained across chat interactions was resolved by implementing UUID-based session tracking and database persistence.
  
- Database Performance: Optimized product search queries by adding indexes and implementing efficient filtering mechanisms.

## Future Improvements

- Natural Language Processing (NLP): Enhance the bot’s ability to understand and process natural language queries.
- Product Recommendations: Implement AI-based product recommendations.
- Order Processing: Integrate with an e-commerce checkout system for order processing.
- Multi-language Support: Add support for multiple languages to reach a broader audience.

## Deployment Guidelines

1. Set up environment variables for API keys and sensitive information.
2. Configure the database connection.
3. Deploy the app on cloud platforms such as Heroku or AWS.

## Maintenance

- Regular database backups.
- Log rotation for efficient log management.
- Performance monitoring to ensure smooth operations.
- Implement security updates and keep the system up-to-date.

## Contributing

We welcome contributions! If you'd like to improve the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Key Sections:

1. Introduction: A short description of the project.
2. System Architecture: Overview of how the project is structured.
3. Installation: Detailed instructions on setting up the project locally.
4. Technology Stack: A list of technologies used.
5. Database Schema: Explanation of database tables.
6. API Endpoints: Details of the available endpoints for the backend.
7. Frontend Implementation: Information on the frontend React components.
8. Backend Implementation: Details on the Flask backend and code structure.
9. Security Measures: Information on how security is handled.
10. Testing: How to test the application.
11. Challenges and Solutions: Any major challenges faced and how they were solved.
12. Future Improvements: Ideas for future features or enhancements.
13. Deployment Guidelines: How to deploy the application.
14. Maintenance: What needs to be done for maintaining the project.
15. Contributing: How others can contribute to the project.
16. License: The project’s license.

