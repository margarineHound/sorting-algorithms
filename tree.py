class Node:
    def __init__(self, key, parent =  None):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None
        self.height = 0
        return


class Tree:
    def __init__(self, key):
        self.root = Node(key)
        self.depth = 0
        self.items = 0

    def traverse(self, node: Node = None):
        if node == None:
            node = self.root
        if node.left == None and node.right == None:
            print(f"key: {node.key} height: {node.height}")
            return
        if node.left:
            self.traverse(node.left)

        print(f"key: {node.key} height: {node.height}")
        if node.right:
            self.traverse(node.right)
        return

    def insert(self, key, node = None):
        if node == None:
            node = self.root

        if self.root == None:
            self.root = Node(key)
            self.depth = 1
            return

        print(f"valye: {key} current node: {node.key}")
        if node.key == key:
            print('value exists')
            return

        if key < node.key:
            if node.left:
                print("going left")
                node.height += 1
                return self.insert(key, node.left)
            else:
                print('added left')
                newNode = Node(key=key, parent=node)
                node.height += 1
                node.left = newNode
                return
        else:
            if node.right:
                print("going right")
                node.height += 1
                return self.insert(key, node.right)
            else:
                print("added right")
                newNode = Node(key=key, parent=node)
                node.right = newNode
                node.height += 1
                return

        print('ended')
        return


if __name__== "__main__":
    print("here")
    mytree = Tree(9)
    mytree.insert(7)
    mytree.insert(6)
    mytree.insert(8)
    mytree.insert(4)
    mytree.insert(5)

    print("middle")
    mytree.insert(5)
    mytree.insert(10)
    mytree.insert(11)
    mytree.insert(15)
    mytree.insert(15)
    mytree.insert(15)
    mytree.traverse()
    print("end")