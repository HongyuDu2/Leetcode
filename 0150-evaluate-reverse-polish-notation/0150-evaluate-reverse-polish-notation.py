class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    c = a+b
                elif tokens[i] == "-":
                    c = b - a
                elif tokens[i] == "*":
                    c = a*b
                else:
                    c = int(b/a)
                stack.append(c)
        return stack.pop()
