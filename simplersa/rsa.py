from Crypto.Util.number import getPrime, inverse
from simplersa.plugins.json_files import (export_private_key,
                                          export_public_key,
                                          import_public_key,
                                          import_private_key)
from simplersa.exceptions.exceptions import NoKeyUsed

class GenerateKeys:
    def __init__(self):
        pass

    def generate(self, prime_size=2048):
        p = getPrime(prime_size)
        q = getPrime(prime_size)
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
    def __init__(self):
        self.KeyGenerator = GenerateKeys()
        self.Encryptor = None
        self.Decryptor = None
    
    def generate_keys(self, prime_size=2048):
        self.n, self.e, self.d = self.KeyGenerator.generate(prime_size)
        self.Encryptor = Encrypt(self.n, self.e)
        self.Decryptor = Decrypt(self.n, self.d)

    """    Reads the public key from a file and initializes the Encryptor.   """

    def public_key_read(self, filename):
        self.n, self.e = import_public_key(filename)
        self.Encryptor = Encrypt(self.n, self.e)
    
    def private_key_read(self, filename):
        self.n, self.d, self.e, self.KeyGenerator.p, self.KeyGenerator.q = import_private_key(filename)
        self.Decryptor = Decrypt(self.n, self.d)
        self.Encryptor = Encrypt(self.n, self.e)
    
    """    Reads the private key from a file and initializes the Decryptor.   """

    def public_key_write(self, filename=None):
        data = export_public_key(self.n, self.e)
        if not filename:
            filename = "public_key.json"
        
        with open(filename, "w") as f:
            f.write(data)

        return export_public_key(self.n, self.e)
    
    def private_key_write(self, filename=None):
        data = export_private_key(self.n, self.d, self.e, self.KeyGenerator.p, self.KeyGenerator.q)
        if not filename:
            filename = "private_key.json"

        with open(filename, "w") as f:
            f.write(data)

        return data
    

    def encrypt(self,message):
        if not self.Encryptor:
            raise NoKeyUsed()
        return self.Encryptor.encrypt(message)
    
    def decrypt(self,message):
        if not self.Decryptor:
            raise NoKeyUsed()
        return self.Decryptor.decrypt(message)

