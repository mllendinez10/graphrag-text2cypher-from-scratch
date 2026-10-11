"""
Run the Text-to-Cypher pipeline by connecting the individual processing steps.
"""

from build_cypher_prompt import build_cypher_prompt
from generate_cypher import generate_cypher


question = input("Ask a question: ")

cypher_prompt = build_cypher_prompt(question)
cypher_query = generate_cypher(cypher_prompt)


print(cypher_query)

