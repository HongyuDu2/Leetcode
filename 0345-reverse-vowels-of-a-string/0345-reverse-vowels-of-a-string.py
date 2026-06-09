class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] not in Vowels:
                left += 1
            elif s[right] not in Vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
        