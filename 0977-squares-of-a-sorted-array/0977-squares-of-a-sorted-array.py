class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Two pointers T:O(N) S:O(N) : without reverse function
        l = 0
        r = len(nums) - 1

        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
                
        return res
        
        # Two pointers T:O(N) S:O(N)
        # l = 0
        # r = len(nums) - 1

        # res = []

        # while l <= r:
        #     if abs(nums[l]) > abs(nums[r]):
        #         res.append(nums[l] ** 2)
        #         l += 1
        #     else:
        #         res.append(nums[r] ** 2)
        #         r -= 1
        
        # res.reverse()
        # return res

        
            