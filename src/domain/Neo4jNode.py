
class Neo4jNode:
    labels = []
    properties = dict()

    def __init__(self, node, name):
        self.node = node
        self.name = name
