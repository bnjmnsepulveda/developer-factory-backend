from shared.client.neo4j_connection import Neo4jConnection


def create_neo4j_connection():
    return Neo4jConnection('bolt://localhost:7687', 'neo4j', '1234')
