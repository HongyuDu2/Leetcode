class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        max_dict = {}
        for i in range(len(s)):
                max_dict[s[i]] = i
        
        stack = []
        visited = set()

        for i, c in enumerate(s):
            if c in visited:
                continue
            
            while stack and stack[-1] > c and max_dict[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return "".join(stack)


