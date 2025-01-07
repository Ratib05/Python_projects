# paramiko provides tools for ssh communication
import paramiko

# allows interaction with system-specific parameters and functions like command-line arguments.
import sys

# function that takes three arguments
def isolate_system(hostname, username, password):
    try:

        # Make a ssh client
        client = paramiko.SSHClient()

        # auto accept unknown host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # connects to remote system
        client.connect(hostname, username=username, password=password)

        # Execute a command on the remote system, the command disables the network interface
        stdin, stdout, stderr = client.exec_command("sudo ifconfig eth0 down")

        # reads and prints the output of the command
        print(stdout.read().decode())

        # reads and prints the error message of the command
        print(stderr.read().decode())

        # terminate the connection
        client.close()
        print(f"System {hostname} isolated successfully.")
    except Exception as e:
        print(f"Failed to isolate system {hostname}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python isolate_systems.py <hostname> <username> <password>")
        sys.exit(1)
    isolate_system(sys.argv[1], sys.argv[2], sys.argv[3])