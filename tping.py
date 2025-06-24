import socket
import time
import sys

# Color definitions
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def tcp_ping(host, port, count=100, timeout=100):
    print(f"Pinging {host} on TCP port {port} with {count} attempts:")

    for i in range(count):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        try:
            start = time.time()
            s.connect((host, port))
            end = time.time()
            duration = (end - start) * 1000
            print(f"{GREEN}Connected To: {host}:{port} - time={duration:.2f}ms{RESET}")
        except socket.timeout:
            print(f"{RED}Booted Offline AHAHAHA ({host}:{port}){RESET}")
        except Exception as e:
            print(f"{RED}Error connecting to {host}:{port} - {e}{RESET}")
        finally:
            s.close()
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    tcp_ping(host, port)
