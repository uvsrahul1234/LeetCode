class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Slinding Window T:0(N) S:O(1)
        l = 0
        sum = 0
        avg = float('-inf')
        for r in range(len(nums)):
            sum += nums[r]  
            if r - l + 1 == k:
                avg = max(avg, sum)
                sum -= nums[l]
                l += 1

            if r == len(nums) - 1:
                return avg/k
        
        return avg/k

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