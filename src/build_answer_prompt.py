"""
Build the prompt used to generate the natural language answer from the query result.
"""

SCHEMA_FILE = "data/schema.json"


def build_answer_prompt(question, cypher_query, query_result):
    
    # Read the complete schema file for property descriptions and units
    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        schema = file.read()


    answer_prompt = f"""
/no_think

Use only the query results below to answer the question.

Rules:
- Give only the final answer, directly and concisely.
- Do not explain your reasoning or describe query execution.
- Do not invent information missing from the query results.
- Use the graph schema to interpret properties and their units.
- Include units for numerical values when defined in the schema.
- Treat missing values as unknown, not as zero.
- If multiple configurations are returned, distinguish them using the available component details and quantities.

If the query result is empty, respond exactly with:
"The information is not available in the database."

Question:
{question}

Cypher query:
{cypher_query}

Query results:
{query_result}

Graph schema:
{schema}

Answer:
"""

    return answer_prompt.strip()