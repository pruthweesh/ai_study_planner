import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Progress = () => {
  const [progressData, setProgressData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const userToken = localStorage.getItem('token');

    if (!userToken) {
      setError('User not authenticated');
      setLoading(false);
      return;
    }

    axios
      .get('http://127.0.0.1:8000/api/progress/user/', {
        headers: {
          Authorization: `Token ${userToken}`, // or Bearer for JWT
        },
      })
      .then((res) => {
        setProgressData(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching progress data:', err);
        setError('Failed to fetch progress data.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="page-container p-6">
      <h2 className="text-2xl font-bold mb-4">📈 Progress Tracker</h2>

      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {!loading && !error && progressData.length > 0 ? (
        <div className="space-y-4">
          {progressData.map((item, index) => (
            <div key={index} className="bg-white p-4 rounded shadow">
              <h3 className="text-lg font-semibold mb-2">{item.subject}</h3>
              <div className="w-full bg-gray-200 rounded h-6 overflow-hidden">
                <div
                  className="bg-blue-500 h-full text-white text-sm flex items-center justify-center"
                  style={{ width: `${item.completed}%` }}
                >
                  {item.completed}%
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : (
        !loading && !error && <p>No progress data available.</p>
      )}
    </div>
  );
};

export default Progress;
