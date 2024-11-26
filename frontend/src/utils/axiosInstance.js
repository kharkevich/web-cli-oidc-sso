import axios from 'axios';
import { getConfig } from './config';

const axiosInstance = axios.create();

axiosInstance.interceptors.request.use(async (config) => {
  const appConfig = getConfig();
  config.baseURL = appConfig.apiBaseUrl;
  return config;
});

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      const appConfig = getConfig();
      window.location.href = `${appConfig.authUrl}?redirect_uri=${appConfig.redirectUrl}`;
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
