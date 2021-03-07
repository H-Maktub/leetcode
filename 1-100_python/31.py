from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        while i>=0 and nums[i]<=nums[i-1]:
            i -=1
        if i>0:
            j = len(nums)-1
            while j>=0 and nums[i-1]>=nums[j]:
                j-=1
            print(j)
            tmp = nums[i-1]
            nums[i-1]=nums[j]
            nums[j] = tmp

        tmp = nums[i:]
        tmp.sort()
        del nums[i:]
        nums.extend(tmp)
 

if __name__ == "__main__":
    a = Solution()
    c=[1,3,2]
    b = a.nextPermutation(c)#[1,3,2]
    print(c)
    # print('====',b)
    # b = a.nextPermutation([1,1,5])#[1,5,1]
    # print('====',b)
    # b = a.nextPermutation([1])
    # print('====',b)
    # b = a.nextPermutation([3,2,1])#[1,2,3]
    # print('====',b)
    # b = a.nextPermutation([1,2,3])#[1,3,2]
    # print('====',b)
    # b = a.nextPermutation([2,3,1])#[3,1,2]
    # print('====',b)
