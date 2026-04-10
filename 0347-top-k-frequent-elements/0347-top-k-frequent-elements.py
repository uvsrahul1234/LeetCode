class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Hashmap Bucket sort O(N) O(N)
        count = defaultdict(int)
        res = [ [] for _ in range(len(nums))]
        for i in nums:
            count[i] += 1
        
        for r, v in count.items():
            res[v - 1].append(r)
        
        print(res)
        ans = []        
        for i in range(len(res) - 1, -1, -1):
            for n in res[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans



