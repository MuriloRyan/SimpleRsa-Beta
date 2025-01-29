from SimpleRsa.ext.pembuilder.pembuilder import PemFormatPrivateKey, PemFormatPublicKey
from Crypto.Util.number import getPrime, inverse
import base64

class GenerateKeys:
    def __init__(self,p=None,q=None):
        self.p = None if not p else p
        self.q = None if not q else q

    def generate(self, prime_size=2048):
        p = self.p if isinstance(self.p,int) else getPrime(prime_size)
        q = self.q if isinstance(self.q,int) else getPrime(prime_size)
        n = p * q
        e = 65537
        phi_n = (p-1)*(q-1)
        d = inverse(e, phi_n)

        return n, e, d

class Encrypt:
    def __init__(self,n,e):
        self.n = n
        self.e = e

    def encrypt(self,message):
        messageBytes = message.encode()
        messageInt = int.from_bytes(messageBytes, "big")
        encrypted = pow(messageInt, self.e, self.n)
        return encrypted

class Decrypt():
    def __init__(self,n,d):
        self.n = n
        self.d = d
    
    def decrypt(self,c):
        cBytes = pow(c, self.d, self.n)
        decryptedBytes = cBytes.to_bytes((cBytes.bit_length() + 7) // 8, "big")
        decrypted = decryptedBytes.decode()
        return decrypted

class Rsa:
    def __init__(self,p=None,q=None,key_size=2048):
        self.KeyGenerator = GenerateKeys(p=p, q=q)
        self.n, self.e, self.d = self.KeyGenerator.generate(prime_size=key_size)
        self.Encryptor = Encrypt(self.n,self.e)
        self.Decryptor = Decrypt(self.n,self.d)
    
    def encrypt(self,message):
        return self.Encryptor.encrypt(message)
    
    def decrypt(self,message):
        return self.Decryptor.decrypt(message)
    
    def public_key_write(self):
        return PemFormatPublicKey(self.n,self.e).buildPublicKey()

    def private_key_write(self):
        return PemFormatPrivateKey(self.n,self.d).buildPrivateKey()
    