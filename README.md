# Markdown Readme Generator

This project provides a Python-based utility to automatically generate a `README.md` file for a specified directory. It leverages the Google GenAI model to create descriptive READMEs by analyzing the contents of the project files, while respecting `.gitignore` rules to exclude irrelevant files like virtual environments.

## Features

*   **AI-Powered README Generation**: Utilizes the Google GenAI model to intelligently summarize project files and create comprehensive READMEs.
*   **`.gitignore` Integration**: Automatically identifies and ignores files/directories specified in a `.gitignore` file, ensuring only relevant source code is processed.
*   **Easy Setup**: Includes a `setup.bat` script for quick environment setup and dependency installation.
*   **File Reading Utility**: Reads content of various files (excluding ignored ones) to provide context for AI generation.

## Prerequisites

*   Python 3.x installed on your system.
*   An API key for Google GenAI. This key should be set as an environment variable named `GOOGLE_API_KEY`. You can place it in a `.env` file in the project root (e.g., `GOOGLE_API_KEY=your_api_key_here`).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bintadik/md-generator.git
    cd md-generator
    ```
    (Replace with your actual repository URL)

2.  **Run the setup script (for Windows users):**

    ```cmd
    setup.bat
    ```
    This script will perform the following actions:
    *   Create a Python virtual environment named `venv`.
    *   Activate the virtual environment.
    *   Install all necessary dependencies listed in `requirements.txt`.

    Alternatively, for manual setup (or on other operating systems like Linux/macOS):

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On Linux/macOS:
    # source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

1.  **Activate the virtual environment** (if it's not already active from running `setup.bat`):

    ```cmd
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate # On Linux/macOS
    ```

2.  **Run the `create_md.py` script:**

    ```bash
    python create_md.py
    ```

3.  The script will prompt you to `Enter the path to the folder you want to generate a README for:`. Provide the absolute or relative path to your desired project folder.

4.  A `README.md` file will be generated in the current directory (where `create_md.py` is located), containing the AI-generated description and summary of the specified folder's contents.

## Project Structure

```
.
├── .gitignore          # Specifies files and directories to be ignored by Git and the README generator.
├── create_md.py        # The main Python script that reads project files, interacts with GenAI, and generates README.md.
├── requirements.txt    # Lists Python libraries required for the project.
└── setup.bat           # A Windows batch script to automate the setup of the Python virtual environment and dependencies.
└── .env                # (Optional) File to store environment variables like GOOGLE_API_KEY.
```