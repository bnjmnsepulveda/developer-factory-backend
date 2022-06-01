
clear;

export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASS="1234"

cd src/ && gunicorn --reload -c server_config.py main:app
