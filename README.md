# Weather Notification Bot

Weather Notification Bot is a Python application that fetches weather data for a given location and sends notifications to users via Twilio. The application uses a scheduler to periodically check for users who need to be notified based on their preferred notification time.

## Project Structure

```
.APIWeatherApp/
	config.json
.gitignore
config.json
index.js
package.json
requirements.txt
src/
	database/
		__pycache__/
		db_manager.py
	main.py
	scheduler/
		task_scheduler.py
	services/
		notification_service.py
		weather_service.py
	utils/
		config.py
tests/
	test_weather_service.py
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-notification-bot.git
    cd weather-notification-bot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create and configure 

config.json

:
    ```json
    {
        "weather_api_key": "YOUR_OPENWEATHER_API_KEY",
        "twilio_account_sid": "YOUR_TWILIO_ACCOUNT_SID",
        "twilio_auth_token": "YOUR_TWILIO_AUTH_TOKEN"
    }
    ```

## Usage

1. Initialize the database:
    ```sh
    python src/main.py
    ```

2. Start the application:
    ```sh
    npm start
    ```

## Running Tests

To run the tests, use the following command:
```sh
npm test
```

## Project Components

### Main Application

- **src/main.py**: Entry point of the application. Initializes services and starts the scheduler.

### Services

- **src/services/weather_service.py**: Fetches weather data from the OpenWeatherMap API.
- **src/services/notification_service.py**: Sends notifications to users via Twilio.

### Scheduler

- **src/scheduler/task_scheduler.py**: Periodically checks for users who need to be notified and processes notifications.

### Database

- **src/database/db_manager.py**: Manages database operations, including adding users and logging alerts.

### Utilities

- **src/utils/config.py**: Loads configuration from 

config.json

.

### Tests

- **tests/test_weather_service.py**: Unit tests for the 

WeatherService

 class.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API.
- [Twilio](https://www.twilio.com/) for providing the SMS notification service.

Similar code found with 1 license type