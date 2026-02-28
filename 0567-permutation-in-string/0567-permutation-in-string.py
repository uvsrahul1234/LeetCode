class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window T:O(N) S:O(1)
        if len(s1) > len(s2):
            return False

        count = {}
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
       
        count2 = defaultdict(int)
        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1 

        if count == count2:
            return True
        
        l = 0 
        for r in range(len(s1), len(s2)):
            if count2[s2[l]] == 1:
                del count2[s2[l]]
            else:
                count2[s2[l]] = count2[s2[l]] - 1
            count2[s2[r]] = count2[s2[r]] + 1
            l += 1
            
            if(count == count2):
                return True
        
        return False