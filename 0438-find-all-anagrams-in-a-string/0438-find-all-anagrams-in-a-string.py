class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        count_p = Counter(p)
        Window = Counter(s[:len(p)])
        res = []
        if Window == count_p:
            res.append(0)
        for right in range(len(p), len(s)):
            Window[s[right]] += 1
            left = s[right - len(p)]
            Window[left] -= 1
            if Window[left] == 0:
                del Window[left]
            if Window == count_p:
                res.append(right-len(p)+1)
        return res