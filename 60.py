from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length):
            print(i)
            if digits[length-1-i]!=9:
                digits[length-1-i] +=1
                break
            else:
                digits[length-1-i] =0
                if i == length-1:
                    digits.insert(0,1)
        return digits

if __name__ == "__main__":
    b = Solution()
    a = b.plusOne(digits=[0,9,8])
    print(a)
    a = b.plusOne(digits=[9,9,9])
    print(a)