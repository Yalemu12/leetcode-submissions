class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a default dictionary store the anagram groups 

        anagram_groups = defaultdict(list)

        #Process each string in the inout array
        for s in strs:

            #sort the characters to create a uniqie key for each anagram group 
            #all anagrams will have the same sorted striing 
            sorted_str = ''.join(sorted(s))

            #add the string to the list in out map using the sorted string as the key 
            anagram_groups[sorted_str].append(s)
        # return the values from our map which are the grouped anagrams   
        return list(anagram_groups.values())   


 #Time Complexity: O(n * k log k)  
 # n is the number of strings in the array 
 #and k is the maximum length of a string 
 #and for each string we peform a sorted operation which takes O(k log k) time