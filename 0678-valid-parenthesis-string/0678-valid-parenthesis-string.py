class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(' or c == '*':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        count = 0
        for c in reversed(s):
            if c == ')' or c == '*':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return True