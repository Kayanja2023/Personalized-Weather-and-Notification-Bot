import json
import os
import logging

logger = logging.getLogger(__name__)

def load_config():
    """
    Load configuration from config.json
    """
    try:
        config_path = "config.json"
        if not os.path.exists(config_path):
            # Create default config file
            default_config = {
                "weather_api_key": "YOUR_OPENWEATHER_API_KEY",
                "twilio_account_sid": "YOUR_TWILIO_ACCOUNT_SID",
                "twilio_auth_token": "YOUR_TWILIO_AUTH_TOKEN"
            }
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=4)
            logger.info("Created default config.json")
            return default_config

        with open(config_path, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        logger.error(f"Error loading config: {str(e)}")
        raise