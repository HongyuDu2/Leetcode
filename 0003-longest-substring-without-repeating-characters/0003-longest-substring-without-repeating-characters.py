class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        status = {}
        left = 0
        max_val = 0
        for i in range(0, len(s)):
            if s[i] in status and status[s[i]] >= left:
                left = status[s[i]] + 1
            status[s[i]] = i
            max_val = max(max_val, i - left + 1)
        return max_val
