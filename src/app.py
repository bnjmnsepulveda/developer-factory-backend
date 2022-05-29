from application.create_neo4j_node import create_neo4j_node
from domain.Neo4jNode import Neo4jNode
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def server():
    return 'Neo4j-maintainer app'


@app.route('/neo4j/node', methods=['POST'])
def create_neo4j_node_request():
    json = request.get_json()
    print(json)
    neo4j_node = Neo4jNode.from_dict(json)
    create_neo4j_node(neo4j_node)
    return "OK"


if __name__ == '__main__':
    app.run()

