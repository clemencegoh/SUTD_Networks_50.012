
# coding: utf-8

import socket
import config
from Encryption import RsaKey, AesKey


s = socket.socket()
s.bind((config.serverHost,config.serverPort))

msg = ""
remKeys = RsaKey()
IpToAesDic = {}

# Listen for connection
while True:
    s.listen(1)
    c, addr = s.accept()
    if config.isTest:
        addr = (config.VPNHost, addr[1])
    print ("Connection from: " + str(addr))
    msg = c.recv(1024)
    if msg == b'Exchange Public Key':
        print('Exchanging public keys')
        # Send own public key to VPN
        c.send(remKeys.getPublicKey())
        
        # Get VPN AES key
        IpToAesDic[addr[0]] = AesKey(remKeys.decrypt(c.recv(1024)))
        c.send(b"1")
        
        # Get encrypted remote host address
        hostAddr = IpToAesDic[addr[0]].decrypt(c.recv(1024)).decode("utf-8")
        c.send(b"1")
        
        # Get remote host's public key
        hostRsaKey = RsaKey(c.recv(1024))
        
        # Send Remote's AES Key, encrypted with client's RSA public key
        IpToAesDic[hostAddr] = AesKey()
        msg = hostRsaKey.encrypt(IpToAesDic[hostAddr].getKey())
        c.send(msg)
        
    else:
        # Decrypts with VPN's AES to get client identity, then decrypt with client's AES
        decoded_list = IpToAesDic[addr[0]].decrypt(msg).decode("utf-8")
        decoded_list = decoded_list.split("/")
        clientHost = decoded_list[0]
        clientPort = decoded_list[1]
        msg = "/".join(decoded_list[2:])
        clientPort = int(clientPort)
        msg = bytes(msg,'utf-8')
        msg = IpToAesDic[clientHost].decrypt(msg).decode("utf-8")
        
        # Handles message, e.g. by routing unencrypted payload to internal network and getting reply
        print("Handling message {} from remote client".format(msg))
        pass
        
        # Sends reply to client
        msg = "This is a message to the client"
        print("Sending the reply '{}' to remote client".format(msg))
        msg = IpToAesDic[clientHost].encrypt(bytes(msg,'utf-8')).decode("utf-8")
        msg = IpToAesDic[addr[0]].encrypt('{}/{}/{}'.format(clientHost,clientPort,msg))
        
        VPN = (config.VPNHost,config.VPNPort)
        v = socket.socket()
        v.connect(VPN)
        v.send(msg)
        v.close()
    c.close()
    

