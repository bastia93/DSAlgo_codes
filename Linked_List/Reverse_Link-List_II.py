"""
Reverse a linked list A from position B to C.

NOTE: Do it in-place and in one-pass.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(start, end):
    left = start
    mid = start
    right = start.next
    left.next = None

    while right != end:
        mid = right
        right = right.next
        mid.next = left
        left = mid
    return


def solve(A, B, C):
    if B == C:
        return A
    else:
        pre_start = None
        post_end = A
        end = A

        for i in range(B-1):

            if pre_start is None:
                pre_start = A
            else:
                pre_start = pre_start.next

        if pre_start is None:
            start = A
        else:
            start = pre_start.next

        # print(pre_start.val)
        # print(start.val)

        for i in range(C-1):
            end = end.next
        post_end = end.next

        reverse(start, post_end)
        if pre_start is None:
            A = end
        else:
            pre_start.next = end
        start.next = post_end

    if B == 1:
        return end
    else:
        return A


arr = [1, 2, 3]
dummy_head = Node(9999)
tail = dummy_head
for i in arr:
    tail.next = Node(i)
    tail = tail.next
head = dummy_head.next

temp_head = solve(head, 2, 3)
#testing
curr = temp_head
while curr:
    print(curr.val)
    curr = curr.next
