from application.create_neo4j_connection import create_neo4j_connection


def get_neo4j_node():
    query = 'MATCH (n) RETURN collect(DISTINCT n.name)'
    cx = create_neo4j_connection()
    return cx.execute_transaction(lambda tx: tx.run(query))
