import argparse
import subprocess
import pyshark
import re
import sys
import platform  # Import the platform module

# 🔥 ASCII BANNER - NOT ANONYMOUS
BANNER = r"""
888b    888          888                d8888                                                                              
8888b   888          888               d88888                                                                              
88888b  888          888              d88P888                                                                              
888Y88b 888  .d88b.  888888          d88P 888 88888b.   .d88b.  88888b.  888  888 88888b.d88b.   .d88b.  888  888 .d8888b  
888 Y88b888 d88""88b 888            d88P  888 888 "88b d88""88b 888 "88b 888  888 888 "888 "88b d88""88b 888  888 88K      
888  Y88888 888  888 888           d88P   888 888  888 888  888 888  888 888  888 888  888  888 888  888 888  888 "Y8888b. 
888   Y8888 Y88..88P Y88b.        d8888888888 888  888 Y88..88P 888  888 Y88b 888 888  888  888 Y88..88P Y88b 888      X88 
888    Y888  "Y88P"   "Y888      d88P     888 888  888  "Y88P"  888  888  "Y88888 888  888  888  "Y88P"   "Y88888  88888P' 
                                                                              888                                          
                                                                         Y8b d88P                                          
                                                                          "Y88P"                                           
              The Ultimate Wi-Fi Pentesting Tool 
"""

def check_compatible_adapter():
    """Checks for a Wi-Fi adapter that supports monitor mode."""
    os_name = platform.system()
    if os_name == "Linux":
        try:
            output = subprocess.check_output(["airmon-ng"], text=True)
            if "monitor mode vif enabled for" in output:
                print("[+] Compatible Wi-Fi adapter found (monitor mode enabled).")
                return True
            elif "PHY" in output and "Interface" in output:
                adapters = []
                lines = output.strip().split('\n')[1:]  # Skip header
                for line in lines:
                    parts = [part.strip() for part in re.split(r'\s+', line) if part.strip()]
                    if len(parts) >= 2:
                        adapters.append(parts[1])
                if adapters:
                    print("[*] Found the following Wi-Fi interfaces:")
                    for adapter in adapters:
                        print(f"    - {adapter}")
                    print("[!] Please ensure one of these adapters supports monitor mode and packet injection.")
                    print("[!] You might need to manually enable monitor mode (e.g., using 'sudo airmon-ng start <interface>').")
                    return True
                else:
                    print("[!] No Wi-Fi interfaces found by airmon-ng.")
                    return False
            else:
                print("[!] Could not determine compatible Wi-Fi adapter using airmon-ng.")
                return False
        except FileNotFoundError:
            print("[!] Error: airmon-ng not found. Please ensure it is installed (part of the aircrack-ng suite).")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error running airmon-ng: {e}")
            return False
    elif os_name == "Darwin":  # macOS
        print("[*] Checking for monitor mode support on macOS requires manual verification or using tools like 'airport'.")
        print("[!] Ensure your Wi-Fi interface supports monitor mode.")
        return True  # Assume user knows
    elif os_name == "Windows":
        print("[*] Monitor mode support on Windows depends on the adapter and drivers. Ensure you have the necessary tools (Npcap, Wireshark).")
        return True  # Assume user knows
    else:
        print(f"[!] Unsupported operating system: {os_name}")
        return False

def sniff_packets(interface):
    """Sniffs Wi-Fi packets on a given interface."""
    os_name = platform.system()
    print(f"[*] Sniffing on {interface}... Press Ctrl+C to stop.")
    try:
        if os_name == "Windows":
            capture = pyshark.LiveCapture(interface=interface)
            for packet in capture.sniff_continuously():
                print(packet)
        elif os_name == "Linux" or os_name == "Darwin":
            # For Linux/macOS, you might prefer scapy for more control
            from scapy.all import sniff
            sniff(iface=interface, store=False, prn=lambda x: x.summary())
        else:
            print(f"[!] Sniffing not fully supported on {os_name} in this script version.")
    except KeyboardInterrupt:
        print("\n[*] Stopping sniffing.")
    except Exception as e:
        print(f"[!] Error during sniffing: {e}")

def capture_handshake(interface, bssid, channel, output_file):
    """Captures WPA2 handshake packets."""
    os_name = platform.system()
    print(f"[*] Capturing handshake for BSSID {bssid} on channel {channel}")
    try:
        if os_name == "Windows":
            cmd = f"airodump-ng.exe -c {channel} --bssid {bssid} -w {output_file} {interface}"
            subprocess.run(cmd, check=True)
        elif os_name == "Linux" or os_name == "Darwin":
            cmd = ["airodump-ng", "--channel", str(channel), "--bssid", bssid, "--write", output_file, interface]
            subprocess.run(cmd, check=True)
        else:
            print(f"[!] Handshake capture not fully supported on {os_name} in this script version.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during handshake capture: {e}")
    except FileNotFoundError:
        tool = "airodump-ng.exe" if os_name == "Windows" else "airodump-ng"
        print(f"[!] Error: {tool} not found. Ensure aircrack-ng suite is installed and in your PATH.")
        sys.exit(1)

def crack_handshake(cap_file, wordlist, bssid):
    """Attempts to crack WPA2 handshake using a wordlist."""
    os_name = platform.system()
    print("[*] Cracking handshake...")
    try:
        if os_name == "Windows":
            cmd = f"aircrack-ng.exe -w {wordlist} -b {bssid} {cap_file}"
            subprocess.run(cmd, check=True)
        elif os_name == "Linux" or os_name == "Darwin":
            cmd = ["aircrack-ng", "-w", wordlist, "-b", bssid, cap_file]
            subprocess.run(cmd, check=True)
        else:
            print(f"[!] Handshake cracking not fully supported on {os_name} in this script version.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during cracking: {e}")
    except FileNotFoundError:
        tool = "aircrack-ng.exe" if os_name == "Windows" else "aircrack-ng"
        print(f"[!] Error: {tool} not found. Ensure aircrack-ng suite is installed and in your PATH.")
        sys.exit(1)

if __name__ == "__main__":
    print(BANNER)  # Display the banner 

    if not check_compatible_adapter():
        print("[!] No compatible Wi-Fi adapter found. Exiting.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Wi-Fi Pentesting Tool for Windows, Linux, and macOS")
    parser.add_argument("-m", "--mode", choices=["sniff", "capture", "crack"], required=True, help="Mode of operation")
    parser.add_argument("-i", "--interface", help="Network interface (e.g., wlan0, en0, Wi-Fi)")
    parser.add_argument("-b", "--bssid", help="Target BSSID (for handshake capture/crack)")
    parser.add_argument("-c", "--channel", help="Wi-Fi Channel (for handshake capture)")
    parser.add_argument("-f", "--file", help="Handshake capture file (for cracking)")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist (for cracking)")

    args = parser.parse_args()

    if args.mode == "sniff":
        sniff_packets(args.interface)
    elif args.mode == "capture":
        if not args.interface or not args.bssid or not args.channel:
            print("[!] Interface, BSSID, and Channel are required for capture mode.")
            sys.exit(1)
        capture_handshake(args.interface, args.bssid, args.channel, "handshake")
    elif args.mode == "crack":
        if not args.file or not args.wordlist or not args.bssid:
            print("[!] Handshake file, wordlist, and BSSID are required for crack mode.")
            sys.exit(1)
        crack_handshake(args.file, args.wordlist, args.bssid)
