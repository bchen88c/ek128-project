#Eliptic curve crypto math module

#We'll be using a curve, so it's convenient to be able to reuse this
class curve:
    a = 0
    b = 0
    mod = 1
    generator = [0,0]
    order = 0
    cofactor = 0
    def __init__(self,p,a,b,G,n,h):
        self.a = a
        self.b = b
        self.mod = p
        self.generator = G
        self.order = n
        self.cofactor = h

class funcs:
    
    def add(self, point1, point2, curve):
        res = [0,0]
        k = ((point2[1]-point1[1]) % curve.mod)
        k = k * self.inverse_mod(point2[0]-point1[0], curve.mod) % curve.mod
        res[0] = (k**2 - point1[0] - point2[0]) % curve.mod
        res[1] = (k*(point1[0]-res[0]) - point1[1]) % curve.mod
        return res
    
    def double(self, curve, point):
        res = [0,0]
        k = (3*(point[0]**2) + curve.a) % curve.mod
        k = k * self.inverse_mod(2*point[1], curve.mod) % curve.mod
        res[0] = (k**2 - 2*point[0]) % curve.mod
        res[1] = (k*(point[0]-res[0])-point[1]) % curve.mod
        return res

    def mult(self, point, scalar, curve):
        li = [int(f) for f in reversed(list(bin(scalar)[2:]))]
        n = li.index(1)
        res = point
        base = point
        for i in range(n):
            res = self.double(curve, res)
            base = self.double(curve, base)
        for i in range(n+1,len(li)):
            base = self.double(curve, base)
            if(li[i]):
                res = self.add(base,res,curve)
        return res
    
    def inverse_mod(self, a, m):
        if a < 0 or m <= a: a = a % m
        c, d = a, m
        uc, vc, ud, vd = 1, 0, 0, 1
        while c != 0:
            q, c, d = divmod( d, c ) + ( c, )
            uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
        if ud > 0: return ud
        else: return ud + m
