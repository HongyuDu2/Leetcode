class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        current_number = 0
        current_operator = '+'  # Start with an initial operator
        s = s.replace(" ", "")  # Remove any spaces in the string
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # If the character is an operator or if it's the last character
            if not char.isdigit() or i == len(s) - 1:
                if current_operator == '+':
                    stack.append(current_number)
                elif current_operator == '-':
                    stack.append(-current_number)
                elif current_operator == '*':
                    stack[-1] = stack[-1] * current_number
                elif current_operator == '/':
                    # Properly handle truncation towards zero for division
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // current_number)
                    else:
                        stack[-1] = stack[-1] // current_number
                
                # Update operator and reset current number
                current_operator = char
                current_number = 0

        return sum(stack)