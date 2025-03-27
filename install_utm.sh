#!/bin/bash

echo "🔥 Installing PacketReaper in UTM (M1/M2/M3/M4 Macs)... 🔥"

# Check if running inside UTM
if [[ $(system_profiler SPHardwareDataType | grep "Processor Name") == *"Apple"* ]]; then
    echo "✅ Detected Apple Silicon (M1/M2/M3/M4) running UTM"
else
    echo "⚠️ Warning: Could not confirm UTM environment! Proceeding anyway..."
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
echo "⚠️ REMINDER: UTM CANNOT use internal Mac Wi-Fi for packet injection."
echo "🔌 You MUST use an external USB Wi-Fi adapter (e.g., Alfa AWUS036NHA)!"
echo "Run PacketReaper with: python3 packetreaper.py --mode sniff"
