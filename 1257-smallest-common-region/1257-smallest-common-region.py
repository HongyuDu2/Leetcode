class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for i in range(len(regions)):
            for j in range(1, len(regions[i])):
                parent[regions[i][j]] = regions[i][0]
        anscter = set()
        node = region1
        while node:
            anscter.add(node)
            node = parent.get(node)
        node = region2
        while node not in anscter:
            node = parent.get(node)
        return node
    