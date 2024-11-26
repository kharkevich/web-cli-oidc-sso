import React, { useState, useEffect } from 'react';
import Login from '../components/Login';
import Logout from '../components/Logout';
import SayHello from '../components/SayHello';

const Home = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('jwt'));
  const [modalMessage, setModalMessage] = useState('');

  useEffect(() => {
    if (modalMessage) {
      const timer = setTimeout(() => {
        closeModal();
      }, 2000);

      const handleKeyDown = (e) => {
        if (e.key === 'Escape') {
          closeModal();
        }
      };

      window.addEventListener('keydown', handleKeyDown);

      return () => {
        clearTimeout(timer);
        window.removeEventListener('keydown', handleKeyDown);
      };
    }
  }, [modalMessage]);

  const handleLogout = () => {
    localStorage.removeItem('jwt');
    setIsLoggedIn(false);
    setModalMessage('Logged out successfully!');
  };

  const closeModal = () => {
    setModalMessage('');
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>OIDC App Demo page</h2>
      <div style={styles.buttonContainer}>
        {!isLoggedIn && <Login style={styles.button} />}
        {isLoggedIn && <Logout style={styles.button} onLogout={handleLogout} />}
        <SayHello style={styles.button} showMessage={setModalMessage} />
      </div>
      {modalMessage && (
        <div style={styles.modalOverlay} onClick={closeModal}>
          <div style={styles.modal}>
            <p>{modalMessage}</p>
            <button style={styles.closeButton} onClick={closeModal}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: '200px',
    backgroundColor: '#e0f7fa',
    borderRadius: '12px',
    boxShadow: '0 6px 12px rgba(0, 0, 0, 0.1)',
    transition: 'background-color 0.3s ease',
  },
  header: {
    color: '#00796b',
    marginBottom: '20px',
    fontFamily: 'Arial, sans-serif',
    fontSize: '24px',
  },
  buttonContainer: {
    display: 'flex',
    gap: '15px',
  },
  button: {
    padding: '10px 20px',
    borderRadius: '8px',
    border: 'none',
    backgroundColor: '#0078d4',
    color: '#ffffff',
    cursor: 'pointer',
    transition: 'background-color 0.3s ease, transform 0.3s ease',
  },
  buttonHover: {
    backgroundColor: '#005a9e',
    transform: 'scale(1.05)',
  },
  popup: {
    position: 'fixed',
    bottom: '20px',
    left: '50%',
    transform: 'translateX(-50%)',
    backgroundColor: '#333',
    color: '#fff',
    padding: '10px 20px',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    zIndex: 1000,
  },
  modalOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
  },
  modal: {
    backgroundColor: '#fff',
    padding: '20px',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    textAlign: 'center',
  },
  closeButton: {
    marginTop: '10px',
    padding: '10px 20px',
    borderRadius: '8px',
    border: 'none',
    backgroundColor: '#0078d4',
    color: '#ffffff',
    cursor: 'pointer',
    transition: 'background-color 0.3s ease',
  },
};

export default Home;
