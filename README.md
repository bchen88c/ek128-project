# ek128-project

ECC project

Members: Anton Paquin, William Chen, David Feng, Jeffrey Lin

Objective: The goal of this project is to demonstrate a basic elliptic-curve cryptography scheme with a GUI to facilitate one-time pad encoding and decoding of messages, fully written in Python. The NIST256 curve is used.

Results/Analysis: The entire backend/mathematical implementation of vanilla ECC is implemented, thanks to Anton. It is notable that for practical applications, the AES256 cipher would be used instead of one-time pad.
The front-end of the crypto was developed by Will, David, and Jeffrey, using the integrated Tkinter Python package. As of now, it is able to generate a public-private keypair and return the user an encoded message. Decoding directly from the encoded message is possible; however, there are currently some issues with decoding from a given encoded message.

Appendix: While a Python ECDSA library (https://github.com/warner/python-ecdsa) was consulted for some reference, the code located inside cryptosystem.py and ECmath.py was primarily created from scratch.
