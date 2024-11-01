class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dis = []
        for i in range(len(points)):
            dis.append(points[i][0]**2 + points[i][1]**2)
        
        dis.sort()
        
        L = 1
        for i in range(len(dis)-1):
            if L == k:
                #count = i+1
                #L = L + 1
                break
            L = L + 1

            #if dis[i+1] > dis[i]:
                #L = L + 1
            

        
        dis2 = []
        for j in range(len(points)):
            if points[j][0]**2 + points[j][1]**2 <= dis[i]:
                dis2.append(points[j])
        
        return dis2