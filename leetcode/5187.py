class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        neededApples = neededApples/4
        temp = [3]
        while temp[-1] < neededApples:
            l = len(temp)+1
            t = ((1+l+1)*(l+1)/2)*l+(l+1)*((1+l-1)*(l-1)/2)
            temp.append(t)
        return 8 * len(temp)

a = Solution()
b = a.minimumPerimeter(1000000000)
print(b)