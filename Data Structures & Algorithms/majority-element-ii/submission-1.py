"""
we are given an array of nums size of n and we need to find all the elements that appear more than n/3 times

so this is a frequency problem to where we want to see which numbers are appearing the most
so we can use a hashmap to count the frequencies

we also need to calculate the length of the array and the threshold value
"""

"""
Solution:

1. Build a frequency map by counting occurances of each element
2. iterate through the map entries 
3. For each entry with count greater than n/3 add the element to the result
4. Return the result list
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []

        for key in count:
            if count[key] > len(nums) // 3:
                result.append(key)
        return result        



        