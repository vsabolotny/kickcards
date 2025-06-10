# Soccer Cards App Frontend

This directory contains the React application built with Expo 53. It provides the user interface for logging in, scanning cards and viewing them.

## Available Scripts

- `npm start` - start the development server with Expo
- `npm run web` - run the project in a web browser
- `npm run android` / `npm run ios` - run on a simulator or device

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Auth/
│   │   │   └── LoginForm.js
│   │   ├── Cards/
│   │   │   ├── CardFilter.js
│   │   │   ├── CardItem.js
│   │   │   └── CardList.js
│   │   └── Scanner/
│   │       └── CardScanner.js
│   ├── pages/
│   │   ├── DashboardPage.js
│   │   ├── LoginPage.js
│   │   └── ScanPage.js
│   ├── services/
│   │   └── api.js
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```
