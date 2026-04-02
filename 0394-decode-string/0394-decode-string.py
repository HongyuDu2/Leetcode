class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""
        for i in s:
            if i.isdigit():
                cur_num = cur_num*10 + int(i)
            elif i == "[":
                stack.append((cur_num, cur_str))
                cur_num = 0
                cur_str = ""
            elif i == "]":
                new_str, pre = stack.pop()
                cur_str = pre + new_str*cur_str
            else:
                cur_str += i
        return cur_str