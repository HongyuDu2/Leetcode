class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        last_op = "+"
        s += "+"
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char != " ":
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                last_op = char
                num = 0
        return sum(stack)