"""
Execute a Cypher query against Neo4j and return the results.
"""

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

# Load connection settings from .env
load_dotenv(".env")


def execute_cypher(cypher_query):
    # Open the Neo4j connection
    with GraphDatabase.driver(
        os.environ["NEO4J_URI"],
        auth=(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"],
        ),
    ) as driver:

        # Normally you receive records (rows), summary (execution info) and keys (column names)
        # In this case we just want to records
        records,_,_ = driver.execute_query(
        cypher_query,
        database_=os.environ["NEO4J_DATABASE"],
        routing_="r",
        )

        query_result = records

    return query_result