# initial thinking:
        # is that we have an array of strings that are anagrams 
        # and they can all be arragned unto different words 
        # in this problem we have to arrange the anagrams into sublists 

        # pattern this is a hashing/sorting problem 

        # we want to bucket the strings based on the property that goes with the anagram family 

        # we want to count the characters in each string mapped to a 26 fixed length tuple 




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # lets create a dictionary that is a list to map the anagrams 
        grouped_anagrams = defaultdict(list)

        # for each word in a string we can sort the characters to create a unique key for each anagram group 

        for s in strs:

            sorted_str = ''.join(sorted(s))

            # ad the string to the list  using the sorted string as the key 
            grouped_anagrams[sorted_str].append(s)
        # and then we can return the values from our map of the grouped anagrams
        return list(grouped_anagrams.values())    


        
        




        


        
           

                


        