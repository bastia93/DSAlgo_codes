


def post_order(node):
    if node.left is None and node.right is None:
        return [True, 1, node.val, node.val]
    else:
        if node.left is None:
            right_child = post_order(node.right)
            if right_child[0] and node.val < right_child[2]:
                return [True, 1 + right_child[1], node.val, right_child[3]]
            else:
                return [False, right_child[1], node.val, right_child[3]]

        elif node.right is None:
            left_child = post_order(node.left)
            if left_child[0] and left_child[3] <= node.val:
                return [True, 1 + left_child[1], left_child[2], node.val]
            else:
                return [False, left_child[1], left_child[2], node.val]
    
        else:
            left_child = post_order(node.left)
            right_child = post_order(node.right)
            if left_child[0] and right_child[0]:
                if left_child[3] <= node.val < right_child[2]:
                    return [True, 1+left_child[1]+right_child[1], left_child[2], right_child[3]]
                
            return [False, max(right_child[1], left_child[1]), left_child[2], right_child[3]]


def solve(A):
    ans = post_order(A)
    return ans[1]
