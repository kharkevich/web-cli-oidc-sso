import React from 'react';
import { getConfig } from '../utils/config';

const Login = ({ style }) => {
  const handleLogin = () => {
    const appConfig = getConfig();
    window.location.href = `${appConfig.authUrl}?redirect_uri=${appConfig.redirectUrl}`;
  };

  return (
    <button style={{ ...style, ...styles.button }} onMouseOver={handleMouseOver} onMouseOut={handleMouseOut} onClick={handleLogin}>
      Login
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

export default Login;
