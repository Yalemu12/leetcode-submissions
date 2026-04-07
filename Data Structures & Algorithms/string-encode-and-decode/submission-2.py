# we are trying to convert a list of strings into a single encoded string 
# then be able to deconde that single string back to it's orginal list 

# so how do we do this 
# the simple solution would be to get it to tell us what the length of the string is first 

#Example: 3:cat3:dog and to decode this -> Read "3" next 3 letters are one word "cat"






class Solution:

    def encode(self, strs: List[str]) -> str:
        #create an empty string to accumalate our encoded result 

        result = ""
        #iterates through each string in the input list and s represents the current string we are processing 

        for s in strs:
            # core encoding logic
            # we are getting the length of the current string
            # and converting that length to a string with "strs(len(s))"
            # add a colon seperator and add the actual string content
            #we append this to our string result 
            result += str(len(s)) + ":" + s 
        return result    

#Current state : "2:hi3:bye"

    def decode(self, s: str) -> List[str]:
        #we want to decode a single string back into a list of strings 
        result = []
        #empty list to store the decoded strings 
        i = 0
        #index pointer to track our position within the string 

        while i < len(s):
            colon_pos = s.find(":", i)
            length = int(s[i:colon_pos])
            start = colon_pos + 1
            string = s[start:start + length]
            result.append(string)
            i = start + length
        return result





           


