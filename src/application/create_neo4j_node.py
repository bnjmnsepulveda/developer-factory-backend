from application.create_neo4j_connection import create_neo4j_connection
from domain.Neo4jNode import Neo4jNode


def create_neo4j_node(neo4j_node: Neo4jNode):

    cx = create_neo4j_connection()
    node_info = [neo4j_node.node]
    node_info.extend(neo4j_node.labels)
    node_info = ':'.join(node_info)

    properties = {
        'name': neo4j_node.name
    }
    properties = {**properties, **neo4j_node.properties}
    query_properties = ', '.join('{0}: ${0}'.format(n) for n in properties)

    query = f"CREATE (n:{node_info} {{ {query_properties} }})"
    print(query)

    result = cx.execute_transaction(lambda tx: tx.run(query, **properties))

    return result
