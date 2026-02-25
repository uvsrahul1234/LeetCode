class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        Python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 1. Calculate the sum of the very first window (first 'k' elements)
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        # 2. Slide the window from index 'k' to the end of the array
        for i in range(k, len(nums)):
            # The Magic Step: Add the new right element, subtract the old left element
            curr_sum += nums[i] - nums[i - k]
            
            # Update the highest sum found so far
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        # 3. Divide by k only once at the very end to get the average
        return max_sum / k

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