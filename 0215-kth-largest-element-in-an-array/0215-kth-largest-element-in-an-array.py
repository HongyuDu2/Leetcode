class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Use a min-heap of size k
        min_heap = []
    
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
    
    # The root of the min-heap is the k-th largest element
        return min_heap[0]
        

        