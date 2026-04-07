# we are trying to convert a list of strings into a single encoded string 
# then be able to deconde that single string back to it's orginal list 

# so how do we do this 
# the simple solution would be to get it to tell us what the length of the string is first 

#Example: 3:cat3:dog and to decode this -> Read "3" next 3 letters are one word "cat"



class Solution:

    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res   

        

    def decode(self, str):
        res = []
        i = 0
        
        # iteration loop to actually read a word with our encoding logic and to keep going 
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res    
              



       




           


