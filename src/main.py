import logging
from database.db_manager import DatabaseManager
from services.weather_service import WeatherService
from services.notification_service import NotificationService
from utils.config import load_config
from scheduler.task_scheduler import TaskScheduler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize services
        config = load_config()
        db = DatabaseManager()
        weather_service = WeatherService(config['weather_api_key'])
        notification_service = NotificationService(config['twilio_account_sid'], 
                                                config['twilio_auth_token'])
        scheduler = TaskScheduler(db, weather_service, notification_service)
        
        # Create database tables if they don't exist
        db.initialize_database()
        
        # Start the scheduler
        scheduler.start()
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    main()