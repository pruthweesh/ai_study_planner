import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Schedule from './pages/Schedule';
import Reports from './pages/Reports';
import Login from './pages/Login';
import Notifications from './pages/Notifications';
import Progress from './pages/Progress';
import Signup from './pages/Signup';
import StudentProgress from './pages/Teacher/StudentProgress';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          
          <Route element={<ProtectedRoute allowedRoles={['STUDENT']} />}>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/progress" element={<Progress />} />
          </Route>
          
          <Route element={<ProtectedRoute allowedRoles={['TEACHER']} />}>
            <Route path="/students" element={<StudentProgress />} />
            <Route path="/reports" element={<Reports />} />
          </Route>
          
          <Route element={<ProtectedRoute allowedRoles={['PARENT']} />}>
            <Route path="/child-progress" element={<Progress />} />
          </Route>
          
          <Route element={<ProtectedRoute allowedRoles={['STUDENT', 'TEACHER', 'PARENT']} />}>
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/schedule" element={<Schedule />} />
          </Route>
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;