"""
A linked list A is given such that each node contains
 an additional random pointer which could point to any node
 in the list or NULL.

Return a deep copy of the list.

"""


class RandomListNode:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


def solve(head):
    # generating identical node
    curr = head
    # print("hello")

    while curr:
        temp_node = RandomListNode(curr.label)
        temp_node.next = curr.next
        curr.next = temp_node
        curr = temp_node.next
        # print("hello")

    # point to the random copied node
    original = head
    copy = head.next

    while original.next.next:
        if original.random:
            copy.random = original.random.next

        original = original.next.next
        copy = copy.next.next
        # print("hello")
    copy.random = original.random.next

    # detaching the nodes
    head_to_return = head.next
    original = head
    copy = head.next

    while original.next.next:
        original.next = original.next.next
        copy.next = copy.next.next

        original = original.next
        copy = copy.next

    original.next = None
    copy.next = None

    return head_to_return


first = RandomListNode(1)
second = RandomListNode(2)
third = RandomListNode(3)
first.next = second
first.random = third
second.next = third
second.random = first
third.random = first

get_head = solve(first)

curr = get_head
while curr:
    print(curr.label, curr.random.label)
    curr = curr.next


