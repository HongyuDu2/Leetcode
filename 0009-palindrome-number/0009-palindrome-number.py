class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x = list(x)
        res = []
        for i in range(len(x)-1,-1,-1):
            res.append(x[i])
        x1 = "".join(res)
        x = "".join(x)
        if x1 == x:
            return True
        else:
            return False