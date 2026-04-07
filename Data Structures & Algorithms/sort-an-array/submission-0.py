"""
our time complaxity is O(n log n)
and we want to use the smallest space possible

what sorting algorithim runs in O(n log n) time

"""



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(i , heap_size):
            largest = i
            left = 2*i + 1
            right = 2*i + 2
        # check the left child
            if left < heap_size and nums[left] > nums[largest]:
                largest = left

            if right < heap_size and nums[right] > nums[largest]:
                largest = right

        # if the largest is not the root
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(largest, heap_size)
        # now lets build the max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)
        return nums        

        