class NoKeyUsed(Exception):
    """Raised when a key is not found in the dictionary."""
    def __init__(self, message="No key used for encryption or decryption.\nPlease generate or read a key before using this method."):
        self.message = message
        super().__init__(self.message)