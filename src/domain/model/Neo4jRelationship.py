
class Neo4jRelationship:

    properties = dict()

    def __init__(self, name, node_a, node_b):
        self.name = name
        self.node_a = node_a
        self.node_b = node_b

    @staticmethod
    def from_dict(value):
        relation = Neo4jRelationship(
            value['name'],
            value['node_a'],
            value['node_b']
        )
        if 'properties' in value:
            relation.properties = value['properties']
        return relation

    def __repr__(self):
        return f"Neo4jRelationship(name={self.name}, nodeA={self.node_a}, nodeB={self.node_b}, properties={self.properties})"
