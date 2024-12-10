from twilio.rest import Client
import logging

logger = logging.getLogger(__name__)

class NotificationService:
    def __init__(self, account_sid: str, auth_token: str):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, to_number: str, message: str) -> None:
        """
        Send a notification to a user via Twilio
        """
        try:
            self.client.messages.create(
                body=message,
                from_='+1234567890',  # Your Twilio phone number
                to=to_number
            )
            logger.info(f"Notification sent to {to_number}")
        except Exception as e:
            logger.error(f"Error sending notification: {str(e)}")
            raise