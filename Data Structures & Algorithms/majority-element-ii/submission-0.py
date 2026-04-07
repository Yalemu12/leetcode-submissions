"""
we are given an array of nums size of n and we need to find all the elements that appear more than n/3 times

so this is a frequency problem to where we want to see which numbers are appearing the most
so we can use a hashmap to count the frequencies

we also need to calculate the length of the array and the threshold value
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        threshold = len(nums) // 3
        result = [num for num, count in counts.items() if count > threshold]

        cand1, count1 = None, 0
        cand2, count2 = None, 0

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return result                        

        