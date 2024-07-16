// import React from 'react';
// import { Bar } from 'react-chartjs-2';

// const Chart = ({ data }) => {
//   const chartData = {
//     labels: data.map(d => d.topic),
//     datasets: [
//       {
//         label: 'Intensity',
//         data: data.map(d => d.intensity),
//         backgroundColor: 'rgba(75, 192, 192, 0.6)',
//       },
//       {
//         label: 'Likelihood',
//         data: data.map(d => d.likelihood),
//         backgroundColor: 'rgba(153, 102, 255, 0.6)',
//       },
//       {
//         label: 'Relevance',
//         data: data.map(d => d.relevance),
//         backgroundColor: 'rgba(255, 159, 64, 0.6)',
//       },
//     ],
//   };

//   return (
//     <div>
//       <Bar
//         data={chartData}
//         options={{
//           title: {
//             display: true,
//             text: 'Data Visualization',
//             fontSize: 25,
//           },
//           legend: {
//             display: true,
//             position: 'right',
//           },
//         }}
//       />
//     </div>
//   );
// };

// export default Chart;


import React from 'react';
import { Line } from 'react-chartjs-2';

const Chart = ({ data }) => {
  const chartData = {
    labels: data.map((item) => item.label),
    datasets: [
      {
        label: 'Sample Data',
        data: data.map((item) => item.value),
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 1,
      },
    ],
  };

  return (
    <div>
      <Line data={chartData} />
    </div>
  );
};

export default Chart;
