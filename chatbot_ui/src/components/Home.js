// src/components/Home.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <div className="animated-background">
        <div className="gradient-overlay"></div>
      </div>
      
      <div className="home-content">
        <div className="hero-section">
          <div className="logo-container">
            <div className="logo-circle">
              <span className="logo-text">AI</span>
            </div>
          </div>
          <h1>
            <span className="gradient-text">Smart Shopping</span>
            <br />Assistant
          </h1>
          <p className="subtitle">Experience the future of e-commerce with our AI-powered chatbot</p>
        </div>

        <div className="features">
          <div className="feature-card">
            <div className="feature-icon">🔍</div>
            <h3>Intelligent Search</h3>
            <p>Natural language product search with smart filtering</p>
            <div className="feature-footer">
              <span className="feature-tag">AI-Powered</span>
            </div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Quick Compare</h3>
            <p>Side-by-side product comparison with key features</p>
            <div className="feature-footer">
              <span className="feature-tag">Real-time</span>
            </div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>Smart Details</h3>
            <p>Comprehensive product information and specifications</p>
            <div className="feature-footer">
              <span className="feature-tag">Detailed</span>
            </div>
          </div>
        </div>

        <div className="demo-section">
          <div className="chat-preview">
            <div className="chat-header">
              <div className="chat-dot"></div>
              <div className="chat-dot"></div>
              <div className="chat-dot"></div>
            </div>
            <div className="chat-messages">
              <div className="demo-message user">Show me gaming laptops under $1500</div>
              <div className="demo-message bot">I found 5 gaming laptops within your budget. Here are the top options...</div>
              <div className="demo-message user">Which one has the best graphics card?</div>
            </div>
          </div>
        </div>

        <div className="action-section">
          <h2>Ready to Start Shopping?</h2>
          <div className="action-buttons">
            <button 
              className="primary-button"
              onClick={() => navigate('/login')}
            >
              <span className="button-icon">👤</span>
              Login
            </button>
            <button 
              className="secondary-button"
              onClick={() => navigate('/chat')}
            >
              <span className="button-icon">💬</span>
              Try Demo
            </button>
          </div>
        </div>

        <div className="floating-shapes">
          <div className="shape shape-1"></div>
          <div className="shape shape-2"></div>
          <div className="shape shape-3"></div>
        </div>
      </div>
    </div>
  );
};

export default Home;
