class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            r = 1
            m = n
            while m > 0:
                r*=m%10
                m = m//10
            if r % t == 0:
                return n
            n+=1