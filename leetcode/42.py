from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l==0:return 0
        right_index = [-1] *l
        right_index[-1] = l-1
        for i in range(1,l):
            if height[l-i-1]>height[right_index[l-i]]:
                right_index[l-i-1] = l-i-1
            else:
                right_index[l-i-1] = right_index[l-i]
        print(right_index)
        ret = 0
        temp = 0
        total=0
        for i in range(1,l):
            if height[i]>=height[temp]:
               ret += total +height[temp]*(i-temp-1)
               print(i,ret)
               temp = i
               total = 0
            elif i==right_index[temp+1]:
                ret += total + height[i]*(i-temp-1)
                print(i,ret)
                print("right",temp,i)
                temp = i
                total = 0
            else:
                total-=height[i]
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print("=======",b)
    b = a.trap([4,2,0,3,2,5])
    print("=======",b)