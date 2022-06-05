from neo4j import GraphDatabase


class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def write(self, query_operation, **kwargs):
        with self.driver.session() as session:
            return session.write_transaction(query_operation, **kwargs)

    def read(self, query_operation, **kwargs):
        with self.driver.session() as session:
            return session.read_transaction(query_operation, **kwargs)


