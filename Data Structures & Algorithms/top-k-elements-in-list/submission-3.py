class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # we need to return the k most frequent elements
        # then when we use the frequenies we want the k kighest
        # we can sort these frequencies using bucket sort 
        #bucket index -> frequnecy of that value
        # then we scan the frequency from highest to lowest
        freq = Counter(nums)

        n = len(nums)

        buckets = [[]for _ in range(n + 1)]
        for (val, count) in freq.items():
            buckets[count].append(val)

        ans = []
        for f in range(n, 0, -1):
            if buckets[f]:
                ans.extend(buckets[f])
                if len(ans) >= k:
                    return ans[:k]
        return ans                
                 

                  
                   




        """
        what we are we given:
        an integer array "nums" and an integer "k"

        we need to return the k most frequent elements within the array

        the answer is unique no ambiguity on which ones are top k 
        order of the output doesn't really matter 
        
        Pattern we are using:
        we want to utlize the key word frequencies lets think of Hash map

        then from these frequencies we need the k highest

        we can sort by frequency use a bucket sort to get on 0(n)

        freq -> BUCKET INDEX
        bucket index = frequency of that value
        then scan from the highest bucket down until we have collected the K elements

        Plan:
        Count the frequencies:
        freq[val] = count for each val in nums

        create buckets
        let n = len(nums)
        max possible frequency is n if all the elements are the same
        create buckets
        buckets = [[] for _ in range(n + 1)]
        for each (val, count) in freq append that value to buckets[count]

        collect the k most frequent by:
        iterate f from n down to 1 (highest freq to low)
        for each buckets[f]:
            append all values in there to ans
            if len(ans) >=k then we return the first k
        """


        