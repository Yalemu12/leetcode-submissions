class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we initalize a variable to count the frequencies 
        # counter gives a dictionary {value: count} in O(n) time
        freq = Counter(nums)

        # we want to build buckets(array of lists)
        n = len(nums)
        buckets = [[]for _ in range(n + 1)]
        # we allocate n+1 buckers becayse the maximum possible freq of any value (if all numbers are identical)
        #buckets[f] will store all the values that appear f times 

        # fill them
        for val, count in freq.items():
            buckets[count].append(val)

        # we can sweet from the highest frequency 
        result = []
        # we iterate frequencies from n to 1 so the first values we see are the most frequent 
        
        for f in range(n, 0, -1):  # for each frequency we dump buckets[f] into the answer
            if buckets[f]:
                result.extend(buckets[f])
                if len(result) >= k:
                    return result[:k]
            


        