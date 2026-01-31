class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # T:O(N) S:O(1)
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res


        # T:O(N) S:O(N)
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)

        # prod = 1
        # for i, n in enumerate(nums):
        #     prod *= n
        #     prefix[i] = prod

        # prod = 1
        # for i in range(len(nums) - 1, 0, -1):
        #     prod *= nums[i]
        #     suffix[i] = prod

        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     if i == 0:
        #         res[i] = suffix[i + 1]
        #     elif i == len(nums) - 1:
        #         res[i] = prefix[i - 1]
        #     else:
        #         res[i] = prefix[i - 1] * suffix[i + 1]
            
        # return res
            
            # Brute Force 1 - O(N2) O(1) (ignoring output array)
            # res = []
            # for i, n in enumerate(nums):
            #     prod = 1
            #     for j, k in enumerate(nums):
            #         if i != j:
            #             prod *= k
            #     res.append(prod)
            # return res


            # zero_count = nums.count(0)
        
            # # Case 1: Too many zeros (Everything becomes 0)
            # if zero_count > 1:
            #     return [0] * len(nums)
            
            # # Calculate product of all NON-ZERO numbers
            # total_product = 1
            # for n in nums:
            #     if n != 0:
            #         total_product *= n
            
            # Brute force 2 - O(N2) O(1) (ignoring output array)
            # res = []
            # for n in nums:
            #     # Case 2: Exactly one zero exists
            #     if zero_count == 1:
            #         if n == 0:
            #             res.append(total_product) # The zero spot gets the product
            #         else:
            #             res.append(0)             # Everyone else gets 0
                
            #     # Case 3: No zeros (Standard Division)
            #     else:
            #         res.append(total_product // n) # Use integer division //
                    
            # return res