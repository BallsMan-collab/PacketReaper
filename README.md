
# 💀 PacketReaper - The Ultimate Wi-Fi Pentesting Tool 🏴‍☠️  
**By ballsman-collab/TomatosCanHack (I go by both)**
🚀 **PacketReaper** is a powerful **Wi-Fi pentesting tool** for **Windows, Linux, macOS (Intel & Apple Silicon M1/M2/M3/M4), and Virtual Machines (VMware, VirtualBox, UTM)**. It allows ethical hackers to **analyze, capture, and crack** Wi-Fi networks.  

⚠️ **Disclaimer:** This tool is for **educational & security research purposes only**. **Do not use it on unauthorized networks!**  

---

## **🛠 Features**  
✅ **Monitor Mode Check** – Detects if your adapter supports monitor mode & packet injection 🔍  
✅ **Packet Sniffing** – Capture and analyze Wi-Fi packets in real-time 📡  
✅ **Handshake Capture** – Extract WPA2 handshakes for cracking 🔓  
✅ **Cracking Module** – Use wordlists to break WPA2 passwords 🚀  
✅ **Windows, Linux, macOS, VirtualBox, VMware & UTM (M1/M2/M3/M4) Support** 🎯  

---

## **📥 Installation**  

### **🖥️ Windows Setup**
💡 **Windows requires Npcap and Wireshark to work!**  
1️⃣ **Download & Install Dependencies:**  
   - Install **Npcap**: [https://nmap.org/npcap/](https://nmap.org/npcap/)  
   - Install **Wireshark**: [https://www.wireshark.org/](https://www.wireshark.org/)  

2️⃣ **Clone the repo and install dependencies:**  
\`\`\`powershell
git clone https://github.com/YourUsername/PacketReaper.git
cd PacketReaper
install_windows.bat
\`\`\`

3️⃣ **Run PacketReaper on Windows:**  
\`\`\`powershell
python packetreaper.py --mode sniff
\`\`\`

---

### **🐧 Linux Setup (Kali/ParrotOS/Ubuntu)**
\`\`\`bash
git clone https://github.com/YourUsername/PacketReaper.git
cd PacketReaper
chmod +x install_linux.sh
./install_linux.sh
python3 packetreaper.py --mode sniff
\`\`\`

---

### **🍏 macOS Setup (Intel & Apple Silicon)**
\`\`\`bash
brew install python3 wireshark aircrack-ng
git clone https://github.com/YourUsername/PacketReaper.git
cd PacketReaper
pip3 install -r requirements.txt
python3 packetreaper.py --mode sniff
\`\`\`

---

### **💻 Running in a Virtual Machine (VirtualBox, VMware, UTM M1/M2/M3/M4)**
🛑 **IMPORTANT:** Virtual machines **CANNOT** use built-in Wi-Fi adapters for packet injection. You **must** use an external USB Wi-Fi adapter (e.g., **Alfa AWUS036NHA**).  

**1️⃣ Connect your USB Wi-Fi adapter to the VM:**  
👉 **For VirtualBox:**  
- Go to **Devices > USB > Select your Wi-Fi Adapter**  
- Enable **USB 3.0** in VM settings  

👉 **For VMware:**  
- Go to **VM > Removable Devices > Select your Wi-Fi Adapter > Connect**  

👉 **For UTM (Apple Silicon M1/M2/M3/M4)**  
- Go to **VM Settings > USB Devices > Add USB Wi-Fi Adapter**  

**2️⃣ Install dependencies inside your VM:**  
\`\`\`bash
git clone https://github.com/YourUsername/PacketReaper.git
cd PacketReaper
chmod +x install_vm.sh
./install_vm.sh
\`\`\`

**3️⃣ Run PacketReaper inside the VM:**  
\`\`\`bash
python3 packetreaper.py --mode sniff
\`\`\`

---

## **🛠 New `install_windows.bat` for Windows Support**
🔥 **Create a file named `install_windows.bat` and paste this:**  
\`\`\`bat
@echo off
echo Installing PacketReaper dependencies...
pip install -r requirements.txt
echo Installation complete! Run 'python packetreaper.py --mode sniff'
\`\`\`

---

## **🚀 Usage Examples**  
📡 **Start sniffing packets:**  
\`\`\`bash
python packetreaper.py --mode sniff
\`\`\`
🔓 **Capture a WPA2 handshake:**  
\`\`\`bash
python packetreaper.py --mode capture --bssid AA:BB:CC:DD:EE:FF --channel 6
\`\`\`
💀 **Crack a handshake with a wordlist:**  
\`\`\`bash
python packetreaper.py --mode crack --file handshake.cap --wordlist rockyou.txt
\`\`\`

---

## **🔓 License**  
MIT License – Free to modify, contribute, and improve!  

---

### **💀 What’s New in This Update?**
✅ **Added Full Windows Support!**  
✅ **New `install_windows.bat` for easy Windows installation**  
✅ **New setup instructions for Windows**  
✅ **Updated README for macOS (Intel & M1/M2/M3/M4), Linux, and VMs**  

🔥 **Now your repo supports everything: Windows, macOS, Linux, VMware, VirtualBox & Apple Silicon (M1/M2/M3/M4)!** 🚀😈  

---

### **💀 Ready to Reap Some Packets? Start Now! 🚀**  

