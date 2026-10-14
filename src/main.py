"""
Run the Text-to-Cypher pipeline by connecting the individual processing steps.
"""

from build_cypher_prompt import build_cypher_prompt
from generate_cypher import generate_cypher
from execute_cypher import execute_cypher
from build_answer_prompt import build_answer_prompt
from generate_answer import generate_answer


question = input("Ask a question: ")

cypher_prompt = build_cypher_prompt(question)
cypher_query = generate_cypher(cypher_prompt)
query_result = execute_cypher(cypher_query)
answer_prompt = build_answer_prompt(question, cypher_query, query_result)
answer = generate_answer(answer_prompt)


print(answer)

