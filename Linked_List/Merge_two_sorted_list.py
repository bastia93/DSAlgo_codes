"""
Merge two sorted linked lists, A and B, and return it as a new list.

The new list should be made by splicing together the nodes
 of the first two lists and should also be sorted.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(A, B):
    if A is None or B is None:
        if A is None:
            return B
        else:
            return A
    else:
        head = Node(-1)
        curr = head
        A_pointer = A
        B_pointer = B

        while A_pointer and B_pointer:
            if A_pointer.val < B_pointer.val:
                curr.next = A_pointer
                curr = curr.next
                A_pointer = A_pointer.next
            else:
                curr.next = B_pointer
                curr = curr.next
                B_pointer = B_pointer.next

        if A_pointer is None:
            curr.next = B_pointer
        else:
            curr.next = A_pointer

        return head.next


def generate_linked_list(arr):
    head = None
    curr = None
    for i in arr:
        if head is None:
            head = Node(i)
            curr = head
        else:
            curr.next = Node(i)
            curr = curr.next
    return head


arr_A = [1, 5, 7, 9]
arr_B = [2, 4, 6, 10]

head_A = generate_linked_list(arr_A)
head_B = generate_linked_list(arr_B)

head = solve(head_A, head_B)

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

