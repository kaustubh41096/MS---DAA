class Node:

    def __init__(self, data, color=None, parent=None):

        self.left = None
        self.right = None
        self.data = data
        self.color = color
        self.parent = parent

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, "red", self)
                    # if self.parent is not None:
                        # self.check_tree(self.left)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, "red", self)
                    if self.parent is not None:
                        self.check_tree(self.right)
                else:
                    self.right.insert(data)
            else:
                print("Data already present")
        else:
            self.data = data

    def search(self, data, depth):
        if data < self.data:
            if self.left:
                level = self.left.search(data, depth + 1)
                return level
            else:
                return -1
        elif data > self.data:
            if self.right:
                level = self.right.search(data, depth + 1)
                return level
            else:
                return -1
        else:
            return depth

    # Print the tree
    def print_tree(self):
        # print("printing node: " + str(self.data))
        if self.left:
            self.left.print_tree()
        print("[" + str(self.data) + "," + self.color + "]", end=' ')
        # print("\n")
        if self.right:
            self.right.print_tree()

    def check_uncle(self, node):
        if node.parent.parent is not None:
            if node.parent.parent.right:
                # check if parent is right child
                if node.parent.parent.right.data == node.parent.data:
                    # return color of parent's sibling
                    if node.parent.parent.left:
                        return node.parent.parent.left.color
                    else:
                        return None
                else:
                    # parent is left child
                    # return color of parent's sibling
                    if node.parent.parent.right:
                        return node.parent.parent.right.color
                    else:
                        return None
            else:
                # parent is left child
                # return color of parent's sibling
                if node.parent.parent.right:
                    return node.parent.parent.right.color
                else:
                    return None

    def ll_rotation(self, child_node, parent_node, grandparent_node):
        # Right rotate on grandparent
        print("ll case")
        temp_node = parent_node.right
        parent_node.parent = grandparent_node.parent
        if grandparent_node.parent:
            if grandparent_node.parent.left:
                if grandparent_node.parent.left.data == grandparent_node.data:
                    grandparent_node.parent.left = parent_node
                else:
                    grandparent_node.parent.right = parent_node
            else:
                grandparent_node.parent.right = parent_node
        parent_node.right = grandparent_node
        grandparent_node.parent = parent_node
        grandparent_node.left = temp_node
        if temp_node:
            temp_node.parent = grandparent_node
        # Swapping colors of parent and grandparent
        col = parent_node.color
        parent_node.color = grandparent_node.color
        grandparent_node.color = col

    def lr_rotation(self, child_node, parent_node, grandparent_node):
        # Left rotate parent
        print("lr case")
        temp_node = child_node.left
        child_node.parent = parent_node.parent
        if grandparent_node.left:
            if grandparent_node.left.data == parent_node.data:
                grandparent_node.left = child_node
            else:
                grandparent_node.right = child_node
        else:
            grandparent_node.right = child_node
        child_node.left = parent_node
        parent_node.parent = child_node
        parent_node.right = temp_node
        if temp_node:
            temp_node.parent = parent_node
        # Apply ll_rotation
        self.ll_rotation(parent_node, child_node, grandparent_node)

    def rr_rotation(self, child_node, parent_node, grandparent_node):
        # Mirror of ll_rotation
        print("rr case")
        temp_node = parent_node.left
        parent_node.parent = grandparent_node.parent
        if grandparent_node.parent:
            if grandparent_node.parent.left:
                if grandparent_node.parent.left.data == grandparent_node.data:
                    grandparent_node.parent.left = parent_node
                else:
                    grandparent_node.parent.right = parent_node
            else:
                grandparent_node.parent.right = parent_node
        parent_node.left = grandparent_node
        grandparent_node.parent = parent_node
        grandparent_node.right = temp_node
        if temp_node:
            temp_node.parent = grandparent_node
        # Swapping colors of parent ond grandparent
        col = parent_node.color
        parent_node.color = grandparent_node.color
        grandparent_node.color = col

    def rl_rotation(self, child_node, parent_node, grandparent_node):
        # Mirror of lr_rotation
        print("rl case")
        temp_node = child_node.right
        child_node.parent = parent_node.parent
        if grandparent_node.left:
            if grandparent_node.left.data == parent_node.data:
                grandparent_node.left = child_node
            else:
                grandparent_node.right = child_node
        else:
            grandparent_node.right = child_node
        child_node.right = parent_node
        parent_node.parent = child_node
        parent_node.left = temp_node
        if temp_node:
            temp_node.parent = parent_node
        # Apply rr_rotation
        self.rr_rotation(parent_node, child_node, grandparent_node)

    def recolor(self, child_node, parent_node, grandparent_node):
        print("recoloring")
        if grandparent_node.parent:
            if parent_node.data == grandparent_node.left.data:
                parent_node.color = "black"
                grandparent_node.right.color = "black"
                grandparent_node.color = "red"
            else:
                parent_node.color = "black"
                grandparent_node.left.color = "black"
                grandparent_node.color = "red"
        else:
            if parent_node.data == grandparent_node.left.data:
                parent_node.color = "black"
                grandparent_node.right.color = "black"
            else:
                parent_node.color = "black"
                grandparent_node.left.color = "black"

    def check_tree(self, node):
        # loop to iterate up the tree
        while node:
            if node.color == "red" and node.parent.color == "red":
                # case 2
                if self.check_uncle(node) == "black" or self.check_uncle(node) is None:  # case 2a
                    if node.parent.parent.left:
                        # check if parent is left child of grandparent
                        if node.parent.parent.left.data == node.parent.data:
                            # check node position
                            if node.parent.left:
                                # node is left child of parent
                                if node.parent.left.data == node.data:
                                    self.ll_rotation(node, node.parent, node.parent.parent)
                                    node = node.parent
                                else:
                                    # node is right child of parent
                                    self.lr_rotation(node, node.parent, node.parent.parent)
                                    node = node.parent
                            else:
                                # node is right child of parent
                                self.lr_rotation(node, node.parent, node.parent.parent)
                                node = node.parent
                        else:
                            # parent is right child
                            # check node position
                            if node.parent.left:
                                # node is left child of parent
                                if node.parent.left.data == node.data:
                                    self.rl_rotation(node, node.parent, node.parent.parent)
                                    node = node.parent
                                else:
                                    # node is right child of parent
                                    self.rr_rotation(node, node.parent, node.parent.parent)
                                    node = node.parent
                            else:
                                # node is right child of parent
                                self.rr_rotation(node, node.parent, node.parent.parent)
                                node = node.parent
                    else:
                        # parent is right child of grandparent
                        # check node position
                        if node.parent.left:
                            # node is left child of parent
                            if node.parent.left.data == node.data:
                                self.rl_rotation(node, node.parent, node.parent.parent)
                                node = node.parent
                            else:
                                self.rr_rotation(node, node.parent, node.parent.parent)
                                node = node.parent
                        else:
                            # node is right child of parent
                            self.rr_rotation(node, node.parent, node.parent.parent)
                            node = node.parent
                else:
                    # case 2b
                    self.recolor(node, node.parent, node.parent.parent)
                    node = node.parent
            else:
                node = node.parent


if __name__ == "__main__":
    print("Enter no of values to be inserted in tree :")
    c = input()
    for i in range(int(c)):
        print("\nEnter value :")
        val = input()
        if i == 0:
            root = Node(int(val), "black", None)
        else:
            while root.parent is not None:
                root = root.parent
            root.insert(int(val))
            while root.parent is not None:
                root = root.parent
            root.print_tree()
    print("\nSearching for 6 in rbtree")
    d = root.search(6, 1)
    print("\n6 found at depth " + str(d))
    # print("In-order traversal of bst is :")
    # print("Root of tree is : " + str(root.data))
    # root.print_tree()
