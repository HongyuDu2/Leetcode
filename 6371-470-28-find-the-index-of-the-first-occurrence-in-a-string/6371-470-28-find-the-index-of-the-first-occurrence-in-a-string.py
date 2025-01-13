class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_1 = 0
        output = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[needle_1]:
                if needle_1 == 0:
                    output = i
                needle_1 += 1
                if needle_1 == len(needle):
                    return output
            else:
                if needle_1 > 0:
                    i = i - needle_1
                needle_1 = 0
            i += 1

        
        return -1