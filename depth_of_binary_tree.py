class BinaryTreeNode:
    left_node = None
    right_node = None

def get_depth(binary_tree_node, depth = 0):
    if binary_tree_node:
        depth += 1
    else:
        return depth
    return max(depth, get_depth(binary_tree_node.left_node, depth), get_depth(binary_tree_node.right_node, depth))

def build_tree(tree_length):
    binary_tree_nodeA = BinaryTreeNode()
    binary_tree_nodeB = BinaryTreeNode()
    binary_tree_nodeC = BinaryTreeNode()
    binary_tree_nodeD = BinaryTreeNode()
    binary_tree_nodeE = BinaryTreeNode()
    binary_tree_nodeF = BinaryTreeNode()
    binary_tree_nodeG = BinaryTreeNode()
    binary_tree_nodeH = BinaryTreeNode()
    binary_tree_nodeI = BinaryTreeNode()

    if tree_length == 5:
        binary_tree_nodeE.right_node = binary_tree_nodeF
        binary_tree_nodeC.right_node = binary_tree_nodeE
        binary_tree_nodeC.left_node = binary_tree_nodeD
        binary_tree_nodeB.right_node = binary_tree_nodeC
        binary_tree_nodeA.left_node = binary_tree_nodeB
    elif tree_length == 3:
        binary_tree_nodeB.right_node = binary_tree_nodeC
        binary_tree_nodeA.left_node = binary_tree_nodeB
    else:
        binary_tree_nodeH.left_node = binary_tree_nodeI
        binary_tree_nodeG.left_node = binary_tree_nodeH
        binary_tree_nodeD.right_node = binary_tree_nodeG
        binary_tree_nodeF.left_node = binary_tree_nodeD
        binary_tree_nodeE.right_node = binary_tree_nodeF
        binary_tree_nodeC.right_node = binary_tree_nodeE
        binary_tree_nodeB.right_node = binary_tree_nodeC
        binary_tree_nodeA.left_node = binary_tree_nodeB

    return binary_tree_nodeA


if __name__ == "__main__":

    print get_depth(build_tree(5)) == 5
    print get_depth(build_tree(3)) == 3
    print get_depth(build_tree("?")) == 9
