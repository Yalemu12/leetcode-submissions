"""
we can create a result filled with zeroes and use a stack to store pairs
(tempature and index) for the days we haven't found a warmer tempature yet

"""



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, tempature in enumerate(temperatures):
            while stack and tempature > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = index - stackInd
            stack.append((tempature, index))
        return result      
        