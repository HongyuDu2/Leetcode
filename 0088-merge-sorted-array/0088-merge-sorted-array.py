class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1[:m]
        num2 = nums2[:n]
        for i in range(0, len(num2)):
            inserted = False
            for j in range(0, len(num1)):
                if num2[i] <= num1[j]:
                    num1.insert(j, num2[i])
                    inserted = True
                    break
            if not inserted:
                num1.append(num2[i])
            
        for k in range(len(num1)):
            nums1[k] = num1[k]
    
        return nums1