class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)
        counter.subtract(t)
        return all(v==0 for v in counter.values())