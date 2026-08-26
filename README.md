# TodoList

A simple command-line TodoList application built with Python.

This project started as a basic Python application and was progressively improved with modular architecture, JSON-based persistence, input validation, error handling, and automated testing.

## Features

- Add tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Prevent duplicate tasks
- Validate menu input
- Persist tasks using JSON
- Handle missing task files
- Handle corrupted JSON files
- Automated unit tests

## Project Structure

TodoList/
│
├── main.py
├── tasks.py
├── ui.py
├── storage.py
│
└── tests/
    ├── test_tasks.py
    └── test_storage.py

## File Responsibilities

- main.py — Controls the application flow and connects the different modules.
- tasks.py — Contains the core task operations.
- ui.py — Handles user input and terminal output.
- storage.py — Handles saving and loading tasks using JSON.
- tests/ — Contains automated tests for task logic and storage.

## How It Works

Tasks are stored as a Python dictionary:

{
    "learn python": False,
    "learn git": True
}

The value represents the task status:

- False — Pending
- True — Completed

The dictionary is saved to tasks.json so that tasks remain available after restarting the application.

## Requirements

- Python 3.10 or newer

## Running the Application

Clone the repository:

git clone https://github.com/piyushhnaikk/TodoList.git

Navigate into the project:

cd TodoList

Run the application:

python main.py

## Running the Tests

The project uses Python's built-in unittest framework.

Run all tests with:

python -m unittest discover -s tests -v

Current test status:

11 tests passed
0 failures
0 errors

The tests cover:

- Adding tasks
- Duplicate tasks
- Completing pending tasks
- Completing already completed tasks
- Completing non-existent tasks
- Deleting tasks
- Deleting non-existent tasks
- Missing JSON files
- Saving and loading tasks
- Corrupted JSON files

## Error Handling

The application handles common problems gracefully.

### Missing JSON File

If tasks.json does not exist, the application starts with an empty task dictionary.

### Corrupted JSON

If the JSON file contains invalid data, the storage layer handles the JSON decoding error and starts with an empty task dictionary instead of crashing.

### Invalid Menu Input

The application rejects:

- Non-numeric input
- Numbers outside the range 1–5

## Technologies Used

- Python
- JSON
- unittest
- Git
- GitHub

## What I Learned

Through this project, I practiced:

- Python functions and dictionaries
- Modular programming
- Separation of concerns
- Input validation
- Exception handling
- JSON file persistence
- Unit testing
- Test setup and cleanup using setUp() and tearDown()
- Debugging and identifying real bugs through tests
- Git and GitHub workflow

## Project Status

The core TodoList application is complete.

The application has been manually tested and currently has 11 automated tests passing with no failures or errors.

The next step is packaging the application as a Windows executable and publishing a release.

## Future Improvements

Potential future improvements include:

- Graphical user interface
- Due dates and priorities
- More advanced task organization
- Support for additional platforms

These features are intentionally outside the current scope of the project.

## Author

Piyush Naik

B.Tech CSE (AIML)

GitHub: https://github.com/piyushhnaikk/TodoList