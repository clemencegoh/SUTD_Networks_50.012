"""
Networks Lab 3: UDP Socket Programming

Client code.
"""

import socket as S
import argparse
import json
import random
import time

def generateRandomString(_length):
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numString = "1234567890"
    allPossible = alphaLower + alphaUpper + numString

    toReturn = ""
    for i in range(_length):
        toReturn += random.choice(allPossible)
    return toReturn


def commandLineArgs(_rate):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-r', type=float, dest='rate',
    #     help='Packet rate in Mbps (eg; -r 1.5 is 1.5 Mbps)')

    # args = parser.parse_args()
    default_rate = 3.0

    if _rate == None:
        # print("USAGE:")
        # print("python2 client.py -r 3.0:")
        print("using default {} Mbps...".format(default_rate))
        return default_rate
    else:
        print("Client rate is {} Mbps.".format(_rate))
        return _rate


def createPayload(_message, _ID):
    return {
        "ID": _ID,
        "Payload": _message,
    }


def clientSide(_rate=None, _missing_numbers=[]):
    rate = commandLineArgs(_rate)
    host_name = "localhost"
    port_number = 5555

    sock = S.socket(S.AF_INET, S.SOCK_DGRAM)
    server_address = (host_name, port_number)

    # number of data to be sent
    max_number = int(rate * 1000)
    total_data = 0

    # timer
    start_time = time.time()

    # client-side counting
    for i in range(max_number):
        if i not in _missing_numbers:
            message = createPayload(generateRandomString(12), i)

            # print("Sent with Payload: {} \nID: {}".format(message, message["ID"]))
            total_data += sock.sendto(json.dumps(message).encode(), server_address)

    end_time = time.time()

    sock.sendto(json.dumps({"ID": max_number, "Payload": "End"}).encode(), server_address)

    # Report
    total_time_taken = end_time - start_time
    print("--------- Report ----------")
    print("Total bytes sent:", str(total_data))
    print("Total time taken:", str(total_time_taken))
    print("Final count:", max_number)
    print("------- End Report --------")





if __name__=="__main__":
    clientSide(_rate=1, _missing_numbers=[2, 6, 12])

