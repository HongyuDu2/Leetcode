class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_arr = [[] for _ in range(numCourses)]
        degree = [0]*numCourses

        for pre, cur in prerequisites:
            course_arr[pre].append(cur)
            degree[cur] += 1
        
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        Count = 0

        while queue:
            cur = queue.popleft()
            Count += 1
            for nums in course_arr[cur]:
                degree[nums] -= 1
                if degree[nums] == 0:
                    queue.append(nums)
        return Count == numCourses