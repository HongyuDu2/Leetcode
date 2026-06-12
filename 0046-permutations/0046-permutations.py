class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)
        # def backtrack(i):
        #     if i == n:
        #         res.append(nums[:])
        #         return
        #     for j in range(i, n):
        #         nums[i], nums[j] = nums[j], nums[i]
        #         backtrack(i+1)
        #         nums[i], nums[j] = nums[j], nums[i]

        # backtrack(0)
        # return res

        res = []
        path = []
        used = [False]*len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return res