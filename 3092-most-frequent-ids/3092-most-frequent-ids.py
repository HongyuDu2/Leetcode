class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        count = defaultdict(int)
        heap = []
        ans = []
        for num, f in zip(nums, freq):
            count[num] += f
            heapq.heappush(heap, (-count[num], num))
            while heap and -heap[0][0] != count[heap[0][1]]:
                heapq.heappop(heap)
            ans.append(-heap[0][0] if heap else 0)
        return ans