class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = "+"
        s += "+"
        for t in s:
            if t.isdigit():
                num = num * 10 + int(t)
            elif t != " ":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                op = t
                num = 0
        return sum(stack)