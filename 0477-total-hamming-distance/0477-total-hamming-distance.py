class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for k in range(32):                        # 遍历每一个二进制位
            ones = sum((x >> k) & 1 for x in nums)  # 统计第 k 位是 1 的数的个数
            total += ones * (n - ones)              # 该位贡献 = 1的个数 × 0的个数
        return total