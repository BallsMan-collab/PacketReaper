# modules/sniff.py

from scapy.all import sniff, Dot11

def sniff_packets(interface):
    """
    Sniffs Wi-Fi packets on the specified interface.

    Args:
        interface (str): The name of the network interface to sniff on.
    """
    print(f"[*] Starting packet sniffing on interface: {interface}")

    def packet_handler(pkt):
        """
        Callback function to process each captured packet.
        For now, it just prints a summary of Dot11 packets.
        """
        if pkt.haslayer(Dot11):
            print(f"[+] Captured Dot11 Packet: {pkt.summary()}")
        # You can add more detailed processing here

    try:
        sniff(iface=interface, prn=packet_handler, store=False)
    except PermissionError:
        print(f"[!] Error: Permission denied to sniff on interface {interface}. Try running with sudo.")
    except Exception as e:
        print(f"[!] An error occurred during packet sniffing: {e}")

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    sniffer_interface = input("Enter the Wi-Fi interface to sniff on (e.g., wlan0mon): ")
    sniff_packets(sniffer_interface)
