"""
Generate a Cypher query from a natural language question.

The script will:
- Receive the prompt
- Send the prompt to the LLM
- Return the generated Cypher query

"""

import ollama

LLM_MODEL = "qwen3:4b"

def generate_cypher(cypher_prompt: str) -> str:

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": cypher_prompt + "\n/no_think"
            }
        ],
        # Disable thinking output
        think=False,
        options={
            # temperature=0 is more deterministic (no creativity)
            "temperature": 0
        }
    )

    cypher_query = response.message.content
    

    # Remove the LLM's thinking section, if present, and keep only the text after </think>. 
    if "</think>" in cypher_query:
        cypher_query = cypher_query.split("</think>", 1)[1]

    # Remove surrounding whitespace
    cypher_query = cypher_query.strip() 

    # Raise an error if no query remains
    if not cypher_query:
        raise ValueError("The model did not return a Cypher query.")


    return cypher_query