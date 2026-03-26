class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Sliding window T:O(N) S:O(1)
        if len(s1) > len(s2): 
            return False

        # Arrays of size 26 for 'a' through 'z'
        s1_count, s2_count = [0] * 26, [0] * 26

        # 1. Build the target array and the initial window array
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # 2. Count our initial matches
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # 3. Slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True
            
            # --- ADD RIGHT CHARACTER ---
            idx_r = ord(s2[r]) - ord('a')
            s2_count[idx_r] += 1
            # Did this addition create a match?
            if s1_count[idx_r] == s2_count[idx_r]:
                matches += 1
            # Did it just break a match that used to exist?
            elif s1_count[idx_r] + 1 == s2_count[idx_r]:
                matches -= 1

            # --- REMOVE LEFT CHARACTER ---
            idx_l = ord(s2[l]) - ord('a')
            s2_count[idx_l] -= 1
            # Did this removal create a match?
            if s1_count[idx_l] == s2_count[idx_l]:
                matches += 1
            # Did it just break a match that used to exist?
            elif s1_count[idx_l] - 1 == s2_count[idx_l]:
                matches -= 1

            l += 1
            
        return matches == 26

        # Sliding window T:O(N) S:O(1)
        # if len(s1) > len(s2):
        #     return False

        # count = {}
        # for i in range(len(s1)):
        #     count[s1[i]] = count.get(s1[i], 0) + 1
       
        # count2 = defaultdict(int)
        # for i in range(len(s1)):
        #     count2[s2[i]] = count2.get(s2[i], 0) + 1 

        # if count == count2:
        #     return True
        
        # l = 0 
        # for r in range(len(s1), len(s2)):
        #     if count2[s2[l]] == 1:
        #         del count2[s2[l]]
        #     else:
        #         count2[s2[l]] = count2[s2[l]] - 1
        #     count2[s2[r]] = count2[s2[r]] + 1
        #     l += 1
            
        #     if(count == count2):
        #         return True
        
        # return False