
# coding: utf-8

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP,AES
from Crypto import Random
# pip install PyCryptodome necessary as PyCrypto is no longer maintained
import ast
import base64


# Class to handle encryption/decryption
class RsaKey:
    def __init__(self, publicKey=None, length=2048):
        if publicKey!=None:
            self.__hasPrivateKey = False
            self.__publicKey = RSA.importKey(publicKey, passphrase=None)
        else:
            self.__hasPrivateKey = True
            self.__key = RSA.generate(length)
            self.__publicKey = self.__key.publickey()
    
    # Returns byte key for transmission
    def getPublicKey(self):
        return self.__publicKey.exportKey(format='PEM', passphrase=None, pkcs=1)
    
    # Encrypts byte message using public key
    def encrypt(self,msg):
        return PKCS1_OAEP.new(self.__publicKey).encrypt(msg)
        
    # Decrypts byte message using private key
    def decrypt(self,encrypted):
        if self.__hasPrivateKey:
            return PKCS1_OAEP.new(self.__key).decrypt(ast.literal_eval(str(encrypted)))

class AesKey:
    def __init__(self,key=None,length=32):
        if key!=None:
            if type(key) != bytes:
                key = bytes(key,'utf-8')
            self.__key = key
        else:
            self.__key = Random.new().read(length)
            
    # Returns byte key for transmission
    def getKey(self):
        return self.__key
    
    # Encrypts message, outputs initialization vector and encrypted message
    def encrypt(self,msg):
        if type(msg)==str:
            msg = bytes(msg,'utf-8')
        
        msg = self.__pad(msg)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(msg))
    
    def decrypt(self,encrypted):
        encrypted = base64.b64decode(encrypted)
        iv = encrypted[:AES.block_size]
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(encrypted[AES.block_size:]))

    def __pad(self, s):
        return s + bytes((AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size),'utf-8')
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    
    
    
    
    
    
    
    
    
    
    
    
    
    

