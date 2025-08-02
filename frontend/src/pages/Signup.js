import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './signup.css';

const Signup = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    role: 'student'
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/signup/', formData);
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      navigate('/dashboard');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed. Please try again.');
    }
  };

  return (
    <div className="signup-container">
      <form onSubmit={handleSubmit} className="signup-form">
        <h2>Create Account</h2>
        {error && <div className="error-message">{error}</div>}
        
        <div className="form-group">
          <label>Username</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="form-group">
          <label>Email</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            minLength="8"
          />
        </div>
        
        <div className="form-group">
          <label>Role</label>
          <div className="role-options">
            <label>
              <input
                type="radio"
                name="role"
                value="student"
                checked={formData.role === 'student'}
                onChange={handleChange}
              />
              Student
            </label>
            <label>
              <input
                type="radio"
                name="role"
                value="teacher"
                checked={formData.role === 'teacher'}
                onChange={handleChange}
              />
              Teacher
            </label>
            <label>
              <input
                type="radio"
                name="role"
                value="parent"
                checked={formData.role === 'parent'}
                onChange={handleChange}
              />
              Parent
            </label>
          </div>
        </div>
        
        <button type="submit" className="signup-button">Sign Up</button>
        
        <p className="login-link">
          Already have an account? <a href="/login">Login</a>
        </p>
      </form>
    </div>
  );
};

export default Signup;