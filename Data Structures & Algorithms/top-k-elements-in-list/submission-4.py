"""
we have an interger array and it's called "nums"
and we have an integer K and we want to return the "k" most frequent 
elements that appear within the array

intuition: we are trying to find the most frequent numbers which makes us think of
frequencies 
so i'm thinking of creating a list where the indices represent the frequency
and at each index we sort all the numbers that appear that many times

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the list frequency map
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            frequency[cnt].append(num)   

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result     

        