class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        stack = []
        par = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in par:
                if stack and stack[-1] == par[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True
