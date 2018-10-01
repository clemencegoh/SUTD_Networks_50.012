"""
Networks Lab 3: UDP Socket Programming

Server code.

By:
Clemence Goh (1002075)
Cheryl Goh (1002421)
"""

import socket as S
import json


def getMissingNumbers(_all_data, _last_number):
    to_return = []
    for i in range(int(_last_number)):
        if i not in _all_data:
            to_return.append(i)
    return to_return


def serverSide():
    sock = S.socket(S.AF_INET, S.SOCK_DGRAM)
    sock.bind(('localhost', 5555))

    # sever side counting of objects
    serverCounter = -1
    all_data = {}

    while True:
        serverCounter += 1
        data, addrs = sock.recvfrom(4096)
        data = json.loads(data.decode())

        if data["Payload"] == "End":
            break

        all_data[data["ID"]] = 1

        # debugger
        # print("Payload: {} \nID: {} \nAddresses: {} \n\n".
        #       format(data["Payload"], data["ID"], addrs))

    missed_data = getMissingNumbers(all_data, data["ID"])

    print("--------- Report ---------")
    print("Total expected:", data["ID"])
    if missed_data:
        print("! WARNING !")
        print("Data missed:", str(missed_data))
        print("! WARNING !")
    print("------- End Report -------")




if __name__=="__main__":
    serverSide()
