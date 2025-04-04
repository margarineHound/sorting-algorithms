class Node:
    def __init__(self, key, parent =  None, size = 1):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None
        self.height = 0
        self.size = size
        self.min = key
        self.max = key
        self.sum = key
        return


class Tree:
    def __init__(self, key):
        self.root = Node(key)
        self.depth = 0
        self.items = 0

    def rebalance(self, node: Node):

        leftHeight = node.left.height
        rightHeight = node.left.height
        bf = leftHeight - rightHeight
        node.height = max(rightHeight, leftHeight) + 1
        if abs(bf)<= 1:
            return self.rebalance(node.parent)
        elif bf < -1:
            self.rightRotate()

        else:
            self.leftrotate(node.right)



    def rightRotate(self, node : Node ):

        y = node.left
        T3 = y.right

        parent = node.parent

        node.parent = y
        y.parent = parent
        y.right = node
        node.right = T3

        self.update_update(node)
        self.update_update(node.parent)
        return

    def leftRotate(self, node: Node):


        pass






    def update_update(self, node: Node):
        if node:

            node.height = 1 + max(node.left.height, node.right.height)

    def subtree_at(self,node, i):
        nl = self.size(node.left)
        if i < node:
            return self.subtree_at(node.left, i)
        elif i == nl:
            return nl
        else:
            return self.subtree_at(node.right, i-nl-1)

    def find_prev(self, node : Node, key =None) -> Node:
        if node.key == key:
            return node.parent

        if key < node.key:
            return self.find_prev (node.left, key)

        else:
            return self.find_prev (node.right, key)


    def fine_next(self, node : Node, key =None) -> Node:
        if node.key == key:
            return node.parent

        if key < node.key:
            return self.fine_next(node.left, key)

        else:
            return self.fine_next(node.right, key)


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
            # right += res

        # node.height = max(left,right)


    def insert(self, key, node = None):
        if node == None:
            node = self.root

        if self.root == None:
            self.root = Node(key)
            self.depth = 1

            return

        # print(f"valye: {key} current node: {node.key}")
        if node.key == key:
            print('value exists')
            return

        node.size += 1
        node.height +=1
        node.min = min(node.min, key )
        node.max = max(node.max, key)
        node.sum += key

        if key < node.key:

            if node.left:
                # print("going left")
                self.insert(key, node.left)
            else:
                # print('added left')
                newNode = Node(key=key, parent=node)
                node.left = newNode
        else:
            if node.right:
                # print("going right")
                self.insert(key, node.right)
            else:
                # print("added right")
                newNode = Node(key=key, parent=node)
                node.right = newNode

        # print('ended')
        return self.rebalance()




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
    mytree.update()
    mytree.update()
    mytree.traverse()
    print("end")