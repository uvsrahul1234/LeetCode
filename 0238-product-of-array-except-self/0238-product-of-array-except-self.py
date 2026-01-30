class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            # Brute Force
            # res = []
            # for i, n in enumerate(nums):
            #     prod = 1
            #     for j, k in enumerate(nums):
            #         if i != j:
            #             prod *= k
            #     res.append(prod)
            # return res

            zero_count = nums.count(0)
        
            # Case 1: Too many zeros (Everything becomes 0)
            if zero_count > 1:
                return [0] * len(nums)
            
            # Calculate product of all NON-ZERO numbers
            total_product = 1
            for n in nums:
                if n != 0:
                    total_product *= n
            
            res = []
            for n in nums:
                # Case 2: Exactly one zero exists
                if zero_count == 1:
                    if n == 0:
                        res.append(total_product) # The zero spot gets the product
                    else:
                        res.append(0)             # Everyone else gets 0
                
                # Case 3: No zeros (Standard Division)
                else:
                    res.append(total_product // n) # Use integer division //
                    
            return res