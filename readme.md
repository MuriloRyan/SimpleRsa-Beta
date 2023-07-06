# Simple Rsa v1.0.0

This my newest project, an simple implementation of rsa algorithm thats use the Crypto.Util lib to generate (in standard mode) 2048 prime numbers to use as p and q to generate the keys of the algorithm

this is an simple implementation, because of this, remember this is made mainly for educational use (mainly using Single Responsability Principle)

but if you want to use this implementation, see the tutorial:

* go to packages/vrsion/dist , choose the last release, download in an new directory, and in the terminal:

```
pip install SimpleRsa-Version.tar.gz
```
_swap 'Version' for the version of the file name_

* To use, go to your python file and write something like

```
from SimpleRsa import Rsa

rsa = Rsa() #you can declare p,q here

message = "Hello, World!"
encrypted = rsa.encrypt(message)
```
