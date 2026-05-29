class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        res = set()
        count = 0
        while r < len(s):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            
            res.add(s[r])
