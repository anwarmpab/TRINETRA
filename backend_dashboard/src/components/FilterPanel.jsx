import React, { useState } from 'react';

const FilterPanel = ({ onFilter }) => {
  const [gesture, setGesture] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const applyFilter = () => {
    onFilter({ gesture, startDate, endDate });
  };

  return (
    <div className="p-4 bg-white shadow rounded mb-4">
      <h2 className="text-lg font-semibold mb-2">🔎 Filter Logs</h2>

      <div className="flex flex-col md:flex-row gap-4">
        <input
          type="text"
          placeholder="Gesture (e.g., Fist)"
          value={gesture}
          onChange={(e) => setGesture(e.target.value)}
          className="border p-2 rounded w-full"
        />
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          className="border p-2 rounded"
        />
        <button
          onClick={applyFilter}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Apply
        </button>
      </div>
    </div>
  );
};

export default FilterPanel;
