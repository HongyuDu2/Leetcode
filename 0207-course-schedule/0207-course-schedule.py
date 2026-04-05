class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_arr = [[]*numCourses for _ in range(numCourses)]
        degree = [0]*numCourses

        for cur, pre in prerequisites:
            course_arr[pre].append(cur)
            degree[cur] += 1
        
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        Count = 0

        while queue:
            cur = queue.popleft()
            Count += 1
            for num in course_arr[cur]:
                degree[num] -= 1
                if degree[num] == 0:
                    queue.append(num)
        return Count == numCourses