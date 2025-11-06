class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0]*n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                results[prev_day] = i - prev_day
            stack.append(i)
        return results