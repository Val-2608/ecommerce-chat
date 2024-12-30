import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = () => {
  const [isRegister, setIsRegister] = useState(false); // Toggle between Login and Register
  const [credentials, setCredentials] = useState({
    email: '',
    password: '',
    confirmPassword: '' // For Register form
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const endpoint = isRegister
        ? 'http://127.0.0.1:5000/api/register'  
        : 'http://127.0.0.1:5000/api/login';
      const payload = isRegister
        ? { email: credentials.email, password: credentials.password }
        : { email: credentials.email, password: credentials.password };

      if (isRegister && credentials.password !== credentials.confirmPassword) {
        setError('Passwords do not match');
        return;
      }

      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const data = await response.json();
      if (response.ok) {
        if (isRegister) {
          alert('Registration successful! Please log in.');
          setIsRegister(false); // Switch to login form
        } else {
          localStorage.setItem('sessionId', data.session_id); // Store session ID
          navigate('/chat'); // Redirect to chat
        }
      } else {
        setError(data.error || 'An error occurred. Please try again.');
      }
    } catch (err) {
      setError('Server error. Please try again later.');
    }
  };

  return (
    <div className="login-container">
      <form onSubmit={handleSubmit} className="login-form">
        <h2>{isRegister ? 'Register for E-commerce Chatbot' : 'Login to E-commerce Chatbot'}</h2>
        {error && <div className="error-message">{error}</div>}

        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={credentials.email}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            name="password"
            value={credentials.password}
            onChange={handleChange}
            required
          />
        </div>

        {isRegister && (
          <div className="form-group">
            <label>Confirm Password:</label>
            <input
              type="password"
              name="confirmPassword"
              value={credentials.confirmPassword}
              onChange={handleChange}
              required
            />
          </div>
        )}

        <button type="submit" className="login-button">
          {isRegister ? 'Register' : 'Login'}
        </button>

        <p className="toggle-link">
          {isRegister ? (
            <>
              Already have an account?{' '}
              <span onClick={() => setIsRegister(false)}>Login</span>
            </>
          ) : (
            <>
              Don't have an account?{' '}
              <span onClick={() => setIsRegister(true)}>Register</span>
            </>
          )}
        </p>
      </form>
    </div>
  );
};

export default Login;
