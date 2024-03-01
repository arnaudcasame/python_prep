from typing import Optional


def diameterOfBinaryTree(root: Optional[int]) -> int:

    

    return dfs(root, 0)

def dfs(root, result) -> int:
    if not root:
        return -1
    
    left = dfs(root.left, result)
    right = dfs(root.right, result)

    result[0] = max(result[0], left + right + 2)

    return -1 + max(left, right)