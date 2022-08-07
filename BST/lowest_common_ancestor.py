"""
Find the lowest common ancestor in an unordered binary tree A, given two values, B and C, in the tree.

Lowest common ancestor: the lowest common ancestor (LCA) of
two nodes v and w in a tree or directed acyclic graph (DAG) is
the lowest (i.e., deepest) node that has both v and w as descendants.

"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param A : root node of tree
# @param B : integer
# @param C : integer
# @return an integer
def lca(A, B, C, ans):
    if A == None:
        return [0, None]
    else:
        check_sum = 1 if A.val == B or A.val == C else 0
        if ans == None:
            left_sum, ans = lca(A.left, B, C, ans)
        if ans == None:
            right_sum, ans = lca(A.right, B, C, ans)

        check_sum = check_sum + left_sum + right_sum


        if check_sum == 2 and ans == None:
            ans = A.val

        return [check_sum, ans]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(lca(root, 2, 3, None))

