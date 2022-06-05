from shared.client.Neo4jConnection import Neo4jConnection
from shared.config import NEO4J_CONFIG
from domain.model.Neo4jNode import Neo4jNode


def create_neo4j_connection():
    return Neo4jConnection(
        NEO4J_CONFIG['uri'],
        NEO4J_CONFIG['user'],
        NEO4J_CONFIG['pass']
    )


def create_neo4j_node(neo4j_node: Neo4jNode):

    query_labels = [neo4j_node.node]
    query_labels.extend(neo4j_node.labels)
    query_labels = ':'.join(query_labels)

    properties = {'name': neo4j_node.name}
    properties = {**properties, **neo4j_node.properties}
    query_properties = ', '.join('{0}: ${0}'.format(n) for n in properties)

    def create_node(tx):
        query = f"CREATE (n:{query_labels} {{ {query_properties} }})"
        tx.run(query)

    return create_neo4j_connection().write(lambda tx: tx.run(create_node, **properties))


def get_neo4j_labels():

    def query(tx):
        return [row[0] for row in tx.run('call db.labels()')]

    return create_neo4j_connection().read(query)


def get_neo4j_node_names():

    def query(tx):
        return [row['node_name'] for row in tx.run('MATCH (n) RETURN n.name AS node_name')]

    return create_neo4j_connection().read(query)

