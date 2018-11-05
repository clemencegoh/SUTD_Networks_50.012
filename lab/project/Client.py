
# coding: utf-8

import socket
import config
from Encryption import RsaKey, AesKey



v = socket.socket()

ownKeys = RsaKey()

VPN = (config.VPNHost,config.VPNPort)
v.connect(VPN)

# Exchange VPN server's key
print('Exchanging public key with VPN')
v.send(b'Exchange Public Key')
vpnRsaKey = RsaKey(v.recv(1024))
v.send(ownKeys.getPublicKey())
vpnAesKey = AesKey(ownKeys.decrypt(v.recv(1024)))
v.close()
# Client now has VPN's RSA and AES keys, VPN's RSA will no longer be used

# Get Remote server's key
print('Exchanging public key with remote')
msg = vpnAesKey.encrypt(bytes('%s/%d/%s'%(config.serverHost,config.serverPort,"Exchange Public Key"),'utf-8'))
v = socket.socket()
v.connect(VPN)
v.send(msg)
remAesKey = AesKey(ownKeys.decrypt(v.recv(1024)))
v.close()
# Client now has Remote's AES Key and can communicate securely with it

# Send request to remote
msg = "This is a message to the remote"
print("Sending '%s' to remote"%(msg))
v = socket.socket()
v.connect(VPN)
ownHost, ownPort = v.getsockname()
msg = remAesKey.encrypt(bytes(msg,'utf-8')).decode("utf-8")
msg = vpnAesKey.encrypt(bytes('{}/{}/{}'.format(config.serverHost,config.serverPort,msg),'utf-8'))
v.send(msg)
v.close()

# Listen for remote's reply
print("Awaiting remote's reply at {} Port {}".format(config.clientHost,ownPort))
v = socket.socket()
v.bind((config.clientHost,ownPort))
v.listen(1)
c, addr = v.accept()

decoded_list = vpnAesKey.decrypt(c.recv(1024)).decode("utf-8").split("/")
msg = bytes("/".join(decoded_list[2:]),'utf-8')
msg = remAesKey.decrypt(msg).decode('utf-8')
print("Received '{}' from remote".format(msg))

v.close()





