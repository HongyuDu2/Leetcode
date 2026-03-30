class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        sum = 0
        for weight in w:
            sum += weight
            self.prefix_sum.append(sum)
        self.total_sum = sum


    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.prefix_sum, target)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()