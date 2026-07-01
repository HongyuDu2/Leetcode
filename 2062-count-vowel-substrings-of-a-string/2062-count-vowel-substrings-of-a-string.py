class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        ans = 0
        n = len(word)
        for start in range(n):
            seen = set()
            for end in range(start, n):
                if word[end] not in vowels:
                    break
                seen.add(word[end])
                if len(seen) == 5:
                    ans += 1
        return ans