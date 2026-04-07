"""
use a dictionary(hash map)

key -> list of (timestamp, value)

because the timestamps are added in increasing order the list is sorted
which is perfect for binary search 
"""

class TimeMap:

    def __init__(self):
        self.keyStore = {} # key/value for the timestampps[val, timestamp]
        
    """
    appending the timestamp/value to the list for that key
    """
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp, value))    

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        values = self.keyStore[key]
        l, r = 0, len(values) - 1
        res = "" 
        while l <= r:
            middle = (l + r) // 2
            mid_timestamp, mid_value = values[middle]

            if mid_timestamp <= timestamp:
                res = mid_value
                l = middle + 1
            else:
                r = middle - 1
        return res               
        
