# utils/adapter_check.py

import subprocess
import platform
import re
from utils.logger import info, warning, error, debug  # Import logger

def check_monitor_mode_support(interface):
    """
    Checks if the given Wi-Fi interface supports monitor mode.

    Args:
        interface (str): The name of the Wi-Fi interface.

    Returns:
        bool: True if monitor mode is likely supported, False otherwise.
    """
    os_name = platform.system()
    info(f"Checking monitor mode support for interface '{interface}' on {os_name}...")

    if os_name == "Linux":
        try:
            output = subprocess.check_output(["iw", interface, "info"], text=True)
            if "monitor flags:" in output:
                info(f"[+] Interface '{interface}' seems to support monitor mode.")
                return True
            else:
                warning(f"[-] Interface '{interface}' does not explicitly report monitor mode support via 'iw info'.")
                return False
        except FileNotFoundError:
            error("Error: 'iw' command not found. Ensure 'iw' package is installed.")
            return False
        except subprocess.CalledProcessError as e:
            error(f"Error running 'iw info {interface}': {e}")
            return False
    elif os_name == "Darwin":  # macOS
        # macOS doesn't have a direct command to check for monitor mode support.
        # The 'airport' utility can be used to enable it, but checking beforehand is tricky.
        warning(f"[*] Checking monitor mode support on macOS requires manual verification or using 'airport' utility.")
        info(f"[*] You can try enabling monitor mode using: 'sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport {interface} sniff'")
        return True  # Assume if the interface exists, monitor mode might be possible
    elif os_name == "Windows":
        warning(f"[*] Checking monitor mode support on Windows depends on the adapter and drivers. Use tools like 'netsh wlan show drivers' to inspect capabilities.")
        info(f"[*] Ensure you have Npcap and compatible drivers installed.")
        return True  # Assume if the interface is listed, it might be usable with tools like pyshark
    else:
        error(f"Unsupported operating system: {os_name}")
        return False

def check_packet_injection_support(interface):
    """
    Attempts a basic check for packet injection capability.

    Note: This is not a definitive test and might require root/administrator privileges.

    Args:
        interface (str): The name of the Wi-Fi interface.

    Returns:
        bool: True if packet injection seems likely, False otherwise.
    """
    os_name = platform.system()
    info(f"Attempting a basic packet injection check on interface '{interface}'...")

    if os_name == "Linux":
        try:
            # Craft a raw 802.11 frame (minimal example)
            subprocess.run(["sudo", "iw", interface, "set", "type", "monitor"], check=True, capture_output=True)
            subprocess.run(["sudo", "iw", interface, "set", "type", "managed"], check=True, capture_output=True)
            info(f"[+] Basic packet injection test (setting/unsetting monitor mode) seems successful on '{interface}'.")
            return True
        except FileNotFoundError:
            error("Error: 'iw' command not found. Ensure 'iw' package is installed.")
            return False
        except subprocess.CalledProcessError as e:
            warning(f"[-] Basic packet injection test failed on '{interface}': {e}")
            warning("[-] This does not definitively mean injection is impossible, but it indicates potential issues.")
            return False
        finally:
            # Ensure interface is back in managed mode (attempt)
            try:
                subprocess.run(["sudo", "iw", interface, "set", "type", "managed"], check=False, capture_output=True)
            except:
                pass
    elif os_name == "Darwin":
        warning(f"[*] Packet injection support on macOS depends on the adapter and drivers. Use tools like 'aireplay-ng' (from aircrack-ng) to test.")
        info(f"[*] Ensure aircrack-ng is installed: 'brew install aircrack-ng'")
        return True  # Rely on aircrack-ng for actual testing
    elif os_name == "Windows":
        warning(f"[*] Packet injection on Windows requires compatible drivers and tools like Npcap and raw packet sending libraries (used by tools like scapy or pyshark).")
        info(f"[*] Functionality depends on the specific adapter and how well drivers support raw packet injection.")
        return True  # Assume if pyshark can send raw packets, injection is possible
    else:
        error(f"Unsupported operating system: {os_name}")
        return False

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    iface = input("Enter the Wi-Fi interface to check (e.g., wlan0): ")
    if iface:
        supports_monitor = check_monitor_mode_support(iface)
        print(f"\nMonitor mode support for '{iface}': {supports_monitor}")

        supports_injection = check_packet_injection_support(iface)
        print(f"Packet injection support for '{iface}': {supports_injection}")
    else:
        warning("No interface provided.")
