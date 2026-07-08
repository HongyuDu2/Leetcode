class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            total = 1
            cap = 0
            for i in range(0, len(weights)):
                if cap + weights[i] > mid:
                    total += 1
                    cap = weights[i]
                else:
                    cap += weights[i]
            if total <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l