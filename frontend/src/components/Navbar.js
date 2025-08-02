import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './navbar.css';

const Navbar = () => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem('user'));

  const handleLogout = () => {
    localStorage.clear();
    navigate('/login');
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">🧠 AI Study Planner</Link>
      </div>
      
      {user ? (
        <div className="navbar-links">
          {/* Student Links */}
          {user.role === 'STUDENT' && (
            <>
              <Link to="/dashboard">Dashboard</Link>
              <Link to="/progress">My Progress</Link>
            </>
          )}
          
          {/* Teacher Links */}
          {user.role === 'TEACHER' && (
            <>
              <Link to="/students">Students</Link>
              <Link to="/reports">Reports</Link>
            </>
          )}
          
          {/* Parent Links */}
          {user.role === 'PARENT' && (
            <Link to="/child-progress">Child Progress</Link>
          )}
          
          <Link to="/notifications">Notifications</Link>
          <button onClick={handleLogout} className="logout-btn">Logout</button>
        </div>
      ) : (
        <div className="navbar-links">
          <Link to="/login">Login</Link>
          <Link to="/signup">Signup</Link>
        </div>
      )}
    </nav>
  );
};

export default Navbar;