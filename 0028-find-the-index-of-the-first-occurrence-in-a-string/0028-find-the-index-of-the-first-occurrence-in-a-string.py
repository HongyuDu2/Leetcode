class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n, m = len(haystack), len(needle)
        if m == 1:
            return haystack.find(needle)  # 或者手写遍历返回第一个等于needle[0]的位置
        for i in range(n - m + 1):
            if haystack[i] == needle[0]:
                for j in range(1, m):
                    if haystack[i + j] != needle[j]:
                        break
                    if j == m - 1:
                        return i
        return -1