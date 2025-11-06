class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        new = []
        total = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                total += 1
            else:
                new.append(total)
                total = 1
        if s:
            new.append(total)
        final = 0
        for i in range(len(new)-1):
            final += min(new[i], new[i+1])
        return final


            



