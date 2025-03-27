# 💀 PacketReaper - The Ultimate Wi-Fi Pentesting Tool 🏴‍☠️  

🚀 **PacketReaper** is a powerful **Wi-Fi pentesting tool** built for **Windows & Linux**, designed for ethical hackers to **analyze, capture, and crack** Wi-Fi networks. It automates key pentesting tasks like **packet sniffing, WPA2 handshake capture, and cracking** while ensuring ease of use.  

⚠️ **Disclaimer:** This tool is for **educational & security research purposes only**. **Do not use it on unauthorized networks!**  

---

## **🛠 Features**  
✅ **Monitor Mode Check** – Ensures your adapter supports monitor mode & packet injection 🔍  
✅ **Packet Sniffing** – Capture and analyze Wi-Fi packets in real-time 📡  
✅ **Handshake Capture** – Extract WPA2 handshakes for cracking 🔓  
✅ **Cracking Module** – Use wordlists to break WPA2 passwords 🚀  
✅ **Optimized for Windows & Linux** – Works on **Windows, Kali, ParrotOS, Ubuntu** 🎯  

---

## **📥 Installation**  

### **Windows Setup (Git Clone Method)**
1️⃣ Open PowerShell and run:  
   ```powershell
   git clone https://github.com/YourUsername/PacketReaper.git
   cd PacketReaper
   python -m venv venv  # (Optional) Create a virtual environment
   venv\Scripts\activate  # (Optional) Activate it
   pip install -r requirements.txt
   python packetreaper.py --mode sniff
Linux Setup (Kali/ParrotOS/Ubuntu)
1️⃣ Run in Terminal:

bash
Copy
Edit
git clone https://github.com/YourUsername/PacketReaper.git
cd PacketReaper
chmod +x install_linux.sh
./install_linux.sh
python3 packetreaper.py --mode sniff
🚀 Usage Examples
📡 Start sniffing packets

bash
Copy
Edit
python packetreaper.py --mode sniff
🔓 Capture a WPA2 handshake

bash
Copy
Edit
python packetreaper.py --mode capture --bssid AA:BB:CC:DD:EE:FF --channel 6
💀 Crack a handshake with a wordlist

bash
Copy
Edit
python packetreaper.py --mode crack --file handshake.cap --wordlist rockyou.txt
🔍 Screenshots
(Add screenshots of the tool in action here!)

💀 Requirements
🔹 USB Wi-Fi Adapter that Supports Monitor Mode & Injection (e.g., Alfa AWUS036NHA, TL-WN722N v1)
🔹 Python 3.x
🔹 Aircrack-ng
🔹 Pyshark

⚠️ Legal Disclaimer
This tool is intended for security research and ethical hacking purposes only. Do not use it on networks you do not own or have explicit permission to test.

🛑 By using this tool, you take full responsibility for your actions.

🛠️ To-Do & Future Features
✅ Deauthentication Attack Module
✅ Automatic Channel Hopping
✅ GUI Version (Maybe 😏)
✅ More Protocol Support (WPA3, etc.)

📜 License
🔓 Open-source under the MIT License – Modify, contribute, and improve!

🤝 Contribute
🔥 Pull requests & feature requests are welcome! Fork the repo and submit a PR if you want to improve PacketReaper!

