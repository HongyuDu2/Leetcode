class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mark = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in mark.keys():
                stack.append(i)
                continue
            if len(stack) == 0:
                return False
            if i != mark[stack[-1]]:
                return False
            stack.pop()
        return len(stack) == 0