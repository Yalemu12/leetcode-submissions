class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hash map where each key is a 26 legnth tuple representing character frequencies
        # and each value pair is a list of strings belonging to the anagram group
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                # covert the count array to a tuple and use it as the key
                #append the string to the list associated with that key
            result[tuple(count)].append(s)
        return list(result.values())        

        