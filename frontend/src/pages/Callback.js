import { useNavigate } from 'react-router-dom';
import { getConfig } from '../utils/config';
import axios from 'axios';
import { useEffect, useRef } from 'react';

const Callback = () => {
  const navigate = useNavigate();
  const hasFetchedToken = useRef(false);

  useEffect(() => {
    console.log('useEffect called');
    const fetchToken = async () => {
      const urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code');
      const state = urlParams.get('state');

      if (code && state && !hasFetchedToken.current) {
        hasFetchedToken.current = true;
        try {
          const appConfig = getConfig();
          const response = await axios.get(
            `${appConfig.callbackUrl}?code=${code}&state=${state}`,
            { withCredentials: true }
          );
          localStorage.setItem('jwt', response.data.jwt);
          navigate('/');
        } catch (error) {
          console.error('Error during token exchange:', error);
        }
      }
    };

    fetchToken();
  }, [navigate]);

  return <h2>Processing Login...</h2>;
};

export default Callback;