# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

'''
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def is_numeric(value):
            return isinstance(value, (int, float))
        
        def flatten_one_level(nested_list):
            flat_list = []
            for item in nested_list:
                if isinstance(item, list):
                    flat_list.extend(item)
                else:
                    flat_list.append(item) 
            return flat_list

        def looop(nestedList, L):
            Total = 0
            for i in range(0, len(nestedList)):
                if is_numeric(nestedList[i]) == True:
                    Total = Total + L * nestedList[i]
                    nestedList[i] = '&'
            nestedList = [item for item in nestedList if item != '&']
            return nestedList, Total

        L = 1
        T = 0
        Sum = 0
        
        while T < 1:
            Output = looop(nestedList, L)
            Sum = Sum + Output[1]
            if len(Output[0]) == 0:
                break
            else:
                nestedList = flatten_one_level(Output[0])
                L = L + 1
        
        return Sum
'''
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def dfs(nested_list, depth):
            total = 0
            for item in nested_list:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
            





