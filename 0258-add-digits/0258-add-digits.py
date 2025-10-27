class Solution:
    def addDigits(self, num: int) -> int:
        i = 10
        while i > 0:
            lst = [int(x) for x in str(num)]
            if len(lst) == 1:
                return sum(lst)
            num = sum(lst)

