from application.create_neo4j_node import create_neo4j_node
from domain.Neo4jNode import Neo4jNode

node = Neo4jNode('Language', 'Rust')
node.labels = ['backend', 'fullstack']
node.properties = {
    'priority': 'RECOMENDADO',
}
result = create_neo4j_node(node)

print(result)