class Solution:
    def nthUglyNumber(self, n: int) -> int:
        temp =[1]
        p2,p3,p5 = 0,0,0
        for i in range(1,n):
            temp.append(min(temp[p2]*2,temp[p3]*3,temp[p5]*5))
            if temp[-1] == temp[p2]*2:
                p2+=1
            if temp[-1] == temp[p3]*3:
                p3+=1
            if temp[-1] == temp[p5]*5:
                p5+=1
        return temp[-1]
