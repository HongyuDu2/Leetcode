class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set = {}
        for i in s:
            if i not in set:
                set[i] = 1
            else:
                set[i] += 1
        for j in t:
            if j not in set:
                return False
            elif set[j] == 0:
                return False
            else:
                set[j] -= 1
        return True

