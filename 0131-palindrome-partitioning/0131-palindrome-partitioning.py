class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                segment = s[start:end+1]
                if is_pal(segment):
                    path.append(segment)
                    backtrack(end+1)
                    path.pop()
        def is_pal(sub):
            return sub == sub[::-1]

        backtrack(0)
        return res