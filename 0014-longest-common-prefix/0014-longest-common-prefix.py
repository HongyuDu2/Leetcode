class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        overlap = strs[0]
        for i in range(len(strs)):
            if len(overlap) <= len(strs[i]) and strs[i].startswith(overlap):
                continue
            else:
                overlap_new = []
                l=0
                p=0
                for j in range(len(strs[i])):
                    for k in range(len(overlap)):
                        if strs[i][j] == overlap[k+p]:
                            overlap_new.append(strs[i][j])
                            p += 1
                            break
                        else:
                            l = 1
                            break
                    if l == 1:
                        break
                overlap = overlap_new
                overlap = ''.join(overlap)
                
        return overlap
        