"""
Build a prompt from the graph schema and user question to generate a Cypher query.

"""

SCHEMA_FILE = "data/schema.json"


def build_cypher_prompt(question):
    
    # Read graph schema file as JSON text
    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        schema = file.read()


    # Prompt
    prompt = f"""
Generate Neo4j Cypher queries from natural language questions.

Instructions:
- Return only the Cypher query.
- Do not include explanations or Markdown code fences.
- Generate only a read only query.
- Do not create, update, or delete data.
- Use only the node labels, relationship types, and properties defined in the graph schema.
- Follow the relationship directions defined in the schema.
- Respect the units specified in the schema.
- Return information relevant to the user's question.
- Treat missing values as unknown, not as zero.
- For torque and resistance questions, match the configuration requested, including components and quantities where applicable.
- Return the specific properties needed to answer the question. Include item_number and designation when listing products.
- Maximum and minimum values:
    - Return all products tied at the highest or lowest value.
    - Use max() or min(), applying the same requested filters when calculating the value and finding matching products.
    - Use LIMIT only when the question requests a fixed number of results.
- Torque questions:
    - Follow (Connector)-[:HAS_TORQUE_CONFIGURATION]->(TorqueConfiguration).
    - Return connector designation, torque_id, torque, and bolt designation.
    - If a bolt is specified, use MATCH on HAS_BOLT and filter by its designation. Otherwise, use OPTIONAL MATCH to retain configurations without a specified bolt.
    - Only traverse ResistanceConfiguration if explicitly relevant to the question.
- Resistance questions:
    - Match all specified components within the same ResistanceConfiguration.
    - The main Connector links to the configuration through HAS_RESISTANCE_CONFIGURATION.
    - The configuration links to the installation Channel through USES_CHANNEL and to channel Connector nodes through USES_CHANNEL_CONNECTOR.
    - Return resistance_id, component designations, relevant quantities, and the requested resistance values or quantities.
    - Read channel connector quantities from the relationship: [usage:USES_CHANNEL_CONNECTOR] → usage.quantity. Do not count nodes.
    - Return all matching configurations.


Graph schema:
{schema}

User question:
{question}

Cypher query:
"""

    return prompt.strip()