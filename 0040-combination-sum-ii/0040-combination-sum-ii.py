class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, path_sum):
            if path_sum == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if path_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, path_sum + candidates[i])
                path.pop()
        backtrack(0, 0)
        return res
