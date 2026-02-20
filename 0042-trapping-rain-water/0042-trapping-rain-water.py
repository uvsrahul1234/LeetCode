class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Two pointers: T:O(N) S:O(1)
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

        # Brute Force: T:O(N) S:O(N)
        # maxleft = [0] * len(height)
        # maxright = [0] * len(height)

        # # getting max height on left for each height
        # for i in range(0, len(height)):
        #     if i == 0:
        #         maxleft[i] = 0
        #     else:
        #         maxleft[i] = max(height[i - 1], maxleft[i - 1])
        
        # # getting max height on right for each height
        # for i in range(len(height) - 1, -1, -1):
        #     if i == len(height) - 1:
        #         maxright[i] = 0
        #     else:
        #         maxright[i] = max(height[i + 1], maxright[i + 1])
        
        # minarr = [0] * len(height)
        
        # res = 0
        # for i in range(0, len(height)):
        #     minarr[i] = min(maxleft[i], maxright[i])
        #     if (minarr[i] - height[i]) > 0:
        #         res += minarr[i] - height[i]

        # return res