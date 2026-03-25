class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        status = {}
        left = 0
        max_len = 0
        for i in range(0, len(s)):
            if s[i] in status and status[s[i]] >= left:
                left = status[s[i]] + 1
            status[s[i]] = i
            max_len = max(max_len, i-left+1)
        return max_len