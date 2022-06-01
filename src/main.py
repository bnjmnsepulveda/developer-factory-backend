from application.create_neo4j_node import create_neo4j_node
from domain.model.Neo4jNode import Neo4jNode
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def root():
    return {
        'app': 'Neo4j-maintainer app'
    }


@app.route("/neo4j/node", methods=['POST'])
def create_neo4j_node_request():
    body = request.get_json()
    print(body)
    neo4j_node = Neo4jNode.from_dict(body)
    result = create_neo4j_node(neo4j_node)
    print(f'Result: {result}')
    return {
        'message': 'OK'
    }


if __name__ == '__main__':
    app.run(debug=True)


