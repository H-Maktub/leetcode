class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        length = 0
        left = 0
        tag = 0
        for ch in s:
            if ch in cache:
                l = tag - left
                length = max(length,l)
                left = max( cache[ch]+1,left)
            cache[ch] = tag
            tag = tag + 1
        l = tag - left
        length = max(length,l)
        return length

if __name__ == "__main__":
    a = Solution.lengthOfLongestSubstring("",s="abba")
    print ('aa',a)
    pass