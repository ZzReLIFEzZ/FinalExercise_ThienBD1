import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        """Loads the configuration from a JSON file."""
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testtesting.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config
    
    @staticmethod
    def get_base_url():
        """Returns the base URL from the configuration."""
        return ConfigReader.load_config()['base_url']
    
    @staticmethod
    def get_username():
        """Returns the username from the configuration."""
        return ConfigReader.load_config()['credentials']['username']
    
    @staticmethod
    def get_password():
        """Returns the password from the configuration."""
        return ConfigReader.load_config()['credentials']['password']