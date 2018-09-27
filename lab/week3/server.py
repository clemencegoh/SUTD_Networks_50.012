"""
Networks Lab 3: UDP Socket Programming

Server code.
"""

import socket as S
import json


def serverSide():
    sock = S.socket(S.AF_INET, S.SOCK_DGRAM)
    sock.bind(('localhost', 5555))

    serverCounter = -1

    while True:
        serverCounter += 1
        data, addrs = sock.recvfrom(4096)
        data = json.loads(data.decode())

        if serverCounter != data["ID"]:
            print("WARNING: ID {} not received\n\n".format(serverCounter))
            # skip count
            serverCounter += 1

        # debugger
        print("Payload: {} \nID: {} \nAddresses: {} \n\n".
              format(data["Payload"], data["ID"], addrs))




if __name__=="__main__":
    serverSide()
