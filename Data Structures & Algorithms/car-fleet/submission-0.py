
"""
what do we know? 

- a car cannot pass the car in front
- if it catches up it becomes a part of that fleet and it will move at a slower speed

so the real question?
will the car behind catch the car ahead before or at the destination

for each car: time = target - position[i]/speed[i]
this tells us how long that car would take driving alone
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair the position and speed and sort them by position descending
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)        
        