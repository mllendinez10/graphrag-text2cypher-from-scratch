# graphrag-text2cypher-from-scratch

This project focuses on learning how GraphRAG works using Text2Cypher as the retrieval method, by building the complete pipeline from scratch in Python.

It intentionally avoids higher level frameworks, so each step can be implemented and understood independently.

As a practical use case, the project uses connected Hilti product data stored in a Neo4j knowledge graph and allows users to ask questions in natural language, which are translated into Cypher queries and used to retrieve the relevant information from the graph.

## Project Goal

The goal is to gain hands-on experience with the main components of a GraphRAG system using Text2Cypher retrieval:

* Structured data and graph schema preparation
* Data import into Neo4j
* Prompt construction using the graph schema and user question
* Cypher query generation with an LLM
* Query execution against Neo4j
* Query result processing
* LLM answer generation
* Evaluation against a golden set
* UI development with Streamlit

## Technology Stack

| **Area**         | **Technology** |
| ---------------------- | -------------------- |
| Programming language   | Python               |
| Structured data source | Excel                |
| Graph schema           | JSON                 |
| Excel processing       | Pandas with openpyxl |
| Graph database         | Neo4j                |
| Query language         | Cypher               |
| Retrieval method       | Text2Cypher          |
| LLM                    | Qwen3 4B via Ollama  |
| UI                     | Streamlit            |

## Project Structure

```
graphrag-text2cypher-from-scratch/
├── data/
│   ├── schema.json
│   └── data.xlsx
├── evaluation/
│   └── golden_set.json
├── src/
│   ├── app.py
│   ├── build_answer_prompt.py
│   ├── build_cypher_prompt.py
│   ├── evaluation.py
│   ├── execute_cypher.py
│   ├── generate_answer.py
│   ├── generate_cypher.py
│   ├── import_data_neo4j.py
│   ├── main.py
│   └── test_neo4j_connection.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## File Purpose

| File                     | Purpose                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| import_data_neo4j.py     | Imports the Excel data into Neo4j as nodes, properties, and relationships                   |
| test_neo4j_connection.py | Checks the connection to Neo4j                                                              |
| build_cypher_prompt.py   | Builds the Cypher generation prompt using the graph schema and user question                |
| generate_cypher.py       | Sends the prompt to Qwen3 via Ollama and generates the Cypher query                         |
| execute_cypher.py        | Executes the generated Cypher query against Neo4j and returns the results                   |
| build_answer_prompt.py   | Builds the answer prompt using the question, Cypher query, query results, and graph schema  |
| generate_answer.py       | Sends the answer prompt to Qwen3 via Ollama and generates the final natural language answer |
| evaluation.py            | Evaluates Text2Cypher answer accuracy against the golden set                               |
| main.py                  | Connects and runs the individual steps of the pipeline                                      |
| app.py                   | Provides the Streamlit user interface                                                       |

## Evaluation Results

The GraphRAG pipeline using Text2Cypher retrieval is evaluated using the questions in golden_set.json.

Each golden set entry contains:

* A natural language question
* A difficulty level: easy, medium, or hard
* The expected answer content

The evaluation script runs every question through the complete pipeline and checks whether all expected answer content is present in the generated answer. A question is counted as correct only if all expected content is present. Questions that cause pipeline errors are counted as incorrect.

The evaluation results are:

* Easy: 8/9 correct
* Medium: 2/3 correct
* Hard: 0/2 correct

## Project Takeaways

The main insights gained from building and evaluating this GraphRAG pipeline with Text2Cypher retrieval are:

* A clear graph schema, including relationship directions, property descriptions, and units, helps the LLM generate appropriate Cypher queries.
* Prompt instructions can guide Cypher generation, but they do not guarantee correct queries.
* Answer accuracy is more meaningful than comparing generated Cypher strings because different queries can return the same correct result.
* Local LLM inference can be the main performance bottleneck, while Cypher query execution is typically fast for this dataset.
* A golden set is essential for identifying the strengths and weaknesses of the system.
* In this evaluation, the pipeline performs well on easy and medium questions but struggles with hard questions involving multiple nodes and relationships.

I initially expected the graph approach to perform better than the relational approach in [text-to-sql-from-scratch](https://github.com/mllendinez10/text-to-sql-from-scratch), because relationship names seemed closer to how users phrase their questions.
However, both approaches depend on the LLM generating the correct query, and both struggled with questions requiring more complex combinations of data with SQL joins or graph traversals. A meaningful graph model helps describe the data, but does not by itself guarantee reliable query generation.
