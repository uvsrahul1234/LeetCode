class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window/Hashmap T:O(N) S:O(M) M = unique elements
        l, r = 0, 0
        count = defaultdict(int)
        res = 0
        while r < len(s):
            if count[s[r]] == 0:
                count[s[r]] += 1
                r += 1
                window = r - l
                res = max(res, window)
            else:
                del count[s[l]]
                l += 1
        return res