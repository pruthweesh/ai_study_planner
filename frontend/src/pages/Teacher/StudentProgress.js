import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../../context/AuthContext';

const StudentProgress = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();

  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const res = await axios.get('http://localhost:8000/api/study/students/', {
          headers: { Authorization: `Token ${localStorage.getItem('token')}` }
        });
        setStudents(res.data);
      } catch (err) {
        console.error('Error fetching students:', err);
      } finally {
        setLoading(false);
      }
    };

    if (user?.role === 'TEACHER') {
      fetchStudents();
    }
  }, [user]);

  return (
    <div className="container">
      <h2>Student Progress Overview</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table className="student-table">
          <thead>
            <tr>
              <th>Student</th>
              <th>Subjects</th>
              <th>Progress</th>
            </tr>
          </thead>
          <tbody>
            {students.map(student => (
              <tr key={student.id}>
                <td>{student.name}</td>
                <td>{student.subjects.join(', ')}</td>
                <td>
                  <div className="progress-bar">
                    <div 
                      className="progress-fill" 
                      style={{ width: `${student.avg_progress}%` }}
                    >
                      {student.avg_progress}%
                    </div>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default StudentProgress;