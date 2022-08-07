"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Input: root of below tree
              5
             / \
            1   5
           / \   \
          5   5   5
Output: 4
There are 4 subtrees with single values.


Input: root of below tree
              5
             / \
            4   5
           / \   \
          4   4   5
Output: 5
There are five subtrees with single values.

"""

# Post order traversal
# for each node find if childrens are unival or not
# keep a checker True for unival and flase for not unival.
# if unival unival at the node = left_univel + right_unival + 1
#   if unival at the current node make checker = true
# if left_value anf right_value are equal with the node then it is true
# return unival_count , checker, value of the node

# if checker = False
# unival = left_univel + right_unival

class Node:
    def __init__(self, node):
        self.val = node
        self.right = None
        self.left = None

def is_unival(left_val, right_val, node_val):
    if left_val == node_val and right_val == node_val:
        return True
    else:
        return False

def unival(node):
    if node.left == None:
        left_checker = True
        left_val = node.val
        left_unival = 0
    else:
        left_checker, left_val, left_unival = unival(node.left)


    if node.right == None:
        right_checker = True
        right_val = node.val
        right_unival = 0
    else:
        right_checker, right_val, right_unival = unival(node.right)

    checker = False
    if right_checker and left_checker:
        checker = is_unival(left_val= left_val, right_val= right_val, node_val= node.val)

    if checker:
        number_unival = left_unival + right_unival + 1
        return True, node.val, number_unival
    else:
        return False, node.val , left_unival + right_unival


A = Node(5)
A.left = Node(1)
A.left.left = Node(5)
A.left.right = Node(5)
A.right = Node(5)
A.right.right = Node(5)

check, val, number = unival(A)

print(number)
