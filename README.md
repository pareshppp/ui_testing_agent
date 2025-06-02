# UI Testing Agent

A Python-based UI testing agent for automating browser interactions and testing web applications.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (Python package installer and virtual environment manager)
- Google Chrome browser installed

## Setup

1. Clone the repository (if you haven't already):
   ```bash
   git clone https://github.com/pareshppp/ui-testing-agent.git
   cd ui-testing-agent
   ```

2. Create and activate a virtual environment using `uv` (recommended):
   ```bash
   uv venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. Install the required Python packages using `uv`:
   ```bash
   uv sync
   ```
   
4. Install playwright:
   ```bash
   uv run playwright install-deps
   uv run playwright install
   ```

## Setup & Run Sample Webapp

Instructions for setting up and running the sample webapp.

### Backend

1.  **Navigate to the Backend Directory:**
    Locate the directory containing your backend application code.
    ```bash
    cd sample_webapp/backend
    ```

2.  **Start the Backend Server:**
    Launch the backend application.
    ```bash
    python main.py
    ```
    After starting, the backend server will start running on `http://localhost:8000`.

### Frontend

Instructions for setting up and running the frontend of the web application.

1.  **Navigate to the Frontend Directory:**
    Locate the directory containing your frontend application code.
    ```bash
    cd sample_webapp/frontend
    ```

2.  **Install Dependencies:**
    Install the necessary libraries and packages for the frontend.
    ```bash
    npm install
    ```

3.  **Start the Frontend Development Server:**
    Launch the frontend application.
    ```bash
    npm start
    # or
    # npm run dev
    ```
    After starting, the frontend application will be accessible via your web browser, at address `http://localhost:3000`.


## Usage for UI Testing Agent

The UI Testing Agent comes with several task prompts for different testing scenarios:

### Running the Sample Web App Test

Update `task` in `src/ui_testing_agent/agent.py` to `task_sample_webapp` and run:

```bash
python src/ui_testing_agent/agent.py
```

### Running Google Search Test

Update `task` in `src/ui_testing_agent/agent.py` to `task_google_search` and run:

```bash
python src/ui_testing_agent/agent.py
```

### Running Custom Task

To run a custom task, create a new task prompt file in the `src/ui_testing_agent/` directory and update `task` in `src/ui_testing_agent/agent.py` to your task name and run:

```bash
python src/ui_testing_agent/agent.py
```


## Project Structure

```
sample_webapp/
├── backend/
│   ├── main.py
│   └── ...
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.js
│   │   ├── ...
│   │   └── index.js
│   └── ...
└── ...

src/ui_testing_agent/
├── __init__.py         # Package initialization
├── agent.py            # Main agent implementation
├── task_prompt_sample_webapp.py  # Sample web app test scenario
├── task_prompt_google_search.py  # Google search test scenario
└── task_prompt_v1.py   # Version 1 task prompt

```

## Configuration

Create a `.env` file in the project root with the following variables:

```
GEMINI_API_KEY=your_gemini_api_key
# Add other environment variables as needed
```
