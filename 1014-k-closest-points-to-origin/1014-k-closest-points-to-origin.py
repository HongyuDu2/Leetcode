class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = -(x * x + y * y)   # 负号 → 最大堆效果
            heapq.heappush(heap, (dist, x, y))
            
            # Maintain heap size k
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for (_, x, y) in heap]