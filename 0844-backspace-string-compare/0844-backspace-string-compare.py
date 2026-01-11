class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        for i in s:
            if i != '#':
                a.append(i)
            else:
                if a:
                    a.pop()
        for i in t:
            if i != '#':
                b.append(i)
            else:
                if b:
                    b.pop()
        if a == b:
            return True
        else:
            return False