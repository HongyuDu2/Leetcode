class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        l, r = 1, n
        output = n
        while l <= r:
            mid = (l + r)//2
            num = 0
            for i in range(0, len(piles)):
                num += (piles[i] + mid - 1) // mid
            if num <= h:
                output = mid
                r = mid - 1
            else:
                l = mid + 1
        return output

