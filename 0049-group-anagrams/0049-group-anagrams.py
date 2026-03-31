class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            new_map[key].append(s)
        return list(new_map.values())