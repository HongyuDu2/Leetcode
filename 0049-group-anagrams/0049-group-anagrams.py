class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagram_dict = defaultdict(list)
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            anagram_dict[sorted_word].append(word)
            
        return list(anagram_dict.values())
        