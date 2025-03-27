#!/bin/bash

echo "🔥 Installing PacketReaper on Linux... 🔥"

# Update package lists
sudo apt update -y && sudo apt upgrade -y

# Install required dependencies
sudo apt install -y python3 python3-pip aircrack-ng tshark net-tools

# Ensure the user has the correct permissions for Wireshark
sudo usermod -aG wireshark $USER

# Install required Python packages
pip3 install -r requirements.txt

echo "✅ Installation complete! Run PacketReaper with:"
echo "python3 packetreaper.py --mode sniff"
