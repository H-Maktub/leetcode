class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a < b:
            a,b = b,a
        for i in range(n-1,-1,-1):
            x = 2**i
            a1 = a & x
            b1 = b & x
            if a1 == b1 == 0:
                a = a | x
                b = b | x
            if a1 != b1:
                a2 = a ^ x
                b2 = b ^ x
                if a > b:
                    if a1 != 0 and a2 > b2:
                        a = a2
                        b = b2
                else:
                    a = a2
                    b = b2
            print(x,a,b,i)
        print("======",bin(a))
        print("======",bin(b),)
        return (a*b) % int(1e9+7)
a = Solution()
b = a.maximumXorProduct(12,5,4)
print("======",b)

b = a.maximumXorProduct(6,7,5)
print("======",b)

b = a.maximumXorProduct(1,6,3)
print("======",b)

b = a.maximumXorProduct(0,7,2)
print("======",b)

b = a.maximumXorProduct(2,9,2)
print("======",b)
b = a.maximumXorProduct(53449611838892,712958946092406,6)
print("======",b)

0b10100010000110111010110000101110001010010101100101
0b00001100001001110010110101001000001000010110111111