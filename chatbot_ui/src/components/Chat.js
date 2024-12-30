import React, { useState, useRef, useEffect } from 'react';
import './Chat.css';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);
  const [loading, setLoading] = useState(false);
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    // Retrieve session ID from local storage
    const storedSessionId = localStorage.getItem('sessionId');
    if (storedSessionId) {
      setSessionId(storedSessionId);
    } else {
      setError('No session found. Please login first.');
    }
  }, []);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const validateMessage = (message) => {
    return message.trim().length > 0 && message.trim().length <= 1000;
  };

  const handleSend = async (e) => {
    e.preventDefault();
    if (!validateMessage(inputMessage)) return;

    const newMessage = {
      content: inputMessage,
      timestamp: new Date().toLocaleTimeString(),
      sender: 'user',
    };

    setMessages((prev) => [...prev, newMessage]);
    setInputMessage('');
    setLoading(true);
    setIsTyping(true);

    try {
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_id: sessionId,
          message: inputMessage,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch response from the bot');
      }

      const data = await response.json();
      
      if (data.status === 'success' && data.bot_response) {
        const botMessage = {
          content: data.bot_response,
          timestamp: new Date().toLocaleTimeString(),
          sender: 'bot',
        };
        setMessages((prev) => [...prev, botMessage]);
      } else {
        throw new Error(data.message || 'Invalid response from server');
      }

    } catch (error) {
      console.error('Error fetching response:', error);
      const errorMessage = {
        content: "Sorry, I encountered an error. Please try again.",
        timestamp: new Date().toLocaleTimeString(),
        sender: 'bot',
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
      setIsTyping(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>E-commerce Assistant</h2>
        <button
          className="reset-button"
          onClick={() => setMessages([])}
        >
          Reset Chat
        </button>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <div className="messages-container">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.sender}-message`}
          >
            <div className="message-content">{message.content}</div>
            <div className="message-timestamp">{message.timestamp}</div>
          </div>
        ))}
        {isTyping && (
          <div className="message bot-message">
            <div className="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSend} className="input-container">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="Type your message here..."
          className="message-input"
          maxLength={1000}
          disabled={loading || !sessionId}
        />
        <button 
          type="submit" 
          className="send-button" 
          disabled={loading || !validateMessage(inputMessage) || !sessionId}
        >
          {loading ? 'Sending...' : 'Send'}
        </button>
      </form>
    </div>
  );
};

export default Chat;
