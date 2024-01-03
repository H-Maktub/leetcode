class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp = [1]*n
        temp_nums = [1]
        for i in range(1,n):
            temp[i] = temp[i-1]*i
            temp_nums.append(i+1)
        print(temp,temp_nums)
        ret = ""
        k-=1
        for i in range(n-1):
            index = k//temp[n-1-i]
            t = k%temp[n-1-i]
            print(ret,t,k,temp_nums,index)
            s = temp_nums.pop(index)
            ret+=str(s)
            k-=temp[n-1-i]*index
            
            
        ret+=str(temp_nums[-1])
        return ret
if __name__ == "__main__":
    a = Solution()
    b = a.getPermutation(3,6)
    print(b)
    b = a.getPermutation(6,502)
    print(b)