# ✠ PacketReaper - The Ultimate Wi-Fi Pentesting Tool 🏴‍☠️
**By ballsman-collab / Not Anonymous**

## 🚀 About PacketReaper
PacketReaper is a powerful **Wi-Fi pentesting tool** for **Windows, Linux, macOS (Intel & Apple Silicon M1/M2/M3/M4), and Virtual Machines (VMware, VirtualBox, UTM)**. It allows ethical hackers to **analyze, capture, and crack** Wi-Fi networks.

> ⚠ **Disclaimer:** This tool is for **educational & security research purposes only**. **Do not use it on unauthorized networks!**

---
## 🛠 Features
- ✅ **Monitor Mode Check** – Detects if your adapter supports monitor mode & packet injection 🔍
- ✅ **Packet Sniffing** – Capture and analyze Wi-Fi packets in real-time 📱
- ✅ **Handshake Capture** – Extract WPA2 handshakes for cracking 🔒
- ✅ **Cracking Module** – Use wordlists to break WPA2 passwords 🚀
- ✅ **Cross-Platform Support** – Works on **Windows, Linux, macOS, VirtualBox, VMware & UTM** 🎯

---
## 💞 Installation
### 🖥️ Windows Setup
> **Windows requires Npcap and Wireshark to work!**

1. **Install Dependencies:**
   - [Npcap](https://nmap.org/npcap/)
   - [Wireshark](https://www.wireshark.org/)
2. **Clone the repository and install dependencies:**
   ```powershell
   git clone https://github.com/ballsman-collab/PacketReaper.git

   cd PacketReaper

   .\install_windows.bat
   ```
3. **Run PacketReaper:**
   ```powershell
   python packetreaper.py --mode sniff
   ```

---
### 🐙 Linux Setup (Kali/ParrotOS/Ubuntu)
```bash

git clone https://github.com/ballsman-collab/PacketReaper.git

cd PacketReaper

chmod +x install_linux.sh

./install_linux.sh

python3 packetreaper.py --mode sniff
```

---
### 🍏 macOS Setup (Intel & Apple Silicon)
```bash

brew install python3 wireshark aircrack-ng

git clone https://github.com/ballsman-collab/PacketReaper.git

cd PacketReaper

pip3 install -r requirements.txt

python3 packetreaper.py --mode sniff
```

---
## 💻 Running in a Virtual Machine (VirtualBox, VMware, UTM M1/M2/M3/M4)
> ⚠ **IMPORTANT: Virtual machines CANNOT use built-in Wi-Fi adapters for packet injection.** You must use an **external USB Wi-Fi adapter** (e.g., Alfa AWUS036NHA).

### 🌐 Connect your USB Wi-Fi adapter to the VM:
- **VirtualBox:**
  - Go to **Devices > USB > Select your Wi-Fi Adapter**
  - Enable **USB 3.0** in VM settings
- **VMware:**
  - Go to **VM > Removable Devices > Select your Wi-Fi Adapter > Connect**
- **UTM (Apple Silicon M1/M2/M3/M4):**
  - Go to **VM Settings > USB Devices > Add USB Wi-Fi Adapter**

### 🛠 Install dependencies inside your VM:
```bash

git clone https://github.com/ballsman-collab/PacketReaper.git

cd PacketReaper

chmod +x install_vm.sh

./install_vm.sh

python3 packetreaper.py --mode sniff
```

---
## 🛠️ Windows Batch Installer
Create a file named **install_windows.bat** and paste the following:
```batch

@echo off

echo Installing PacketReaper dependencies...

pip install -r requirements.txt

echo Installation complete! Run 'python packetreaper.py --mode sniff'
```

---
## 🚀 Usage Examples
### 📱 Start sniffing packets:
```bash
python packetreaper.py --mode sniff --interface <your_wifi_interface>
```
### 🔒 Capture a WPA2 handshake:
```bash
python packetreaper.py --mode capture --interface <your_wifi_interface> --bssid <target_bssid> --channel <channel_number>
```
### 🔐 Crack a handshake with a wordlist:
```bash
python packetreaper.py --mode crack --file <path_to_capture_file.cap> --wordlist <path_to_wordlist.txt> --bssid <target_bssid>
```
> **Note:** Replace `<...>` placeholders with your actual values (interface name, BSSID, channel, file paths, and wordlist path).

---
## 🔧 License
**MIT License** – Free to modify, contribute, and improve!

---
## 💀 What’s New in This Update?
- ✅ Added **Full Windows Support!**
- ✅ New **install_windows.bat** for easy Windows installation
- ✅ Updated README for **macOS (Intel & M1/M2/M3/M4), Linux, and VMs**
- 🔥 **Now supports everything**: **Windows, macOS, Linux, VMware, VirtualBox & Apple Silicon (M1/M2/M3/M4)!**

---
## 💀 Ready to Reap Some Packets? Start Now! 🚀

