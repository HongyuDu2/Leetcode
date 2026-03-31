class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for x in arr:
            if x <= k:
                k += 1
            else:
                break
        return k