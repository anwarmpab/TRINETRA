import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Your FastAPI server

export const fetchLogs = () => axios.get(`${API_URL}/logs`);
export const fetchByGesture = (gesture) => axios.get(`${API_URL}/logs/by-gesture`, { params: { gesture } });
export const fetchByDateRange = (start, end) =>
  axios.get(`${API_URL}/logs/by-date`, { params: { start_date: start, end_date: end } });
