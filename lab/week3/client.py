"""
Networks Lab 3: UDP Socket Programming

Client code.
"""

import socket as S
import argparse
import json
import random

def generateRandomString(_length):
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numString = "1234567890"
    allPossible = alphaLower + alphaUpper + numString

    toReturn = ""
    for i in range(_length):
        toReturn += random.choice(allPossible)
    return toReturn

def commandLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', type=float, dest='rate',
        help='Packet rate in Mbps (eg; -r 1.5 is 1.5 Mbps)')

    args = parser.parse_args()
    rate = 3.0

    if args.rate == None:
        # print("USAGE:")
        # print("python2 client.py -r 3.0:")
        print("using default {} Mbps...".format(rate))
        return rate
    else:
        print("Client rate is {} Mbps.".format(args.rate))
        return args.rate


def createPayload(_message, _ID):
    return {
        "ID": _ID,
        "Payload": _message,
    }


def clientSide():
    rate = commandLineArgs()
    host_name = "localhost"
    port_number = 5555

    sock = S.socket(S.AF_INET, S.SOCK_DGRAM)
    server_address = (host_name, port_number)

    for i in range(100):
        if i != 12:
            message = createPayload(generateRandomString(12), i)

            print("Sent with Payload: {} \nID: {}".format(message, message["ID"]))
            sent = sock.sendto(json.dumps(message).encode(), server_address)


if __name__=="__main__":
    clientSide()

