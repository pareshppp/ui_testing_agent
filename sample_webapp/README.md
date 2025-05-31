# Sample Web Application

This is a sample web application with a React frontend and FastAPI backend.

## Prerequisites

- Node.js (v14 or higher)
- Python 3.7 or higher
- pip (Python package installer)

## Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd src/sample_webapp/backend
   ```

2. Install the required Python packages:
   ```bash
   pip install fastapi uvicorn python-multipart
   ```

3. Start the FastAPI server:
   ```bash
   python main.py
   ```

   The backend will be available at `http://localhost:8000`

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd src/sample_webapp/frontend
   ```

2. Install the required Node.js packages:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`

## Features

- Form with Name, Email, Phone, and Message fields
- Form validation
- Modal popup showing the API response
- Responsive design that works on mobile and desktop
- Clean and modern UI

## Project Structure

```
src/sample_webapp/
├── backend/
│   ├── main.py           # FastAPI backend
│   └── data/             # Directory where form submissions are stored
└── frontend/
    ├── public/           # Static files
    └── src/
        ├── App.js        # Main React component
        ├── App.css       # Main styles
        ├── index.js      # Entry point
        └── index.css     # Base styles
```
