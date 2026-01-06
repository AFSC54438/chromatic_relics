# -------------------------------------------------------------------
# 3) (a) (i)
class Node:
    def __init__(self, data):
        self.NodeData = data  # Integer
        self.LeftNode = None  # Node
        self.RightNode = None  # Node

    # ---------------------------------------------------------------
    # 3) (a) (ii)
    def GetLeft(self):
        return self.LeftNode

    def GetRight(self):
        return self.RightNode

    def GetData(self):
        return self.NodeData

    # ---------------------------------------------------------------
    # 3) (a) (iii)
    def SetLeft(self, left):
        self.LeftNode = left

    def SetRight(self, right):
        self.RightNode = right

    # ---------------------------------------------------------------

# -------------------------------------------------------------------
# 3) (c) (i)
class Tree:
    def __init__(self, first):
        self.FirstNode = first  # Node

    # ---------------------------------------------------------------
    # 3) (c) (ii)
    def GetRootNode(self):
        return self.FirstNode

    # ---------------------------------------------------------------
    # 3) (c) (iii)
    def Insert(self, new_node):
        current_node = self.FirstNode

        while True:
            if new_node.GetData() > current_node.GetData():
                next_node = current_node.GetRight()
                if next_node is None:
                    current_node.SetRight(new_node)
                    break
                else:
                    current_node = next_node
                    continue

            elif new_node.GetData() < current_node.GetData():
                next_node = current_node.GetLeft()
                if next_node is None:
                    current_node.SetLeft(new_node)
                    break
                else:
                    current_node = next_node
                    continue
    # ---------------------------------------------------------------

# -------------------------------------------------------------------
# 3) (d)
def OutputInOrder(node):
    left = node.GetLeft()
    if left is not None:
        OutputInOrder(left)

    print(node.GetData())

    right = node.GetRight()
    if right is not None:
        OutputInOrder(right)


# -------------------------------------------------------------------
# 3) (b)
node1 = Node(data=10)
node2 = Node(data=20)
node3 = Node(data=5)
node4 = Node(data=15)
node5 = Node(data=7)

# -------------------------------------------------------------------
# 3) (e) (i)

this_tree = Tree(first=node1)
this_tree.Insert(node2)
this_tree.Insert(node3)
this_tree.Insert(node4)
this_tree.Insert(node5)

OutputInOrder(node1)
# -------------------------------------------------------------------
