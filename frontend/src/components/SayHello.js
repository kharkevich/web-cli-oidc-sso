import React from 'react';
import axiosInstance from '../utils/axiosInstance';
import { getConfig } from '../utils/config';

const SayHello = ({ style, showMessage }) => {
  const handleHello = async () => {
    try {
      const token = localStorage.getItem('jwt');
      const response = await axiosInstance.get('/hello', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });
      showMessage(response.data.message);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <button style={{ ...style, ...styles.button }} onMouseOver={handleMouseOver} onMouseOut={handleMouseOut} onClick={handleHello}>
      Say Hello (protected url)
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

export default SayHello;
