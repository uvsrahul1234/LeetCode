class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Slinding Window T:O(N) S:O(N) (number of unique characters in s and t)
        if t == "":
            return ""

        countT, countS = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            
            if c in countT:
                countS[c] = 1 + countS.get(c, 0)

            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                c = s[l]
                if c in countT:
                    countS[c] -= 1
                
                if c in countT and countS[c] < countT[c]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
