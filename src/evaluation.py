"""
Evaluate the answer accuracy of the Text-to-Cypher pipeline.

This script will:
- Load the evaluation questions from the golden set
- Run each question through the Text-to-Cypher pipeline
- Compare each generated answer with the expected answer content
- Calculate the answer accuracy for easy, medium, and hard questions
"""

import json

from main import run_pipeline

# ---------------------------------------------------------
# Load golden set
# ---------------------------------------------------------

# Open and store json file
with open("evaluation/golden_set.json", "r", encoding="utf-8") as file:
    golden_set = json.load(file)
    
# Test that document is loaded
print(f"the loaded file contains: {len(golden_set)} questions")


# --------------------------------------------------
# Result counters
# --------------------------------------------------

results = {
    "easy": {"correct": 0, "total": 0},
    "medium": {"correct": 0, "total": 0},
    "hard": {"correct": 0, "total": 0}
}


# ---------------------------------------------------------
# Run evaluation
# ---------------------------------------------------------

for test in golden_set:

    question = test["question"]
    difficulty = test["difficulty"].lower()
    expected_content = test["expected_answer_content"]
    
    # Run Text-to-Cypher pipeline. Includes error handling.
    try:
        answer = run_pipeline(question)
    except Exception as error:
        results[difficulty]["total"] += 1
        print(f"\nQuestion: {question}")
        print(f"Error: {error}")
        continue
    
    # Convert the expected content into a list
    expected_values = []

    for value in expected_content.values():

        if isinstance(value, list):
            expected_values.extend(value)
        else:
            expected_values.append(value)
            
    # Check if all expected values appear in the answer
    correct = all(
        str(value).lower() in answer.lower()
        for value in expected_values
    )

  # Update counters
    results[difficulty]["total"] += 1

    if correct:
        results[difficulty]["correct"] += 1
        

   # Test that the evaluation is in process
    print(f"\nQuestion: {question}")
    print(f"\nAnswer: {answer}")


# --------------------------------------------------
# Print final results
# --------------------------------------------------

print("\nEVALUATION RESULTS")

for difficulty, result in results.items():

    correct = result["correct"]
    total = result["total"]

    print(
        f"{difficulty.capitalize()}: "
        f"{correct}/{total} correct"
    )