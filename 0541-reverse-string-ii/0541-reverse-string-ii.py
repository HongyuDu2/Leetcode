class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return ""
        s = list(s)
        res = []
        stack = []
        for i in range(len(s)):
            if (i // k) % 2 == 0:
                stack.append(s[i])
                if len(stack) == k or i == len(s) - 1:
                    while stack:
                        res.append(stack.pop())
            else:
                res.append(s[i])
        return "".join(res)