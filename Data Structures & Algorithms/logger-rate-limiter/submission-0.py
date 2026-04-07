"""
we need to think of what data structure would we need that
is best for looking up info that goes with a specific key
ANSWER: hash table
"""

class Logger:

    def __init__(self):
        # create our dictionary that will go across called to our next function
        self.messages = {}

        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last_message = self.messages.get(message, 0)

        if timestamp >= last_message:
            self.messages[message] = timestamp + 10
            return True
        else:
            return False    


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
