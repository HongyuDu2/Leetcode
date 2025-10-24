class Solution:
    def validPalindrome(self, s: str) -> bool:
        def inner_test(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return inner_test(left+1, right) or inner_test(left, right-1)
            left += 1
            right -= 1
        return True