class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_count = sum(1 for k, freq in task_counts.items() if freq == max_freq)
        
        intervals = (max_freq - 1) * (n + 1) + max_count
        
        return max(len(tasks), intervals)