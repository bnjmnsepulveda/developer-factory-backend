from neo4j import GraphDatabase


class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_transaction(self, query_operation, **kwargs):
        with self.driver.session() as session:
            return session.write_transaction(query_operation)

