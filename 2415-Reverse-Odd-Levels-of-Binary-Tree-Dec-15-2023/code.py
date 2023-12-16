# Link: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        list = []
        flatTree = []
        list.append(root)
        while i < len(list):
            for n in list:
                flatTree.append(n)
                if n.left:
                    list.append(n.left)
                    list.append(n.right)
                list.pop(0)
        r = 0
        node = root
        while node.left:
            r += 1
            node = node.left

        for i in range(0, r):
            if i % 2 == 1:
                start = 2**i - 1
                end = 2**(i+1) - 1
                flatTree[start:end] = flatTree[start:end][::-1]

        for i in range(0, len(flatTree)):
            if 2*i+1 < len(flatTree):
                flatTree[i].left = flatTree[2*i+1]
                flatTree[i].right = flatTree[2*i+2]
            else:
                flatTree[i].left = None
                flatTree[i].right = None
        
        return flatTree[0]

# rewrite
class Solution(object):
    def reverseOddLevels(self, root):
        # how many rows?
        r = 0
        node = root
        while node.left:
            r += 1
            node = node.left

        # store all nodes in a list
        flatTree = []
        flatTree.append(root)
        for i in range(0, 2**(r+1)-2):
            flatTree.append(flatTree[i].left)
            flatTree.append(flatTree[i].right)

        # re-order
        for i in range(0, r+1):
            if i % 2 == 1:
                start = 2**i - 1
                end = 2**(i+1) - 1
                flatTree[start:end] = flatTree[start:end][::-1]

        # re-build the tree
        for i in range(0, len(flatTree)):
            if 2*i+1 < len(flatTree):
                flatTree[i].left = flatTree[2*i+1]
                flatTree[i].right = flatTree[2*i+2]
            # else:
            #     flatTree[i].left = None
            #     flatTree[i].right = None
        
        return flatTree[0]
