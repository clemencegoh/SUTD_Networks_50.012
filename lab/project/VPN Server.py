
# coding: utf-8

import socket
import config
from Encryption import RsaKey, AesKey


s = socket.socket()
s.bind((config.VPNHost,config.VPNPort))
s.listen(5)

VPNKeys = RsaKey()
IpToRsaDic = {}
IpToAesDic = {}

connCount = 0

while True:
    c, addr = s.accept()
    if config.isTest:
        addr = (config.VPNTESTCONNECTION[connCount], addr[1])
        connCount+=1
        connCount%=len(config.VPNTESTCONNECTION)
    
    print ("Connection from: "+str(addr))
    msg = c.recv(1024)
    
    
    if msg==b'Exchange Public Key':
        print("Exchanging keys with client")
        # Server sends the public key certificate to client
        c.send(VPNKeys.getPublicKey())
        
        # Records client key state
        IpToRsaDic[addr[0]] = RsaKey(c.recv(1024))
        
        # Generates symmetric Key, Encrypt with client's RSA key, and send to client
        IpToAesDic[addr[0]] = AesKey()
        msg = IpToAesDic[addr[0]].getKey()
        msg = IpToRsaDic[addr[0]].encrypt(msg)
        c.send(msg)
        
    else:
        # Server receives remote server's information
        decoded_list = IpToAesDic[addr[0]].decrypt(msg).decode("utf-8")
        msgLen = len(decoded_list)
        decoded_list = decoded_list.split("/")
        remHost = decoded_list[0]
        remPort = decoded_list[1]
        payload = "/".join(decoded_list[2:])
        remPort = int(remPort)
        
        # Server connects to remote server
        print("Connecting to: {} Port {}".format(remHost,remPort))
        r = socket.socket()
        r.connect((remHost,remPort))
        
        # If payload requests remote key, get remote's public cert to client and client to remote
        if payload=="Exchange Public Key":
            print("Exchanging keys between client and remote")
            
            # Since the payload was decrypted, the client's state must have been recorded in absence of timeout
            clientKeys = IpToRsaDic[addr[0]]
            
            # Request public key exchange
            r.send(b'Exchange Public Key')
            remKeys = RsaKey(r.recv(1024))
            
            # Send VPN encrypted AES key to remote
            IpToAesDic[remHost] = AesKey()
            r.send(remKeys.encrypt(IpToAesDic[remHost].getKey()))
            
            # Wait for ACK
            if (r.recv(1024)!=b"1"):
                r.close()
                c.close()
                continue
            
            # Send encrypted client IP & unencrypted RSA key to remote server
            r.send(IpToAesDic[remHost].encrypt(bytes(addr[0],'utf-8')))
            if (r.recv(1024)!=b"1"):
                r.close()
                c.close()
                continue
            r.send(clientKeys.getPublicKey())
            
            # Send remote server's AES key to client
            msg = r.recv(1024)
            c.send(msg)
        else:
            print("Forwarding information")
            # Add encapsulation for sender address
            payload = "{}/{}/{}".format(addr[0],addr[1],payload)
            payload = IpToAesDic[remHost].encrypt(bytes(payload,'utf-8'))
            
            # Send encrypted information
            r.send(payload)
        
        # Close remote server connection
        r.close()
    c.close()
"""
NOTE
Switch architecture to remote access VPN
Encryption only between host and VPN server
Remote server becomes intranet
"""






