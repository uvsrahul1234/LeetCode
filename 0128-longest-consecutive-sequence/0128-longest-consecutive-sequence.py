class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numSet = set(nums)
        res = 0        

        for n in numSet:
            if (n - 1) not in numSet:
                size = 0
                while (n + size) in numSet:
                    size += 1
                res = max(res, size)
        
        return res