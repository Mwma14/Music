# AnonXMusic Bot - Local Setup Guide

This guide will walk you through the steps to run your modified AnonXMusic bot on your local machine.

## Prerequisites

Before starting, ensure you have the following installed on your system:

1.  **Python 3.9 or higher**: [Download Python](https://www.python.org/downloads/)
2.  **FFmpeg**: Required for audio/video processing.
    *   **Windows**: [Download from gyan.dev](https://www.gyan.dev/ffmpeg/builds/) (add to PATH).
    *   **Linux/macOS**: Use `sudo apt install ffmpeg` or `brew install ffmpeg`.
3.  **Deno**: Required for certain core functionalities.
    *   **Windows (PowerShell)**: `irm https://deno.land/install.ps1 | iex`
    *   **Linux/macOS**: `curl -fsSL https://deno.land/install.sh | sh`
4.  **Git (Optional)**: For cloning or managing the code.

## Configuration

The bot's credentials are already configured in `config.py`. However, if you want to change them, you can edit the following values in `config.py`:

*   `API_ID`: Your Telegram API ID.
*   `API_HASH`: Your Telegram API Hash.
*   `BOT_TOKEN`: Your Telegram Bot Token.
*   `MONGO_URL`: Your MongoDB connection string.
*   `OWNER_ID`: Your Telegram User ID.
*   `SESSION1`: Your Pyrogram string session for the assistant.

## Installation Steps

1.  **Extract the Files**:
    Extract the provided `AnonXMusic_Modified.zip` into a folder of your choice.

2.  **Open Terminal/Command Prompt**:
    Navigate to the extracted folder:
    ```bash
    cd AnonXMusic
    ```

3.  **Create a Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    ```
    *   **Windows**: `venv\Scripts\activate`
    *   **Linux/macOS**: `source venv/bin/activate`

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Bot

Once everything is installed and configured, you can start the bot using:

```bash
python -m anony
```

Alternatively, you can use the provided start scripts:
*   **Linux/macOS**: `bash start`
*   **Windows**: Use `python -m anony` directly.

## Notes
*   Ensure your MongoDB database is active and accessible.
*   The "Source" inline button has been removed as requested.
*   Make sure both FFmpeg and Deno are in your system's PATH.
