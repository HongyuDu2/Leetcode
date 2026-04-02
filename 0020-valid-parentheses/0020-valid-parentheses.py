class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mark = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in mark.keys():
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            if c != mark[stack[-1]]:
                return False
            stack.pop()
        return len(stack) == 0