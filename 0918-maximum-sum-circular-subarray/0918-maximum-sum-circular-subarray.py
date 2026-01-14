class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        extended = nums + nums
        prefix = [0]
        for x in extended:
            prefix.append(prefix[-1] + x)
        
        max_sum = float('-inf')
        q = deque()
        q.append(0)
        for j in range(1, len(prefix)):
            while q and  j - q[0] > n:
                q.popleft()
            max_sum = max(max_sum, prefix[j]-prefix[q[0]])
            while q and prefix[j] <= prefix[q[-1]]:
                q.pop()
            q.append(j)
        return max_sum