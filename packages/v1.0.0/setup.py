from setuptools import setup

setup(
    name='SimpleRsa',
    version='1.0.0',
    description='Simple lib for RSA encryption and decryption',
    author='Murilo Ryan Barbosa da Silva',
    author_email='murilryanbarbosa@gmail.com',
    url='https://github.com/MuriloRyan/SimpleRsa',
    packages=['SimpleRsa','SimpleRsa.ext','SimpleRsa.ext.pembuilder'],
    install_requires=['pycryptodome'],
    license='MIT',
    keywords='rsa encryption decryption cryptography',
    project_urls=
        {
        'Bug Reports': 'https://github.com/MuriloRyan/SimpleRsa/issues',
        'Source': 'https://github.com/MuriloRyan/SimpleRsa',
        }
)