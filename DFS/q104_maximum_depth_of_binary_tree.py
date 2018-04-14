# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def insert_left_child(self, new_node_value):
        # 当前节点没有左孩子时，直接添加新节点作为该节点的左孩子
        if not self.left:
            self.left = TreeNode(new_node_value)
            return
        # 当前节点有左孩子时，在当前节点的左孩子后代中继续寻找，直到找到没有左孩子的节点
        else:
            self.left.insert_left_child(new_node_value)

    def insert_right_child(self, new_node_value):
        if not self.right:
            self.right = TreeNode(new_node_value)
            return
        else:
            self.right.insert_right_child(new_node_value)

    def build_tree(self, a_list, i):
        if i < len(a_list) and a_list[i]:
            root = TreeNode(a_list[i])
            root.left = self.build_tree(a_list, 2 * i + 1)
            root.right = self.build_tree(a_list, 2 * i + 2)
            return root


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.max_depth_helper(root, 0)

    def max_depth_helper(self, root, result):
        if root:
            left = self.max_depth_helper(root.left, result + 1)
            right = self.max_depth_helper(root.right, result + 1)
            return left if left > right else right
        else:
            return result


def main():
    solution = Solution()
    # root = TreeNode(3)
    # root.insert_left_child(9)
    # root.insert_right_child(20)
    # root.right.insert_left_child(15)
    # root.insert_right_child(7)
    node_list = [3, 9, 20, "", "", 15, 7]
    root = TreeNode()
    root = root.build_tree(node_list, 0)
    print(solution.maxDepth(root))


main()

