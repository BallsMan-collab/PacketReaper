# modules/monitor_check.py

import subprocess
import sys

def check_monitor_mode_support(interface):
    """
    Checks if the specified Wi-Fi interface supports monitor mode on Linux/macOS.

    Args:
        interface (str): The name of the network interface.

    Returns:
        bool: True if monitor mode is likely supported, False otherwise.
    """
    if sys.platform.startswith("linux"):
        try:
            # Use iw to get interface info
            output = subprocess.check_output(["iw", interface, "info"], text=True)
            if "monitor flags: RX_MONITOR" in output:
                print(f"[+] Interface {interface} appears to support monitor mode.")
                return True
            else:
                print(f"[-] Interface {interface} does not explicitly report monitor mode support (iw info).")
                return False
        except FileNotFoundError:
            print("[!] Error: 'iw' command not found. Please ensure it is installed (usually part of wireless-tools).")
            return False
        except subprocess.CalledProcessError:
            print(f"[!] Error: Could not get information for interface {interface} using 'iw'.")
            return False
    elif sys.platform == "darwin":
        try:
            # Use airport utility (macOS specific) - might require enabling
            output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", interface, "sniff", "1"], text=True, stderr=subprocess.PIPE)
            if "en0: Sniffing" in output or "en1: Sniffing" in output: # Common Wi-Fi interfaces
                print(f"[+] Interface {interface} appears capable of entering monitor mode (airport sniff).")
                return True
            else:
                print(f"[-] Interface {interface} does not seem to enter monitor mode using airport sniff.")
                return False
        except FileNotFoundError:
            print("[!] Error: 'airport' utility not found.")
            return False
        except subprocess.CalledProcessError as e:
            # airport sniff 1 often exits with an error code even if it starts sniffing
            if "exit status 1" in str(e):
                print(f"[+] Interface {interface} appears capable of entering monitor mode (airport sniff - exited with status 1).")
                return True
            else:
                print(f"[!] Error using airport utility: {e.stderr}")
                return False
    elif sys.platform.startswith("win"):
        print("[*] Monitor mode detection on Windows is different. Ensure your adapter and drivers support it.")
        return True # Assume the user knows if their adapter supports it on Windows
    else:
        print(f"[!] Unsupported operating system: {sys.platform}")
        return False

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    check_interface = input("Enter the Wi-Fi interface to check (e.g., wlan0 on Linux, en0 on macOS): ")
    supports_monitor = check_monitor_mode_support(check_interface)
    print(f"[*] Monitor mode support for {check_interface}: {supports_monitor}")
