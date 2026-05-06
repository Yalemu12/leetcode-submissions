class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0

            while j < len(prefix) and j < len(strs[i]):
                if prefix[j] == strs[i][j]:
                    j += 1
                else:
                    break
            # Trim down only to the matching part 
            prefix = prefix[:j] 

            if not prefix:
                return ""

        return prefix         

                

        