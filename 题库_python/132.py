
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]: 
            return 0   
        l = len(s)
        t = [[True] * l for _ in range(l)]

        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                print(i,j)
                t[i][j] = (s[i] == s[j]) and t[i + 1][j - 1]
        f = [l-1] * l
        print(f)
        for i in range(l):
            if t[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if t[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[-1]

if __name__ == "__main__":
    a = Solution()
    b = a.minCut("aab")
    print(b)