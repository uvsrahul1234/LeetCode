class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Hashmap
        count = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in count:
                return [count[diff] ,i]
            count[n] = i
        
        # Brute force
        # for i, n in enumerate(nums):
        #     for j in range(i+1, len(nums)):
        #         if n + nums[j] == target:
        #             return [i, j]
