# initial thinking:
        # is that we have an array of strings that are anagrams 
        # and they can all be arragned unto different words 
        # in this problem we have to arrange the anagrams into sublists 

        # pattern this is a hashing/sorting problem 

        # we want to bucket the strings based on the property that goes with the anagram family 

        # we want to count the characters in each string mapped to a 26 fixed length tuple 




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))

            anagrams[sorted_str].append(s)
        return list(anagrams.values())    




        
        




        


        
           

                


        