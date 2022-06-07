from application.Neo4jMaintainer import get_neo4j_labels, get_neo4j_node_names, create_neo4j_node, \
    create_neo4j_relationship
from domain.model.Neo4jNode import Neo4jNode
from flask import Flask, request
from flask_cors import CORS
from flasgger.utils import swag_from
from flasgger import Swagger

from domain.model.Neo4jRelationship import Neo4jRelationship

app = Flask(__name__)
CORS(app)
Swagger(app)


def response(data=None, message='OK', status=200):
    return {
        'data': data,
        'message': message,
        'status': status
    }


@app.route('/', methods=['GET'])
@swag_from('./../apidocs/root.yml')
def root():
    return response(data={
        'app': 'Neo4j-maintainer app'
    })


@app.route('/neo4j/node/name', methods=['GET'])
@swag_from('./../apidocs/neo4j-node-names.yml')
def get_neo4j_node_name_request():
    return response(data=get_neo4j_node_names())


@app.route('/neo4j/node/label', methods=['GET'])
@swag_from('./../apidocs/neo4j-node-labels.yml')
def get_neo4j_node_label_request():
    return response(data=get_neo4j_labels())


@app.route('/neo4j/node', methods=['POST'])
@swag_from('./../apidocs/create-neo4j-node.yml')
def create_neo4j_node_request():
    body = request.get_json()
    neo4j_node = Neo4jNode.from_dict(body)
    create_neo4j_node(neo4j_node)
    return response(
        status=201,
        message=f'Neo4j Node(={neo4j_node.name}) Created'
    )


@app.route("/neo4j/relationship", methods=['POST'])
@swag_from('./../apidocs/create-neo4j-relationship.yml')
def create_neo4j_relationship_request():
    body = request.get_json()
    neo4j_relationship = Neo4jRelationship.from_dict(body)
    create_neo4j_relationship(neo4j_relationship)
    return response(
        status=201,
        message=f'Neo4j Node(={neo4j_relationship.name}) Created)'
    )


if __name__ == '__main__':
    app.run(debug=True)


