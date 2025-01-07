# run shell commands from within python
import subprocess

# allows interaction with system-specific parameters and functions like command-line arguments.
import sys

def block_ip(ip_address):
    try: 
        
        # Runs the iptables command using subprocess.run() to block incoming traffic from the specified IP address.
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-S', ip_address, '-j', 'DROP'], check=True)
        print(f"IP address {ip_address} blocked successfully.")
   
   # Catches any errors raised by subprocess.run() when the iptables command fails.
    except subprocess.CalledProcessError as e:
        print(f"Failed to block IP addres {ip_address}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python block_ip.py <ip_address>")
        sys.exit(1)
    block_ip(sys.argv[1])