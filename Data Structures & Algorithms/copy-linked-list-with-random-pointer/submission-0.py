"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


"""
what does deep copy mean?

it means that every new node must be newly created
no new node can point to the orginal node 
the new structure should be val -> next -> random

First pass:
create a copy of every node
store mapping in the dictionary using a hashmap
don't worry about next/random yet

Second pass:
connect new_node.next and new_node.random using our hashmap

"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        # make our hashmap to store our nodes to know where to point
        old_to_knew = {}

        current = head
        while current:
            old_to_knew[current] = Node(current.val)
            current = current.next

        #Second pass
        
        current = head
        while current:
            old_to_knew[current].next = old_to_knew.get(current.next)
            old_to_knew[current].random = old_to_knew.get(current.random)

            current = current.next
        return old_to_knew[head]            
        