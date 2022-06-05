from application.create_neo4j_connection import create_neo4j_connection
from domain.model.Neo4jNode import Neo4jNode


def create_neo4j_node(neo4j_node: Neo4jNode):

    query_labels = [neo4j_node.node]
    query_labels.extend(neo4j_node.labels)
    query_labels = ':'.join(query_labels)

    properties = {'name': neo4j_node.name}
    properties = {**properties, **neo4j_node.properties}
    query_properties = ', '.join('{0}: ${0}'.format(n) for n in properties)

    cx = create_neo4j_connection()
    query = f"CREATE (n:{query_labels} {{ {query_properties} }})"
    return cx.execute_transaction(lambda tx: tx.run(query, **properties))


