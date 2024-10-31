'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_input = list(s)
        s_input2 = s_input[::-1]         # 反转复制的列表

        t = s_input
        for i in range(len(s_input)):
            if s_input[i] == s_input2[i]:
                continue
            else:
                if i < len(s_input) - 1 and s_input[i] == s_input2[i + 1]:
                    if  s_input[i + 1] != s_input2[i]:
                        s_input2.pop(i)
                        t = s_input2
                        break
                    else:
                        s_input2.pop(i)
                        t = s_input2
                        break
                elif i < len(s_input) - 1 and s_input[i + 1] == s_input2[i]:
                    if s_input2[i + 1] != s_input[i]:
                        s_input.pop(i)
                        t = s_input
                        break
                    else:
                        s_input2.pop(i)
                        t = s_input2
                        break
                else:
                    return False  # 如果没有符合条件的情况
        
        t_reverse = t[::-1]  # Create a reversed copy of t
        for i in range(len(t)):
            if t[i] == t_reverse[i]:  # Compare with the reversed copy
                continue
            else:
                return False  # If any characters do not match, return False
        
        return True
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome_range(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Check if we can skip either character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True  # If the loop completes, it's a palindrome
                
