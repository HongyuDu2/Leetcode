class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set = {}
        for c in s:
            if c in set:
                set[c] += 1
            else:
                set[c] = 1
        for c in t:
            if c not in set:
                return False
            elif set[c] == 0:
                return False
            else:
                set[c] -= 1
        return True

