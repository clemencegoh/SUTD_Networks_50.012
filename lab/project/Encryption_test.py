import unittest
import Encryption as e


class TestEncryption(unittest.TestCase):
    def testRSA(self):
        # RSA Demonstration
        # Generate new key pair
        ks1 = e.RsaKey()  # class object
        publicKey = ks1.getPublicKey()

        # Generate keys using exising public key
        ks2 = e.RsaKey(publicKey)

        message_byte = b"RSA Test message"

        # Encryption
        msg = ks2.encrypt(message_byte)

        # Decryption
        msg = ks1.decrypt(msg)
        self.assertEqual(msg, message_byte, "TestRSA: Message different")

    def testAES(self):
        # AES Demonstration
        # Generate new keys
        ks3 = e.AesKey()
        key = ks3.getKey()

        # Generate key from exising symmetric key
        ks4 = e.AesKey(key)

        message_byte = b"AES Test message"

        # Encryption
        msg = ks3.encrypt(message_byte)

        # Decryption
        msg = ks4.decrypt(msg)
        self.assertEqual(msg, message_byte, "TestAES: message different")


if __name__ == "__main__":
    unittest.main()