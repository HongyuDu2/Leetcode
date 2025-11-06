class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        value = []
        local = []
        for i, num in enumerate(s):
            if num in '()':
                value.append(num)
                local.append(i)
        
        m = 0
        local_pop = []
        for i in range(len(value)):
            if value[i] == '(':
                m += 1
            else:
                m -= 1
            if m < 0:
                local_pop.append(local[i])
                m += 1
        
        m = 0
        local_pop2 = []
        for i in range(len(value)-1, -1, -1):
            if value[i] == ')':
                m += 1
            else:
                m -= 1
            if m < 0:
                local_pop2.append(local[i])
                m += 1

        local_final = sorted(local_pop + local_pop2)
        result = "".join(c for i, c in enumerate(s) if i not in local_final)

        return(result)

