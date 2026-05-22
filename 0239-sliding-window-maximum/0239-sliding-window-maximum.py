class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heap = []
        # output = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     if i >= k - 1:
        #         while heap[0][1] <= i - k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output

        l = len(nums)
        dec = deque()
        res = []
        right = 0
        for left in range(l-k+1):
            while right - left < k:
                while dec and dec[-1] < nums[right]:
                    dec.pop()
                dec.append(nums[right])
                right += 1
            res.append(dec[0])
            curr_left = nums[left]
            if curr_left == dec[0]:
                dec.popleft()
        return res