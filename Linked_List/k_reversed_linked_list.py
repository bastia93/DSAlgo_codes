"""
Given a singly linked list A and an integer B,
reverse the nodes of the list B at a time and return the modified linked list.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(start, end):
    end.next = None
    curr = start
    pre = None
    post = curr.next
    while post:
        curr.next = pre
        pre = curr
        curr = post

        post = post.next
    curr.next = pre
    return end, start


def solve(A, B):
    dummy_head = Node(-1)
    dummy_head.next = A
    back = dummy_head
    front = dummy_head.next
    start = dummy_head.next
    end = dummy_head

    while front:
        print("hello")
        for i in range(B):
            front = front.next
            end = end.next
        start, end = reverse(start, end)
        back.next = start
        end.next = front
        back = end
        start = front

    return dummy_head.next


def generate_linked_list(arr):
    dummy = Node(-1)
    curr =dummy

    for i in arr:
        temp = Node(i)
        curr.next = temp
        curr = curr.next

    return dummy.next


A = [8, 11, 13, 16, 18, 9]
head = generate_linked_list(A)

final_head = solve(head, 3)

curr = final_head
while curr:
    print(curr.val, end='->')
    curr = curr.next

