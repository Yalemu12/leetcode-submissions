class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        we are given an integer array nums 
        and an integer "k" 
        and we need to return the k most frequent elements nin nums 
        the answer is unique

        Pattern:
        we want frequencies so think of --> hashmap(Counter)
        then from those frequencies we need the k kighest

        We will do Bucket sort for a clean O(n) solution
        """              
        freq = Counter(nums)

        n = len(nums)

        # buckets: index = frequency, value = list of numbers with that frequency 
        buckets = [[] for _ in range(n + 1)]
        for val, count in freq.items():
            buckets[count].append(val)

        # then we can transverse the buckets from the highest frequency down 
        ans = []
        for f in range(n, 0, -1):
            if buckets[f]:
                ans.extend(buckets[f])
                if len(ans) >= k:
                    return ans[:k]
        return ans                    


        