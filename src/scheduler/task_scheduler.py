import time
import logging
from datetime import datetime
import threading

logger = logging.getLogger(__name__)

class TaskScheduler:
    def __init__(self, db_manager, weather_service, notification_service):
        self.db = db_manager
        self.weather_service = weather_service
        self.notification_service = notification_service
        self.running = False

    def start(self):
        """
        Start the scheduler in a separate thread
        """
        self.running = True
        thread = threading.Thread(target=self._run_schedule)
        thread.daemon = True
        thread.start()
        logger.info("Scheduler started")

    def stop(self):
        """
        Stop the scheduler
        """
        self.running = False
        logger.info("Scheduler stopped")

    def _run_schedule(self):
        """
        Main scheduling loop
        """
        while self.running:
            try:
                current_time = datetime.now()
                users = self.db.get_users_for_notification(current_time)

                for user in users:
                    self._process_user_notification(user)

                # Sleep for 60 seconds before next check
                time.sleep(60)
            except Exception as e:
                logger.error(f"Scheduler error: {str(e)}")
                time.sleep(60)  # Wait before retrying

    def _process_user_notification(self, user):
        """
        Process notifications for a single user
        """
        try:
            weather_data = self.weather_service.get_weather(user[2])  # location
            message = self.weather_service.format_weather_message(weather_data)
            self.notification_service.send_notification(user[1], message)  # phone_number
            self.db.log_alert(user[0], "weather_update", message)
        except Exception as e:
            logger.error(f"Error processing notification for user {user[0]}: {str(e)}")