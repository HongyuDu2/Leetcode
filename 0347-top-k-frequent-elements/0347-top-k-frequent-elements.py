class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        
        heap = [(-freq, num) for num, freq in count.items()]
        
        heapq.heapify(heap)
        
        most_frequent = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return most_frequent