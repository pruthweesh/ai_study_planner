import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, []);

  const login = async (credentials) => {
    try {
      const res = await axios.post('http://localhost:8000/api-token-auth/', credentials);
      localStorage.setItem('token', res.data.token);
      const userRes = await axios.get('http://localhost:8000/api/auth/user/', {
        headers: { Authorization: `Token ${res.data.token}` }
      });
      setUser(userRes.data);
      localStorage.setItem('user', JSON.stringify(userRes.data));
      return { success: true };
    } catch (err) {
      return { success: false, error: err.response?.data || 'Login failed' };
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => React.useContext(AuthContext);