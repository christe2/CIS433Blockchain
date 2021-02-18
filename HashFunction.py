
"""
maps arbitrary string of data to fixed length output
in a deterministic, public, "random" manner

-One Way
-Collision Resistance
-Target Collision Resistance
-Pseudo-Random
-Non Malleability: can't find relationship between h(x) and h(y) for all x,y


h:{0,1}* -> {0,1}^d
"""
class CryptoHash():
    def __init__(self):
        self.d = 128  # length of output
        self.b = 16  # block width
        self.r = 64  # rate

    # counts the number of bits
    def __bitNum__(self, x):
        num = 0
        while x > 0:
            x = x >> 1
            num += 1
        return num

    def __creatOnes__(self, l):
        x = 1
        for i in range(l):
            x = (x << 1) + 1
        return x

    #def shift(self):

    #def rotate(self):

    #def xor(self):

    #def add(self):

    # pads the input to have a length divisible by r
    def pad(self, x):
        l = self.__bitNum__(x)
        gap = (l + self.r) % self.r
        if gap == 0:
            padding = 1 << (self.r - 1)
            x = (x << self.r) + padding + 1
        else:
            padding = 1 << (gap - 1)
            x = (x << gap) + padding + 1
        return x

    def split(self, x):
        blocks = []
        n = x / self.r
        ones = self.__creatOnes__(self.r)
        for i in range(n):
            blocks.append(x & ones)
            x = x >> self.r
        return blocks

    def permutate(self, x):
        self.pad(x)



class MerkleTree():

