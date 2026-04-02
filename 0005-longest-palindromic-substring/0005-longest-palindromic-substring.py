class Solution:
    def longestPalindrome(self, s: str) -> str:
        def dfs(l, r):
            while l >= 0 and r <= len(s)-1 and s[l]==s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            odds = dfs(i,i)
            even = dfs(i,i+1)
            if len(odds) > len(res):
                res = odds
            if len(even) > len(res):
                res = even
        return res