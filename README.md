
# Project Setup and Usage Instructions

## Project Description

This repository uses OpenAI to upload PDFs to a vector database to query and allow the user to query it.

## Prerequisites

You need an [OpenAI Account](https://platform.openai.com) and API key to use this. For more information, refer to [Account setup](https://platform.openai.com/docs/quickstart/account-setup).

## Setup Instructions

Follow these steps to set up and run the project:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/pechea/openai-chat.git
    cd openai-chat
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv env
    ```

3. **Activate the virtual environment:**
    ```bash
    source env/bin/activate
    ```

4. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your OpenAI API key:**
    ```bash
    export OPENAI_API_KEY=<api key>
    ```

6. **Run the main script:**
    ```bash
    python main.py
    ```

## Example Usage

You can use the following example text to interact with the application:

```text
Please summarize the PDF
```

The PDF is in the `docs` directory. You can add your own.
