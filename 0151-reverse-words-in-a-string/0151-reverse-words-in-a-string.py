class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split()
        s_new = ''
        for i in range(len(array)):
            s_new += array[-i-1]
            s_new += ' '
        
        return s_new.rstrip()
