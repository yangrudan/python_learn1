"""
Copyright (c) Cookie Yang. All right reserved.
"""
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # 插入节点
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    # 删除节点
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # 遍历
    def inorder_traversal(self):
        res = []
        self._inorder_traversal_recursive(self.root, res)
        return res

    def _inorder_traversal_recursive(self, node, res):
        if not node:
            return
        self._inorder_traversal_recursive(node.left, res)
        res.append(node.value)
        self._inorder_traversal_recursive(node.right, res)


def dfs_recursive(node):
    if not node:
        return
    print(node.value, end=" ")
    dfs_recursive(node.left)
    dfs_recursive(node.right)


def bfs(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


# 创建一个二叉树
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# 中序遍历
print("Inorder traversal:", tree.inorder_traversal())
print("Inorder traversal:", inorder_traversal(tree.root))

print("DFS (recursive):")
dfs_recursive(tree.root)
print()

print("BFS:")
bfs(tree.root)
print()


# 删除节点
tree.delete(3)
print("After deleting 3:", tree.inorder_traversal())
