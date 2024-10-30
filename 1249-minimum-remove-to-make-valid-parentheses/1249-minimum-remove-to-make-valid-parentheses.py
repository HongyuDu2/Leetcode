class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_input = list(s)  # Convert the string to a list of characters
        n = 0  # Count of open parentheses
        m = 0  # Count of close parentheses
        
        # First pass: remove invalid closing parentheses
        for i in range(len(s_input)):
            if s_input[i] == '(':
                n += 1  # Increment open parentheses count
            elif s_input[i] == ')':
                if n > m:  # Valid closing parenthesis
                    m += 1  # Increment valid close count
                else:
                    s_input[i] = '&'  # Mark invalid closing parenthesis
        
        # Filter out invalid closing parentheses
        s_input = [item for item in s_input if item != '&']
        
        # Reset counts for second pass
        n = 0  # Count of close parentheses
        m = 0  # Count of open parentheses
        
        # Second pass: remove invalid opening parentheses
        s_input.reverse()  # Reverse the list to process from right to left
        for i in range(len(s_input)):
            if s_input[i] == ')':
                n += 1  # Increment close parentheses count
            elif s_input[i] == '(':
                if n > m:  # Valid opening parenthesis
                    m += 1  # Increment valid open count
                else:
                    s_input[i] = '&'  # Mark invalid opening parenthesis
        
        # Filter out invalid opening parentheses
        s_input = [item for item in s_input if item != '&']
        s_input.reverse()  # Reverse back to original order
        
        s_str = ''.join(s_input)  # Join list back to string
        return s_str
        
        
        

        