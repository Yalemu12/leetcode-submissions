class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n



    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        # then we want to insert at the next empty position
        self.arr[self.length] = n
        self.length += 1    



    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.arr[self.length]    
 

    def resize(self) -> None:
        #create a new list with double the current capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

    # now we copy all existing elements over and update self capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr    


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
