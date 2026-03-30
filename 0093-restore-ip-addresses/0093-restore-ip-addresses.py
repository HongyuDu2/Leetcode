class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for size in range(1, 4):
                if start + size > len(s):
                    break
                
                segment = s[start: start+size]

                if (size > 1 and segment[0] == '0') or int(segment) > 255:
                    continue

                backtrack(start + size, path + [segment])
        backtrack(0, [])
        return res
            
        