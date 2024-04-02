import React, { useState, useEffect } from 'react';

const LoadingBar = ({ duration = 2000 }) => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress(prevProgress => {
        const newProg = prevProgress + 10;
        return newProg >= 100 ? 100 : newProg;
      });
    }, duration / 10);

    return () => clearInterval(interval);
  }, [duration]);

  return (
    progress < 100 && (
      <div style={{ width: '100%', backgroundColor: '#f0f0f0', borderRadius: '10px', overflow: 'hidden', padding: '2px' }}>
        <div style={{ width: `${progress}%`, backgroundColor: '#90CAF9', height: '10px', borderRadius: '10px' }}></div>
      </div>
    )
  );
};

export default LoadingBar;
