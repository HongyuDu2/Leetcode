class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backshift(index, path):
            if index == len(digits):
                res.append(path)
                return
            
            letters = phone_map[digits[index]]
            for chi in letters:
                backshift(index + 1, path + chi)
        
        backshift(0, "")
        return res
