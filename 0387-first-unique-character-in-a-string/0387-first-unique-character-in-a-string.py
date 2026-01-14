class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque()
        hash_map = dict()
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
                q.append((s[i],i))
        
        for i in range(len(q)):
            k = q.popleft()
            if hash_map[k[0]] == 1:
                return k[1]
        return -1