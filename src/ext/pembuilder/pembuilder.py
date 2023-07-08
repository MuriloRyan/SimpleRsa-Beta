import base64

def pemfile(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

class PemFormatPublicKey:
    def __init__(self,n,e):
        self.n = n
        self.e = e

    def buildPublicKey(self):
        public_key_pem = f"-----BEGIN PUBLIC KEY-----\n"
        encoded_n = base64.b64encode(self.n.to_bytes((self.n.bit_length() + 7) // 8, 'big')).decode()
        
        for i in range(0, len(encoded_n), 64):
            public_key_pem += encoded_n[i:i+64] + "\n"

        public_key_pem += f"-----END PUBLIC KEY-----"
        return pemfile(public_key_pem, 'public-key.pem')

class PemFormatPrivateKey:
    def __init__(self,n,d):
        self.n = n
        self.d = d

    def buildPrivateKey(self):
        private_key_pem = f"-----BEGIN PRIVATE KEY-----\n"
        encoded_n = base64.b64encode(self.n.to_bytes((self.n.bit_length() + 7) // 8, 'big')).decode()
        encoded_d = base64.b64encode(self.d.to_bytes((self.d.bit_length() + 7) // 8, 'big')).decode()
        
        for i in range(0, len(encoded_n), 64):
            private_key_pem += encoded_n[i:i+64] + "\n"

        for i in range(0, len(encoded_d), 64):
            private_key_pem += encoded_d[i:i+64] + "\n"

        private_key_pem += f"-----END PRIVATE KEY-----"
        return pemfile(private_key_pem, 'private-key.pem')