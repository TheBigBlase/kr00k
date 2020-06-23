import socket
import sys
from time import sleep


def generateTraffic(port, ip, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # genereate UDP traffic 
    print("Sending ", payload, " to ip ", ip + " using port ", port)
    while True:
        try:
            sock.sendto(bytes(payload, "utf-8"), (ip, port))
            sleep(.1)
        except OSError:
            print("deauth")
        except KeyboardInterrupt:
            print("Goodbye ! ")
            return 0
        except:
            print("error", sys.exec_info())

def main():
    port = 53
    ip = "8.8.8.8"
    payload = "woaw such packet much wow" * 60 
    generateTraffic(port, ip, payload)


if __name__ == "__main__":
    main()
