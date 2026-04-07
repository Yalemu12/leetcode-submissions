# initial thinking:
        # is that we have an array of strings that are anagrams 
        # and they can all be arragned unto different words 
        # in this problem we have to arrange the anagrams into sublists 

        # pattern this is a hashing/sorting problem but we are implementing sorting for this solution 

        # we want to bucket the strings based on the property that goes with the anagram family 

        # we want to count the characters in each string mapped to a 26 fixed length tuple 

# plan:
        # create a dictionary that is a list to map the anagrams 

        # for each word in a string e can sort the characters to create a unique key for each anagram group

        # add the string to the list using the sorted string as a key 

        # and then we can return the values from our map to the grouped anagrams 




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())        


        




        
        




        


        
           

                


        