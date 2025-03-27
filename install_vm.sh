#!/bin/bash

echo "🔥 Installing PacketReaper in a Virtual Machine... 🔥"

# Check if running inside a VM
if [[ $(dmidecode -s system-product-name) == *"VirtualBox"* ]]; then
    echo "✅ Detected VirtualBox VM"
elif [[ $(dmidecode -s system-product-name) == *"VMware"* ]]; then
    echo "✅ Detected VMware VM"
elif [[ $(dmidecode -s system-product-name) == *"Parallels"* ]]; then
    echo "✅ Detected Parallels VM"
else
    echo "⚠️ Warning: Could not detect VM type! Proceeding anyway..."
fi

# Update package lists
sudo apt update -y && sudo apt upgrade -y

# Install required dependencies
sudo apt install -y python3 python3-pip aircrack-ng tshark net-tools usbutils

# Ensure the user has the correct permissions for Wireshark
sudo usermod -aG wireshark $USER

# Install required Python packages
pip3 install -r requirements.txt

echo "✅ Installation complete!"
echo "⚠️ Remember: VMs CANNOT use internal Wi-Fi adapters for packet injection."
echo "🔌 You MUST use an external USB Wi-Fi adapter (e.g., Alfa AWUS036NHA)!"
echo "Run PacketReaper with: python3 packetreaper.py --mode sniff"
