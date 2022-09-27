def main():
    pass

class Node:
    def __init__(self, name: str, links: list, visited=False) -> None:
        self.name = name
        self.links = links
        self.visited = visited
    
class Link:
    def __init__(self, cost: int, nodes: Node) -> None:
        self.cost = cost
        self.nodes = nodes[2]


def DFStraversal(startNode: Node):
    # Process node
    #   -   -   -
    # Visit this node.
    startNode.Visited = True

    # Make a stack and put the start node in it.
    stack = list()
    stack.append(startNode)

    # Repeat as long as the stack isn´t empty
    while stack:
        # Get the next node from the stack.
        node = Node()
        node = stack.pop()
        # Process the node´s links.
        for link in node.links:
            # Use the link only if the destination
            # node hasn´t been visisted
            if not (link.nodes[1].Visited):
                # Mark the node as visited
                link.nodes[1].Visited = True
                # Push the node onto the stack.
                stack.append(link.nodes[1])
            # Continue processing the stack until empty

main()
