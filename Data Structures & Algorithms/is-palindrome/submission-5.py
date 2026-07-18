class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create an empty string
        new_string = ''
        #loop though each character c within the input string s
        for c in s:
            # if c is alphumnumeric then we convert it to lowercase and add it to the new_string 
            if c.isalnum():
                new_string += c.lower()
        #Compare newStr with it's reverse(newStr[::-1])
        # if they are equal we return true if not then we return False         
        return new_string == new_string[::-1]        
        
