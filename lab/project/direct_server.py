import socket
from Encryption import RsaKey, AesKey
import config
import time



s = socket.socket()
s.bind((config.serverHost,config.serverPort))

remKeys = RsaKey()
IpToAesDic = {}

while True:
    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    starttime = time.time()
    msg = c.recv(1024)
    print("Received msg", str(msg))
    endtime = time.time()
    print("Direct time taken:", endtime - starttime)
