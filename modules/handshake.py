# modules/handshake.py

import subprocess
import time
import os

def capture_handshake(interface, bssid, channel, output_prefix="handshake"):
    """
    Captures the WPA/WPA2 handshake using airodump-ng.

    Args:
        interface (str): The name of the monitor mode enabled Wi-Fi interface.
        bssid (str): The BSSID of the target network.
        channel (str): The channel the target network is operating on.
        output_prefix (str, optional): The prefix for the output files.
                                       Defaults to "handshake".
    """
    print(f"[*] Starting handshake capture on interface {interface} for BSSID {bssid} (Channel {channel})...")
    output_file = output_prefix  # airodump-ng will append .cap, .csv, etc.

    command = [
        "airodump-ng",
        "--bssid",
        bssid,
        "--channel",
        str(channel),
        "--write",
        output_file,
        interface
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("[*] Airodump-ng is running. Press Ctrl+C to stop the capture manually.")

        # Keep the script running until Ctrl+C is pressed or a handshake is captured
        while True:
            time.sleep(5)  # Check for the .cap file every 5 seconds
            cap_file_path = f"{output_file}-01.cap"
            if os.path.exists(cap_file_path) and os.path.getsize(cap_file_path) > 0:
                print(f"[+] Handshake captured and saved to: {cap_file_path}")
                process.terminate()  # Stop airodump-ng
                break
            if process.poll() is not None:
                print("[-] Airodump-ng exited unexpectedly.")
                break

    except FileNotFoundError:
        print("[!] Error: airodump-ng not found. Please ensure it is installed and in your system's PATH.")
    except Exception as e:
        print(f"[!] An unexpected error occurred during handshake capture: {e}")
    finally:
        if 'process' in locals() and process.poll() is None:
            process.terminate() # Ensure airodump-ng is stopped if the script exits

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    capture_interface = input("Enter the monitor mode Wi-Fi interface (e.g., wlan0mon): ")
    target_bssid = input("Enter the BSSID of the target network: ")
    target_channel = input("Enter the channel of the target network: ")
    capture_handshake(capture_interface, target_bssid, target_channel)
