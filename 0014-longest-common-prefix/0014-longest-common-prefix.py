class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # overlap = strs[0]
        # for i in range(len(strs)):
        #     if len(overlap) <= len(strs[i]) and strs[i].startswith(overlap):
        #         continue
        #     else:
        #         overlap_new = []
        #         l=0
        #         p=0
        #         for j in range(len(strs[i])):
        #             for k in range(len(overlap)):
        #                 if strs[i][j] == overlap[k+p]:
        #                     overlap_new.append(strs[i][j])
        #                     p += 1
        #                     break
        #                 else:
        #                     l = 1
        #                     break
        #             if l == 1:
        #                 break
        #         overlap = overlap_new
        #         overlap = ''.join(overlap)
                
        # return overlap
        if not strs:
            return ""
        for i in range(len(strs[0])):
            character = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != character:
                    return strs[0][:i]
        return strs[0]


        