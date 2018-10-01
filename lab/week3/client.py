"""
Networks Lab 3: UDP Socket Programming

Client code.

By:
Clemence Goh (1002075)
Cheryl Goh (1002421)
"""

import socket as S
import argparse
import json
import time


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


def clientSide(_rate=None):
    rate = commandLineArgs(_rate)
    host_name = "localhost"
    port_number = 5555

    _missing_numbers = [1650]  # after 1.65 Mbps, start dropping

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
            message = createPayload(
                "This is a message from the client",
                i)

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


if __name__ == "__main__":
    clientSide(_rate=2.0)

