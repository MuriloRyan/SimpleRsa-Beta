from setuptools import setup

setup(
    name='SimpleRsa',
    version='1.0.0',
    description='Simple lib for RSA encryption and decryption',
    author='Murilo Ryan Barbosa da Silva',
    packages=['simple_rsa'],
    install_requires=['pycryptodome','base64']
)