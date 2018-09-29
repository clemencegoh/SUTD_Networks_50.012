"""
Networks Lab 3: UDP Socket Programming

Server code.
"""

import socket as S
import json


def serverSide():
    sock = S.socket(S.AF_INET, S.SOCK_DGRAM)
    sock.bind(('localhost', 5555))

    # sever side counting of objects
    serverCounter = -1
    missed_data = []

    while True:
        serverCounter += 1
        data, addrs = sock.recvfrom(4096)
        data = json.loads(data.decode())

        if data["Payload"] == "End":
            break

        if serverCounter != data["ID"]:
            # print("WARNING: ID {} not received\n\n".format(serverCounter))
            missed_data.append("ID: {}".format(serverCounter))

            # skip count
            serverCounter += 1

        # debugger
        # print("Payload: {} \nID: {} \nAddresses: {} \n\n".
        #       format(data["Payload"], data["ID"], addrs))

    print("--------- Report ---------")
    print("Total expected:", data["ID"])
    if missed_data:
        print("! WARNING !")
        print("Data missed:", str(missed_data))
        print("! WARNING !")
    print("------- End Report -------")




if __name__=="__main__":
    serverSide()
