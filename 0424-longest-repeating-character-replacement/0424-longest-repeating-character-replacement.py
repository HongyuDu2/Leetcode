class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = 0
        best = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(count.values())
            window_len = right - left + 1
            if window_len - max_freq > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best