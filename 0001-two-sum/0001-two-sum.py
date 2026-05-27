class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        
        for i, n in enumerate(nums):
            rem = target - n

            if rem in store:
                return [store[rem], i]
            
            store[n] = i