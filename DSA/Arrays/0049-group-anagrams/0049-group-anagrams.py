class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Hashmap T:O(m*n) S:O(m) 
        # m = no of strs, n = len of longest str

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())

                