class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window/set T:O(N) S:O(M) M = unique element
        l = 0
        window_chars = set()
        res = 0
        
        for r in range(len(s)):
            while s[r] in window_chars:
                window_chars.remove(s[l])
                l += 1
            
            window_chars.add(s[r])
            res = max(res, r - l + 1)
            
        return res
        
        # Sliding Window/Hashmap T:O(N) S:O(M) M = unique elements
        # l, r = 0, 0
        # count = defaultdict(int)
        # res = 0
        # while r < len(s):
        #     if count[s[r]] == 0:
        #         count[s[r]] += 1
        #         r += 1
        #         window = r - l
        #         res = max(res, window)
        #     else:
        #         del count[s[l]]
        #         l += 1
        # return res