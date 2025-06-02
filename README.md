# Soccer Cards App

## Overview
The Soccer Cards App is a full-stack application that allows users to log in, scan soccer cards, save them, and view a list of saved cards with filtering options. The application consists of a Python backend built with Flask and a React.js frontend.

## Project Structure
The project is organized into two main directories: `backend` and `frontend`.

### Backend
- **app**: Contains the main application code.
  - **routes**: Defines the API endpoints for authentication and card management.
    - `auth.py`: Handles user login and registration.
    - `cards.py`: Manages soccer card operations (add, retrieve, filter).
  - **models**: Contains the data models for the application.
    - `user.py`: Defines the User model.
    - `card.py`: Defines the Card model.
  - **services**: Contains business logic for authentication and card management.
    - `auth_service.py`: Handles user authentication logic.
    - `card_service.py`: Manages card data operations.
  - **static**: Directory for storing static files (e.g., images).
- `run.py`: Entry point for running the backend application.
- `config.py`: Configuration settings for the backend.
- `requirements.txt`: Lists Python dependencies for the backend.
- `README.md`: Documentation for the backend.

### Frontend
- **public**: Contains static files for the React application.
  - `index.html`: Main HTML file for the React app.
- **src**: Contains the source code for the React application.
  - **components**: Reusable components for the application.
    - **Auth**: Contains authentication-related components.
      - `LoginForm.js`: Component for user login.
    - **Cards**: Contains components for displaying and filtering cards.
      - `CardList.js`: Displays a list of saved cards.
      - `CardItem.js`: Represents a single soccer card.
      - `CardFilter.js`: Allows filtering of cards.
    - **Scanner**: Contains the card scanning component.
      - `CardScanner.js`: Component for scanning soccer cards.
  - **pages**: Contains page components for routing.
    - `LoginPage.js`: Page for user login.
    - `DashboardPage.js`: Main dashboard after login.
    - `ScanPage.js`: Page for scanning and saving cards.
  - **services**: Contains API call functions.
    - `api.js`: Functions for making API calls to the backend.
  - `App.js`: Main component that sets up routing.
  - `index.js`: Entry point for the React application.
- `package.json`: Configuration file for npm, listing dependencies and scripts.
- `README.md`: Documentation for the frontend.

## Features
- User authentication with login functionality.
- Soccer card scanning and saving.
- Display of saved cards with filtering options by date and player name.

## Getting Started
1. Clone the repository.
2. Navigate to the `backend` directory and install the required Python packages using `pip install -r requirements.txt`.
3. Run the backend server using `python run.py`.
4. Navigate to the `frontend` directory and install the required npm packages using `npm install`.
5. Start the React application using `npm start`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.