import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Chart from './Chart';
import Filters from './Filters';

const Dashboard = () => {
  const [data, setData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/data')
      .then(response => {
        setData(response.data);
        setFilteredData(response.data);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const handleFilterChange = (filters) => {
    let filtered = data;
    if (filters.endYear) {
      filtered = filtered.filter(d => d.end_year === filters.endYear);
    }
    if (filters.topics) {
      filtered = filtered.filter(d => d.topic.includes(filters.topics));
    }
    // Add more filters as needed
    setFilteredData(filtered);
  };

  return (
    <div>
      <Filters onFilterChange={handleFilterChange} />
      <Chart data={filteredData} />
    </div>
  );
};

export default Dashboard;
