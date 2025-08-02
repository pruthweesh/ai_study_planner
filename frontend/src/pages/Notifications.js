import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/notifications/user/')
      .then(res => {
        setNotifications(res.data);
      })
      .catch(err => {
        console.error('Error fetching notifications:', err);
      });
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Notifications</h1>
      {notifications.length > 0 ? (
        <ul className="space-y-2">
          {notifications.map((note, idx) => (
            <li key={idx} className="bg-blue-100 p-3 rounded">
              <strong>{note.title}</strong>
              <p>{note.message}</p>
              <small className="text-gray-500">{new Date(note.created_at).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No notifications found.</p>
      )}
    </div>
  );
};

export default Notifications;
