class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force T:O(n2) S:O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Hashset T:O(n) S:O(n)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
