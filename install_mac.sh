#!/bin/bash

echo "🔥 Installing PacketReaper on macOS... 🔥"

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "⚠️ Homebrew not found! Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew is already installed!"
fi

# Update Homebrew and install dependencies
brew update && brew upgrade
brew install python3 wireshark aircrack-ng

# Install required Python packages
pip3 install -r requirements.txt

echo "✅ Installation complete! Run PacketReaper with:"
echo "python3 packetreaper.py --mode sniff"
