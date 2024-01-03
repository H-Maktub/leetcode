class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        t1 = 0
        l1 = [0]*10
        l2 = [0]*10
        for x,y in zip(secret,guess):
            if x == y:
                t1+=1
            else:
                l1[int(x)]+=1
                l2[int(y)]+=1
        t2 = 0
        for x,y in zip(l1,l2):
            t2+=min(x,y)
        return f'{t1}A{t2}B'