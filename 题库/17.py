from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        retList = []
        for i,num in enumerate(digits):
            tmplist = []
            for ch in temp[int(num)]:
                print('+++++++++++',len(retList),len(temp[int(num)]))
                if i==0:
                    tmplist.append(ch)
                else:
                    for ch2 in retList:
                        tmplist.append(ch2+ch)
                        print(tmplist)
            print('============',retList,tmplist)
            retList = tmplist
        return retList


if __name__ == "__main__":
    a = Solution()
    b = a.letterCombinations("234")
    print(b)