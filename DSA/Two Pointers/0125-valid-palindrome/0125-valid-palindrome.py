class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointers T:O(N) S:O(1)
        l = 0
        r = len(s) - 1

        while l < r:
            while not self.alphaNumeric(s[l]):
                l += 1
            while not self.alphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True
    
    def alphaNumeric(self, ch):
        return (ord('0') <= ord(ch) <= ord('9') or
                ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z'))
        
        # T:O(N) S:O(N) Using inbuilt functionality
        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]