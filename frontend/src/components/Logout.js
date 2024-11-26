import React from 'react';

const Logout = ({ style, onLogout }) => {
  return (
    <button style={{ ...style, ...styles.button }} onMouseOver={handleMouseOver} onMouseOut={handleMouseOut} onClick={onLogout}>
      Logout
    </button>
  );
};

const styles = {
  button: {
  },
  buttonHover: {
    backgroundColor: '#005a9e',
    transform: 'scale(1.05)',
  },
};

const handleMouseOver = (e) => {
  e.target.style.backgroundColor = styles.buttonHover.backgroundColor;
  e.target.style.transform = styles.buttonHover.transform;
};

const handleMouseOut = (e) => {
  e.target.style.backgroundColor = styles.button.backgroundColor;
  e.target.style.transform = 'none';
};

export default Logout;
