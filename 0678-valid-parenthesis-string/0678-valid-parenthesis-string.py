class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for r in s:
            if r == "(" or r == "*":
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        count = 0
        for r in reversed(s):
            if r == ")" or r == "*":
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return True