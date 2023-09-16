# Automation Engineer MoonActive Home Assignment

Welcome to the  MoonActive Home Assignment :)

This project is organized into several directories and files to keep both API abd UI testing efforts well-structured and maintainable:

### `backend`

The `backend` directory contains the core components for API testing.

- **`config`**: This directory stores API configuration and settings.
  - `config.json`: Configuration file for API settings.

- **`endpoints`**: This directory holds API endpoints definitions for different resources.
  - `pet.py`: API endpoints related to the 'pet' resource.

- **`tests`**: This directory is dedicated to test cases for pet API resources.
  - `test_pet.py`: Test cases for the 'pet' resource.

- **`utils`**: Utility functions and modules for API testing.
  - `api_client.py`: API client for making HTTP requests.
  - `assertions.py`: Custom assertion functions for test validations.
  - `helpers.py`: Utility functions to assist with testing.

###  `UI Testing (front)`

The `front` directory contains the components for UI testing.

- **`config`**: This directory stores UI configuration and settings.
  - `config.json`: Configuration file for front-end settings.

- **`data-for-test`**: Data files for UI tests.
  - `calendar_data_for_tests.py`: Data for UI tests related to the calendar.

- **`pages`**: Page objects for UI tests.
  - `base_page.py`: Base page class for UI tests.
  - `calendar_page.py`: Page object for interacting with the calendar.

- **`tests`**: This directory contains UI test cases.
  - `test_calendar.py`: UI test cases for the calendar.
  - `conftest.py`: hold pytest fixtuers for UI tests.

- **`utils`**: Utility functions and modules for UI testing.
  - `driver_manager.py`: Driver manager for handling browser instances.

**`requirements.txt`**: This file lists the project dependencies. Use `pip install -r requirements.txt` to install them.

**`README.md`**: You are reading this file! It provides an overview of the project and its structure.


## Getting Started

To start using this API and UI Test Infrastructure for your project, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/RivkaTestGit/MoonActive.git
   ```

2. Navigate to the project directory and create venv to install dependencies:
- For Windows:
  ```bash
  python -m venv venv
  ``` 


- For macOS:
  
  ```bash
  python3 -m venv venv
  ```

3. Activate the virtual environment:
- For Windows:

   ```bash
   venv\Scripts\activate
    ```

- For macOS:

   ```bash
   source venv/bin/activate
   ```

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run tests:
API tests - navigate to the backend folder and run:
 
    ```bash
    pytest
    ```

  UI tests - navigate to the FRON folder and run:
      
    ```bash
    pytest
   ```


