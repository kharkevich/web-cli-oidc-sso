let config = null;

export const loadConfig = async () => {
  if (config) return config; // Return cached config if already loaded.

  const response = await fetch('/config.json');
  if (!response.ok) {
    throw new Error(`Failed to load configuration: ${response.statusText}`);
  }

  config = await response.json();
  return config;
};

export const getConfig = () => {
  if (!config) {
    throw new Error('Configuration not loaded yet. Call loadConfig() first.');
  }
  return config;
};
