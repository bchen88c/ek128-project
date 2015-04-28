import ECmath
from random import SystemRandom as random
class curves:
    nist256 = ECmath.curve(115792089210356248762697446949407573530086143415290314195533631308867097853951,
                           -3,
                           41058363725152142129326129780047268409114441015993725554835256314039467401291,
                           [48439561293906451759052585252797914202762949526041747995844080717082404635286,36134250956749795798585127919587881956611106672985015071877198253568414405109],
                           115792089210356248762697446949407573529996955224135760342422259061068512044369,
                           1)
                           
class publicKey:
    def __init__(self, point):
        self.point = point

class privateKey:
    def __init__(self, x):
        self.multiplier = x

class keyPair:
    EC = ECmath.funcs()
    def generate(self, curve):
        Randall = random()
        self.private = privateKey(Randall.randint(1,curve.order-1))
        self.public = publicKey(self.EC.mult(curve.generator, self.private.multiplier, curve))
        print(self.private.multiplier, self.public.point)

class Encoder:
    EC = ECmath.funcs()
    
    def genSharedSecret(self, publicKey, curve):
        Randall = random()
        r = Randall.randint(1,curve.order-1)
        R = self.EC.mult(curve.generator, r, curve)
        S = sum(self.EC.mult(publicKey.point, r, curve))
        return (R,S)

    def findSharedSecret(self, privateKey, R, curve):
        S = sum(self.EC.mult(R, privateKey.multiplier, curve))
        return S

    def encode(self, publicKey, curve, message):
        i = self.pad(message)
        secret = self.genSharedSecret(publicKey, curve)
        transmit = (secret[0],secret[1]+i)
        return transmit

    def decode(self, privateKey, curve, transmitted):
        S = self.findSharedSecret(privateKey, transmitted[0],curve)
        message = self.unpad(transmitted[1]-S)
        return message
        
    def pad(self, message):
        i = 1
        res = 0
        for c in reversed(message):
            res += ord(c)*i
            i *= 256
        return res

    def unpad(self, padded):
        i = int(padded.bit_length()/8)
        i = 256**i
        msg = ''
        while i>=1:
            n = padded//i
            padded -= n*i
            msg += chr(n)
            i//=256
        return msg
