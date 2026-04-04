class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res= [0]*n
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                test = stack.pop()
                res[test] = i - test
            stack.append(i)
        return res
