import React from 'react';

const Header = () => {
  return (
    <header className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-4 px-6 shadow-md">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <h1 className="text-2xl font-bold tracking-wide">🧠 TRINETRA Dashboard</h1>
        <p className="text-sm font-light hidden md:block">Real-Time Gesture Monitoring System</p>
      </div>
    </header>
  );
};

export default Header;
