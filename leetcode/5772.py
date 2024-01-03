class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        temp = [firstWord,secondWord,targetWord]
        for i in range(3):
            num = 0
            for j in range(len(temp[i])):
                num += (ord(temp[i][-(j+1)])-97) * 10**j
            temp[i] = num
        print(temp)
        return temp[-1] == temp[0] + temp[1]

            
a = Solution()
b = a.isSumEqual("acb","cba","cdb")