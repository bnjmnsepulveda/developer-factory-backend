# Developer Factory Backend

Mantenedor de nodos y relaciones para una base de datos Neo4j

## Requerimientos
* Python3
* Docker and docker compose

## Levantar Stack Developer Factory

para levantar tanto la base de datos de neo4j y el backend necesitas tener levantado el servicio de docker y docker compose y ejecutar lo siguiente:

```bash

# add permissions
chmod +x up-developer-factory-stack.sh
# run script
./up-developer-factory-stack.sh

```

Esto levantara los siguientes servicios

* developer-factory-backend: http://localhost:5000/apidocs
* neo4j admin app: http://localhost:7474/
* neo4j db bolt://localhost:7687

## Levantar Unicamente Developer Factory Backend

Crear una base de datos neo4j
```bash

# create neo4j database with docker
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/s3cr3t neo4j

```

Ejecutar el backend

```bash
# installing virtual environment for python 
python3 -m venv venv 
# activate virtual env
source venv/bin/activate
# install dependencies
pip install -r requirements.txt

# add permissions to script
chmod +x up-server.sh
# run script
./up-server.sh

```


