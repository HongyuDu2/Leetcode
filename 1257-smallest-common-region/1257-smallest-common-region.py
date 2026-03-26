class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for r in regions:
            for j in range(1, len(r)):
                parent[r[j]] = r[0]
        anster = set()
        node = region1
        while node:
            anster.add(node)
            node = parent.get(node)
        node = region2
        while node not in anster:
            node = parent.get(node)
        return node