class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        for i, s in cars:
            time = (target-i)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
