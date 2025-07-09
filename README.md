# Markdown README Generator for GitHub

This project provides a Python-based tool to automate the generation of GitHub README files. It works by analyzing the contents of a specified project directory, filtering out ignored files using `.gitignore` rules, and then sending the collected code snippets to a large language model (Google Gemini) to generate a comprehensive `README.md`.

## Features

*   **Automated README Generation**: Quickly create a `README.md` for your projects.
*   **`.gitignore` Integration**: Automatically excludes files and directories specified in your `.gitignore` file, ensuring only relevant code is processed.
*   **AI-Powered Content Creation**: Leverages the Google Gemini API to intelligently summarize and generate descriptive README content based on your codebase.
*   **Easy Setup**: Includes a `setup.bat` script for simple virtual environment creation and dependency installation.

## Prerequisites

Before you begin, ensure you have:

*   Python 3.x installed.
*   An active internet connection.
*   A Google API Key for accessing the Gemini API. This key should be set as an environment variable named `GOOGLE_API_KEY` or stored in a `.env` file in the project's root directory.

## Installation

Follow these steps to set up the project:

1.  **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd md-generator
    ```

2.  **Run the Setup Script**:
    Execute the `setup.bat` script to create a Python virtual environment and install all necessary dependencies.

    ```bash
    setup.bat
    ```

    This script will:
    *   Create a virtual environment named `venv/` (if it doesn't exist).
    *   Activate the virtual environment.
    *   Install the packages listed in `requirements.txt`.

## Usage

To generate a README file for your project:

1.  **Ensure API Key is Set**: Make sure your `GOOGLE_API_KEY` environment variable is configured or present in a `.env` file.

2.  **Run the Generator Script**:
    ```bash
    python create_md.py
    ```

3.  **Enter Project Folder Path**:
    The script will prompt you to enter the path to the folder for which you want to generate a README. Provide the absolute or relative path to your project directory.

    Example:
    ```
    Enter the path to the folder you want to generate a README for: C:\Users\YourUser\Documents\my_project
    ```

    Upon successful execution, a `README.md` file will be created or updated directly within the specified project folder.

## Project Structure

```
.
├── .gitignore
├── create_md.py
├── requirements.txt
├── setup.bat
└── venv/ (ignored by .gitignore)
```

*   **`.gitignore`**: Defines files and directories that Git should ignore, such as the `venv/` directory and `.env` files. These patterns are also used by `create_md.py` to filter files for README generation.
*   **`create_md.py`**: The main Python script that orchestrates the README generation process. It reads project files (respecting `.gitignore`), consolidates their content, and sends it to the Gemini model for README creation.
*   **`requirements.txt`**: Lists all Python dependencies required by `create_md.py` (e.g., `google-genai`, `python-dotenv`, `pathspec`).
*   **`setup.bat`**: A simple Windows batch script to automate the setup of the Python virtual environment and installation of required packages.
*   **`venv/`**: (Virtual Environment Directory) Contains the isolated Python environment and its installed packages. This directory is excluded from version control.