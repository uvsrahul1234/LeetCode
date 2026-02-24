class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window T:O(N) S:O(1)/O(26)
        l = 0
        count = defaultdict(int)
        res = 0
        maxfreq = 0

        for r in range(len(s)):
            window = r - l + 1
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])

            if window - maxfreq <= k:
                res = max(res, window)
                continue
            
            count[s[l]] -= 1
            l += 1
        return res

        # Sliding Window T:O(N)/O(26*N) S:O(1)/O(26)
        # l = 0
        # count = defaultdict(int)
        # res = 0

        # for r in range(len(s)):
        #     window = r - l + 1
        #     count[s[r]] += 1

        #     if window - max(count.values()) <= k:
        #         res = max(res, window)
        #         continue
            
        #     count[s[l]] -= 1
        #     l += 1

        # return res