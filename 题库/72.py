class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        temp = [[0] *(w2+1) for _ in range(w1+1)]
        for i in range(w1+1):
            temp[i][0]=i
        for i in range(w2+1):
            temp[0][i]=i
        for i in temp:
            print(i)
        for i in range(1,w1+1):
            for j in range(1,w2+1):
                left = temp[i - 1][j] + 1
                down = temp[i][j - 1] + 1
                left_down = temp[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                temp[i][j] = min(left, down, left_down)
        return temp[-1][-1]

if __name__ == "__main__":
    a = Solution()
    b = a.minDistance("horse","ros")
    print(b)