class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a list if size N filled with default values
        
        result = [0] * len(temperatures)
        # we can store just the index to save space as the tempetature can be looked up
        #via temperatures[index]
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result