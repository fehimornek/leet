from timeit import default_timer as timer
from datetime import timedelta

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

nodes = [ListNode(i) for i in range(1000000)]
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


start1 = timer()
val1 = hasCycle_set(nodes[0])
end1 = timer()
print(timedelta(seconds=end1-start1))

start2 = timer()
val2 = hasCycle_dict(nodes[0])
end2 = timer()
print(timedelta(seconds=end2-start2))