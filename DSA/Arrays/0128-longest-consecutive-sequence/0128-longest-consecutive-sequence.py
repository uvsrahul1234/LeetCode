class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Hashset T:0(N) S:O(N)
        setnum = set(nums) # used to remove duplicates
        longest = 0

        for n in setnum:
            # check if number is start of sequence
            if (n - 1) not in setnum:
                length = 1
                while(n + length) in setnum:
                    length += 1
                longest = max(length, longest)
        
        return longest