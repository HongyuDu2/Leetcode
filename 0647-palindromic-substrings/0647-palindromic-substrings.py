class Solution:
    def extendSubstrings(self, s, l, r):
        count, n = 0, len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += self.extendSubstrings(s, i, i)
            total += self.extendSubstrings(s, i, i+1)
        return total