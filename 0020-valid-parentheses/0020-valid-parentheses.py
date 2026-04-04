class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        test = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in test.keys():
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            if c != test[stack[-1]]:
                return False
            stack.pop()
        return len(stack) == 0
            