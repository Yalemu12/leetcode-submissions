class Solution:
    def maxArea(self, height: List[int]) -> int:
        #create a finction called maxArea that can take a list pf heights as an inpiut 
        max_water = 0 # track the maximum area we have found so far stating from 0 
        left = 0 #we set up two pointes "left" starts at index 0 the most left line while 
        right = len(height) - 1 #right starts at index len(height) -1

        while left < right:

            #cLCULATE THE WIDTH OF THE CONTAINER
            width = right - left

            #find the height of the container(limited by the shorter line )
            #the height of our container is limited by the shorter 2 lines water is spilled over the
            # shorter side wo we take the minimum of the 2 heights
            container_height = min(height[left], height[right])

            #we calculate the area of the curent container as width * height
            current_area = width * container_height
            #we update max_water if the area is larger than we have ever seen
            max_water = max(max_water, current_area)

            #this is crucial that we always move the pointer that goes to the shorter line 
            #if the left line is shorter we move left one step to the right
            #if the right line is shorter or equal we move right one step to the left

            if height[left] < height[right]:
                left += 1
            else:
                right-= 1


        return max_water            

        
                   

        