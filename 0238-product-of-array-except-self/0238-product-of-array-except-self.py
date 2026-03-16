class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftarr = [1] * len(nums)
        rightarr = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            leftarr[i] = leftarr[i - 1] * nums[i - 1]
    
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                rightarr[i] = rightarr[i + 1] * nums[i + 1]

            res[i] = leftarr[i] * rightarr[i]
        
        return res