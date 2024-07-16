import React, { useState } from 'react';

const Filters = ({ onFilterChange }) => {
  const [endYear, setEndYear] = useState('');
  const [topics, setTopics] = useState('');

  const handleFilterChange = () => {
    onFilterChange({ endYear, topics });
  };

  return (
    <div>
      <label>
        End Year:
        <input type="text" value={endYear} onChange={(e) => setEndYear(e.target.value)} />
      </label>
      <label>
        Topics:
        <input type="text" value={topics} onChange={(e) => setTopics(e.target.value)} />
      </label>
      <button onClick={handleFilterChange}>Apply Filters</button>
    </div>
  );
};

export default Filters;
