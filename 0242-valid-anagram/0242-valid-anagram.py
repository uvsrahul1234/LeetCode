class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}

        for n in s:
            res[n] = res.get(n, 0) + 1
        
        for n in t:
            res[n] = res.get(n, 0) - 1
        
        for i in res.values():
            if i != 0:
                return False
        
        return True

        
