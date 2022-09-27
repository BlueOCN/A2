"""
    Implementación de un árbol binario
    basado en el libro "Essential Algorithms" de Rod Stephens

    Hector E. Del Angel Z. A01039991
    Sarahí José Aguilar - A01705020
    Salvador Torres Rodríguez - A00825038
    Roberto Emmanuel González Muñoz A01376803

"""

from __future__ import annotations

def main():

    # Simplified
    tree = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
    print("%r Tree" % tree)
    # Build a tree with a list
    buildTree(tree)


class BinaryNode:

    def __init__(self, data=None, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def traversePreorder(self):
        """
            The algorithm processes a ´node´ followed by its ´left child´ 
            and then its ´right child´.
        """
        # Process node
        print(self.data, end=" ")
        if self.leftChild != None:
            self.leftChild.traversePreorder()
        if self.rightChild != None:
            self.rightChild.traversePreorder()

    def traverseInorder(self):
        """
            The algorithm processes a node's ´left child´,
            the ´node´, and then the node's ´right child´.
        """
        if self.leftChild != None:
            self.leftChild.traverseInorder()
        # Process node
        print(self.data, end=" ")
        if self.rightChild != None:
            self.rightChild.traverseInorder()

    def traversePostorder(self):
        """
            The algorithm processes a node's ´left child´,
            then its ´right child´, and then the ´node´.
        """
        if self.leftChild != None:
            self.leftChild.traverseInorder()
        if self.rightChild != None:
            self.rightChild.traverseInorder()
        # Process node
        print(self.data, end=" ")

    def traverseDepthFirst(self, root: BinaryNode):
        """
            The algorithm processes all the nodes at a given level
            of the tree in left-to-right order before processing 
            the nodes at the next level.
        """
        # Create a queue to hold children for later processing
        children = list()
        # Place the root node on the queue
        children.append(root)
        # Process the queue until it is empty
        while children:
            # Get the next node in the queue
            node = children.pop(0)
            # Process the node
            print(node.data, end=" ")
            # Add the node´s children to the queue
            if node.leftChild != None:
                children.append(node.leftChild)
            if node.rightChild != None:
                children.append(node.rightChild)

    def addNode(self, newData):
        """
        The algorithm compares the ´newData´ to the current ´node's data´. If the 
        ´newData´ is smaller than the ´node's data´, the algorithm should place the ´newData´
        in the left subtree. If the ´leftChild´ reference is ´None´, the algorithm gives 
        the current node a new ´leftChild´ node and places the ´newData´ there. If the ´leftChild´
        is not ´None´, the algorithm calls the child node's ´addNode´ method recursively
        to place the ´newData´ in the left subtree. If the ´newData´ is not smaller than the ´node's data´,
        the algorithm should place the ´newData´ in the right subtree. If the ´rightChild´ reference is ´None´,
        the algorithm gives the current ´node´ a new ´rightChild´ node and places the ´newData´ there.
        If the ´rightChild´ is not ´None´, the algorithm calls the child node's 
        ´addNode´ method recursively to place the ´newData´ in the right subtree.
        """
        if newData < self.data:
            if self.leftChild == None:
                self.leftChild = BinaryNode(newData)
            else:
                self.leftChild.addNode(newData)
        else:
            if self.rightChild == None:
                self.rightChild = BinaryNode(newData)
            else:
                self.rightChild.addNode(newData)

    def findNode(self, target):
        """
        First the algorithm checks the current ´node´'s ´data´. If that ´data´ equals the 
        target ´data´, the algorithm returns the current ´node´.
        Next, if the target ´data´ is less than the current ´node´'s ´data´, the desired ´node´ 
        lies in this ´node´'s left subtree. If the ´leftChild´ branch is ´None´, the algorithm 
        returns ´None´ to indicate that the target item isn't in the tree. If the ´leftChild´ 
        isn't  ´None´, the algorithm recursively calls the ´leftChild´'s ´findNode´ method to 
        search that subtree. If the target ´data´ is greater than the current ´node´'s ´data´,
        the algorithm performs similar steps to search the right subtree.
        """
        if target == self.data:
            return self
        if target < self.data:
            if self.leftChild == None:
                return None
            return self.leftChild.findNode(target)
        else:
            if self.rightChild == None:
                return None
            return self.rightChild.findNode(target)


    def graphTree(self, node: BinaryNode, level=0) -> None:
        if node is not None:
            self.graphTree(node.rightChild, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.data) + '\t\t')
            self.graphTree(node.leftChild, level + 1)


def buildTree(tree):
    if type(tree) == list:
        root = BinaryNode(tree[0])
        for node in tree[1:]:
            root.addNode(node)
        root.traversePreorder()
        print("Traverse Preorder")
        root.traverseInorder()
        print("Traverse Inorder")
        root.traversePostorder()
        print("Traverse Postorder")
        root.traverseDepthFirst(root)
        print("Traverse Depth First")

        # Graph the tree
        print("\nBinary Tree Representation", end='\n\n')
        root.graphTree(root)
        print('')
    else:
        print("Type not supported!")

main()
