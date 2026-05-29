class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
             
            q.append(nums[r])

            if nums[l] > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(q[0])
                l += 1
            
            r += 1
        
        return res
