# 🤖 AI Code Explainer

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [API Key Setup](#api-key-setup)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

The AI Code Explainer is a Streamlit web application that leverages Google's Gemini AI to provide beginner-friendly explanations for various programming code snippets. Whether you're learning a new language or need a quick clarification on a piece of code, this tool aims to simplify complex concepts into easy-to-understand explanations.

This version of the application directly utilizes the `requests` library to interact with the Gemini API, providing a clear demonstration of API integration in Python.

## Features

* **Multi-Language Support:** Explain code in Python, JavaScript, C++, Java, Go, Ruby, PHP, Swift, Kotlin, Rust, TypeScript, and other languages.
* **Beginner-Friendly Explanations:** Focuses on clarity and simplicity, breaking down complex parts without including the original code or generic language introductions.
* **Intuitive UI:** Built with Streamlit for a clean and easy-to-use interface.
* **Robust Error Handling:** Provides clear messages for API errors (invalid key, rate limits, connection issues, etc.).

## Getting Started

Follow these instructions to get your local copy of the project up and running.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

* Python 3.8 or higher
* `pip` (Python package installer)

### Installation

1.  **Clone the repository (or download the `ai_code_explainer.py` file):**
    If you're using Git:
    ```bash
    git clone <your-repository-url> # Replace with your actual repository URL if applicable
    cd ai_code_explainer_project # Or wherever your file is located
    ```
    If you downloaded the file directly, navigate to its directory:
    ```bash
    cd path/to/your/AI CODE folder
    ```

2.  **Create a Virtual Environment (Recommended):**
    It's highly recommended to use a virtual environment to manage dependencies and avoid conflicts.
    ```bash
    python -m venv venv_explainer
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows (Command Prompt):**
        ```bash
        venv_explainer\Scripts\activate
        ```
    * **On Windows (PowerShell):**
        ```powershell
        .\venv_explainer\Scripts\Activate.ps1
        ```
    * **On macOS/Linux:**
        ```bash
        source venv_explainer/bin/activate
        ```
    Your terminal prompt should now show `(venv_explainer)` indicating the environment is active.

4.  **Install Required Libraries:**
    ```bash
    pip install streamlit requests
    ```

### API Key Setup

This application requires a Google Gemini API key to function.

1.  **Get Your Gemini API Key:**
    * Go to [Google AI Studio](https://aistudio.google.com/).
    * Sign in with your Google account.
    * Navigate to "Get API key" or "API keys" on the left sidebar.
    * Generate a new API key.

2.  **Add the API Key to Your Code:**
    Open the `ai_code_explainer.py` file and locate the line:
    ```python
    MY_GEMINI_API_KEY = "PASTE YOUR API KEY HERE" # <<< PASTE YOUR API KEY HERE >>>
    ```
    Replace `"PASTE YOUR API KEY HERE"` with your actual, copied Gemini API key.

    **Security Note:** For production deployments or public repositories, avoid hardcoding your API key directly in the script. Instead, use Streamlit Secrets or environment variables (`os.getenv`).

    *Example using Streamlit Secrets (Recommended for deployment):*
    1. Create a folder named `.streamlit` in your app's root directory.
    2. Inside `.streamlit`, create a file named `secrets.toml`.
    3. Add your API key to `secrets.toml`:
        ```toml
        GEMINI_API_KEY = "your_actual_gemini_api_key_here"
        ```
    4. In your `ai_code_explainer.py` script, replace the hardcoded key with:
        ```python
        MY_GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
        ```

3.  **Model Selection (Optional but Recommended to Check):**
    The current code uses `GEMINI_MODEL_NAME = "gemini-1.5-flash"`. If you encounter `403 Forbidden` errors even with a valid API key, try switching to a more widely available model like `"gemini-pro"`:
    ```python
    GEMINI_MODEL_NAME = "gemini-pro"
    ```

### Running the Application

Once you have installed the dependencies and set up your API key, run the application from your terminal:

```bash
streamlit run ai_code_explainer.py
