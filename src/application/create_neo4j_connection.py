from shared.client.neo4j_connection import Neo4jConnection
from shared.config import NEO4J_CONFIG


def create_neo4j_connection():
    return Neo4jConnection(
        NEO4J_CONFIG['uri'],
        NEO4J_CONFIG['user'],
        NEO4J_CONFIG['pass']
    )
