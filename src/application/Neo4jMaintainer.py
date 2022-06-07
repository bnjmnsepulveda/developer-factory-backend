from domain.model.Neo4jRelationship import Neo4jRelationship
from domain.service.Neo4jConnection import Neo4jConnection
from shared.config import NEO4J_CONFIG
from domain.model.Neo4jNode import Neo4jNode


def create_neo4j_connection():
    return Neo4jConnection(
        NEO4J_CONFIG['uri'],
        NEO4J_CONFIG['user'],
        NEO4J_CONFIG['pass']
    )


def write_on_neo4j(query):
    neo4j_connection = None
    try:
        neo4j_connection = create_neo4j_connection()
        return neo4j_connection.write(query)
    finally:
        if neo4j_connection is not None:
            neo4j_connection.close()


def read_from_neo4j(query):
    neo4j_connection = None
    try:
        neo4j_connection = create_neo4j_connection()
        return neo4j_connection.read(query)
    finally:
        if neo4j_connection is not None:
            neo4j_connection.close()


def create_neo4j_node(neo4j_node: Neo4jNode):

    query_labels = [neo4j_node.node]
    query_labels.extend(neo4j_node.labels)
    query_labels = ':'.join(query_labels)

    properties = {'name': neo4j_node.name}
    properties = {**properties, **neo4j_node.properties}
    query_properties = ', '.join('{0}: ${0}'.format(n) for n in properties)

    def create_node(tx):
        query = f"CREATE (n:{query_labels} {{ {query_properties} }}) RETURN n"
        tx.run(query, **properties)

    return write_on_neo4j(create_node)


def create_neo4j_relationship(neo4j_relationship: Neo4jRelationship):

    properties = {
        'nodeA': neo4j_relationship.node_a,
        'nodeB': neo4j_relationship.node_b
    }
    properties = {**properties, **neo4j_relationship.properties}
    query_properties = ', '.join('{0}: ${0}'.format(n) for n in neo4j_relationship.properties)

    def create_relationship(tx):
        query = f"""
            MATCH (na), (nb) 
               WHERE na.name = $nodeA AND nb.name = $nodeB 
            CREATE (na)-[r:{neo4j_relationship.name} {{ {query_properties} }}]->(nb) 
        """
        tx.run(query, **properties)

    return write_on_neo4j(create_relationship)


def get_neo4j_labels():

    def query(tx):
        return [row[0] for row in tx.run('call db.labels()')]

    return read_from_neo4j(query)


def get_neo4j_node_names():

    def query(tx):
        return [row['node_name'] for row in tx.run('MATCH (n) RETURN n.name AS node_name')]

    return read_from_neo4j(query)

