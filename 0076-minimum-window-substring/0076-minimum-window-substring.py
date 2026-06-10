class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""
        need = Counter(t)
        required = len(need)

        window = {}
        formed = 0

        left = 0
        best_length = float('inf')
        best_begin = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_begin = left

                left_car = s[left]
                window[left_car] -= 1
                if left_car in need and window[left_car] < need[left_car]:
                    formed -= 1
                left += 1
        return "" if best_length == float('inf') else s[best_begin:best_begin+best_length]
