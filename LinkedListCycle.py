from timeit import default_timer as timer
from datetime import timedelta

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


nodes = [ListNode(i) for i in range(1_000)]

for i in range(len(nodes) -1):
    nodes[i].next = nodes[i+1]

nodes[999].next = nodes[200]

"""
explanation: 
we create a dictionary to keep nodes that we've seen. If there is such a node that we
encounter again we return 1 which means a cycle has happened. If there is a head with
value None this means that linked list has come to an end, so we return 0.
"""

def hasCycle_dict(head):
    dictNodes = {}
    while head:
        head = head.next
        if head not in dictNodes:
            dictNodes[head] = 1
        else:
            return 1
    return 0

"""
explanation: 
we create a set to keep nodes that we've seen. If there is such a node that we
encounter again we return 1 which means a cycle has happened. If there is a head with
value None this means that linked list has come to an end, so we return 0.
"""

def hasCycle_set(head):
    nodes = set()
    while head:
        head = head.next
        if head not in nodes:
            nodes.add(head)
        else:
            return 1
    return 0


# TO-DO : tortoise and the hare algorithm
"""
explaination:
we create two pointers called the tortoise and the hare. In every loop
tortoise moves by one node and the hare moves by two nodes. If they overlap 
it means that there is a loop in the linked list. If the hare gets to a node
with None value it means there is no loop.
"""
def tortoise_hare(head):
    tortoise = head
    hare = head.next
    while True:
        if tortoise == hare:
            return 1
        if hare is None or hare.next is None:
            return 0

        tortoise = tortoise.next
        hare = hare.next.next


print(tortoise_hare(nodes[0]))

"""
start1 = timer()
val1 = hasCycle_set(nodes[0])
end1 = timer()
print(timedelta(seconds=end1-start1))

start2 = timer()
val2 = hasCycle_dict(nodes[0])
end2 = timer()
print(timedelta(seconds=end2-start2))
"""