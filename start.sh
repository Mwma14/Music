#!/bin/bash

# AnonXMusic Start Script for bot-hosting.net and Pterodactyl Panels

echo "--- Starting AnonXMusic Setup Check ---"

# 1. Check for FFmpeg
if command -v ffmpeg >/dev/null 2>&1; then
    echo "[OK] FFmpeg is installed at $(command -v ffmpeg)"
else
    echo "[ERROR] FFmpeg not found in PATH. Please ensure it's installed in your hosting environment."
fi

# 2. Check for Deno
if command -v deno >/dev/null 2>&1; then
    echo "[OK] Deno is installed at $(command -v deno)"
else
    # Try common Deno installation paths if not in PATH
    if [ -f "$HOME/.deno/bin/deno" ]; then
        export DENO_INSTALL="$HOME/.deno"
        export PATH="$DENO_INSTALL/bin:$PATH"
        echo "[OK] Deno found at $HOME/.deno/bin/deno and added to PATH."
    else
        echo "[ERROR] Deno not found. Please install it using: curl -fsSL https://deno.land/x/install/install.sh | sh"
    fi
fi

# 3. Ensure dependencies are installed (optional but recommended for first run)
if [ -f "requirements.txt" ]; then
    echo "Checking/Installing Python dependencies..."
    pip install -r requirements.txt --quiet
fi

# 4. Start the Bot
echo "--- Launching Bot ---"
python3 -m anony
