
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0]*(1<<10)
        cnt[0]=1
        state = 0
        ans = 0
        for ch in word:
            print("=============")
            state ^=1<<(ord(ch) - ord('a'))
            print("state",state,cnt[state])
            ans += cnt[state]
            print("ans",ans)
            for i in range(10):
                print(state ^ (1 << i))
                ans+=cnt[state ^ (1 << i)]
            cnt[state] += 1
        print(cnt)
        return ans

a = Solution()
b = a.wonderfulSubstrings("aba")
print(b)
