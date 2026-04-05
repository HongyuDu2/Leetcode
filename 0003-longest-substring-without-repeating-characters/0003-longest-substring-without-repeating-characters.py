class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        status = {}
        total = 0
        left = 0
        for i in range(len(s)):
            if s[i] in status and status[s[i]] >= left:
                left = status[s[i]] + 1
            status[s[i]] = i
            total = max(total, i - left + 1)
        return total