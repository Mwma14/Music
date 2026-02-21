# AnonXMusic - Music Bot

This is a powerful Telegram music bot with support for both audio and video playback.

## Prerequisites

Before running the bot, ensure you have the following installed on your system:

1.  **Python 3.10 or higher**
2.  **FFmpeg**: Required for processing audio and video streams.
    -   Ubuntu/Debian: `sudo apt install ffmpeg`
    -   macOS: `brew install ffmpeg`
    -   Windows: Download from [ffmpeg.org](https://ffmpeg.org/)
3.  **Deno**: Required for certain bot core functionalities.
    -   Installation: `curl -fsSL https://deno.land/x/install/install.sh | sh`
    -   Ensure `deno` is in your system PATH.

## Setup and Running

### 1. Install Dependencies

Open your terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 2. Configuration

The credentials have already been hardcoded into `config.py`. No additional `.env` file is required.

### 3. Start the Bot

Run the following command to start the bot:

```bash
python -m anony
```

Or use the provided start script:

```bash
bash start
```

## Features

-   Audio and Video playback.
-   Assistant auto-invite to groups.
-   Queue management.
-   Multi-language support.
-   Sudo user management.

## Support

For any issues, please refer to the support chat links provided in the bot's `/start` message.
