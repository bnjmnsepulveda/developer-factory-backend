
class Neo4jNode:

    labels = []
    properties = dict()

    def __init__(self, node, name):
        self.node = node
        self.name = name

    @staticmethod
    def from_dict(json):
        neo4j_node = Neo4jNode(node=json['node'], name=json['name'])
        if json.get('labels') is not None:
            neo4j_node.labels = json['labels']
        if json.get('properties') is not None:
            neo4j_node.properties = json['properties']
        return neo4j_node

    def __repr__(self):
        return f"Neo4jNode(name={self.name}, node={self.node}, labels={self.labels}, properties={self.properties})"
