import React, { useEffect, useState } from "react";
import axios from "axios";

const LogTable = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/logs")  // Your FastAPI endpoint
      .then((res) => setLogs(res.data))
      .catch((err) => console.error("Error fetching logs", err));
  }, []);

  return (
    <div>
      <h2>Gesture Logs</h2>
      <table>
        <thead>
          <tr>
            <th>Gesture</th>
            <th>Timestamp</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{log.gesture}</td>
              <td>{new Date(log.timestamp).toLocaleString()}</td>
              <td>{log.action}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LogTable;
