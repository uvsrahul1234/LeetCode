class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Slinding Window T:0(N) S:O(1)
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum/k

        # Brute Force T:O(N⋅k) S:O(1) 
        # average = float('-inf')
         
        # for i in range(len(nums)):
        #     count = k
        #     sum = 0
        #     j = i
        #     while count != 0:
        #         sum += nums[j]
        #         j += 1
        #         count -= 1
        #     average = max(average, sum)
        #     if i == len(nums) - k:
        #         break
        
        # return average/k