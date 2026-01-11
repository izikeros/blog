---
Title: Using MLflow-RAGAS Integration Without Tracing
Slug: using-mlflowragas-integration-without-tracing
Date: 2026-01-11
Modified: 2026-01-11
Status: published
Tags: mlflow, ragas, RAG-evaluation, rag-optimization, rag
Category: note
---

You can use MLflow's RAGAS integration to calculate evaluation scores and log them to experiments **without** implementing MLflow traces in your RAG pipeline. This is useful when:

- You have an existing RAG pipeline you don't want to modify
- You're doing batch evaluation of pre-computed results
- You want to quickly test RAGAS metrics without full instrumentation

## Option 1: Static Data Approach (Recommended)

Pre-compute your RAG outputs, then pass everything to `mlflow.genai.evaluate()` with the `outputs` field already populated.

```python
import mlflow
from mlflow.genai.scorers import Faithfulness, FactualCorrectness

# Your existing RAG pipeline (no MLflow code needed)
def my_rag_pipeline(question: str) -> tuple[str, list[str]]:
    """Your RAG implementation - completely unchanged."""
    contexts = my_retriever.retrieve(question)
    answer = my_llm.generate(question, contexts)
    return answer, contexts

# Golden dataset
golden_dataset = [
    {
        "question": "What is MLflow?",
        "ground_truth": "MLflow is an open-source platform for ML lifecycle management.",
        "contexts": ["MLflow is an open-source platform..."]  # Expected contexts
    },
    # ... more samples
]

# Step 1: Run your RAG pipeline and collect outputs
eval_data = []
for item in golden_dataset:
    answer, retrieved_contexts = my_rag_pipeline(item["question"])
    eval_data.append({
        "inputs": {
            "question": item["question"]
        },
        "outputs": {
            "response": answer,
            "retrieved_contexts": retrieved_contexts,  # Required for Faithfulness
        },
        "expectations": {
            "expected_answer": item["ground_truth"],
            "ground_truth": item.get("contexts", []),  # For ContextRecall
        },
    })

# Step 2: Run evaluation with static data (no predict_fn)
mlflow.set_experiment("rag-evaluation")

with mlflow.start_run(run_name="static-data-evaluation"):
    mlflow.log_param("evaluation_mode", "static_data")
    mlflow.log_param("num_samples", len(eval_data))
    results = mlflow.genai.evaluate(
        data=eval_data,  # Data already includes outputs
        scorers=[
            Faithfulness(model="openai:/gpt-4o-mini"),
            FactualCorrectness(model="openai:/gpt-4o-mini"),
        ],
    )
    print(f"Results logged to run: {mlflow.active_run().info.run_id}")
```

### Key Points

- **No `predict_fn` needed** - outputs are pre-computed
- **`retrieved_contexts` in outputs** - Required for Faithfulness metric to work
- **Your RAG code stays unchanged** - No decorators or MLflow imports needed in your pipeline

## Option 2: Simple predict_fn (No Tracing Decorator)

If you prefer the `predict_fn` approach but don't want tracing:

```python
def simple_rag_predict(question: str) -> dict:
    """Wrapper around your RAG - no @mlflow.trace decorator."""
    contexts = my_retriever.retrieve(question)
    answer = my_llm.generate(question, contexts)
    return {
        "response": answer,
        "retrieved_contexts": contexts,
    }

# Evaluation data without outputs (they'll be generated)
eval_data = [
    {
        "inputs": {"question": item["question"]},
        "expectations": {
            "expected_answer": item["ground_truth"],
            "ground_truth": item.get("contexts", []),
        },
    }
    for item in golden_dataset
]

with mlflow.start_run():
    results = mlflow.genai.evaluate(
        predict_fn=simple_rag_predict,
        data=eval_data,
        scorers=scorers,
    )
```

## Comparison: When to Use Each Approach

| Approach                                  | Tracing    | Faithfulness                                  | Best For                                    |
| ----------------------------------------- | ---------- | --------------------------------------------- | ------------------------------------------- |
| **Static data** (Option 1)                | Not needed | Works (needs `retrieved_contexts` in outputs) | Existing pipelines, batch evaluation, CI/CD |
| **predict_fn with @mlflow.trace**         | Required   | Works (reads from RETRIEVER spans)            | New pipelines, debugging, detailed traces   |
| **predict_fn without tracing** (Option 2) | Not needed | Works (needs `retrieved_contexts` in return)  | Quick integration, simple pipelines         |

## Complete Working Example

```python
"""
Complete example: Evaluate any RAG pipeline with RAGAS metrics in MLflow.
No tracing required in your RAG implementation.
"""

import mlflow
from mlflow.genai.scorers import Faithfulness, FactualCorrectness

# Configure MLflow
mlflow.set_tracking_uri("http://localhost:5000")  # Or your tracking server
mlflow.set_experiment("my-rag-evaluation")

# Your RAG pipeline (example - replace with your implementation)
class MyRAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def query(self, question: str) -> tuple[str, list[str]]:
        contexts = self.retriever.search(question, k=3)
        answer = self.llm.generate(
            f"Context: {contexts}\n\nQuestion: {question}\n\nAnswer:"
        )
        return answer, contexts

# Initialize your pipeline
rag = MyRAGPipeline(retriever=my_retriever, llm=my_llm)

# Your evaluation dataset
test_questions = [
    {"question": "What is X?", "ground_truth": "X is..."},
    {"question": "How does Y work?", "ground_truth": "Y works by..."},
]

# Build evaluation data with pre-computed outputs
eval_data = []
for item in test_questions:
    answer, contexts = rag.query(item["question"])
    eval_data.append({
        "inputs": {"question": item["question"]},
        "outputs": {
            "response": answer,
            "retrieved_contexts": contexts,
        },
        "expectations": {
            "expected_answer": item["ground_truth"],
        },
    })

# Run evaluation
with mlflow.start_run(run_name="rag-eval-no-tracing"):
    # Log your pipeline configuration
    mlflow.log_params({
        "retriever_k": 3,
        "llm_model": "gpt-4o-mini",
        "num_samples": len(eval_data),
    })
    # Evaluate with RAGAS scorers
    results = mlflow.genai.evaluate(
        data=eval_data,
        scorers=[
            Faithfulness(model="openai:/gpt-4o-mini"),
            FactualCorrectness(model="openai:/gpt-4o-mini"),
        ],
    )
    # Results are automatically logged to MLflow
    print("Evaluation complete!")
    print(f"View results: mlflow ui --port 5000")
    print(f"Run ID: {mlflow.active_run().info.run_id}")

# Access results programmatically
print(results.metrics)
print(results.tables["eval_results_table"])
```

## Recommendation

For existing RAG pipelines, use **Option 1 (Static Data)**:

1. **Minimal changes** - Your RAG code stays completely unchanged
2. **Batch-friendly** - Run your pipeline once, evaluate multiple times with different scorers
3. **CI/CD compatible** - Easy to integrate into automated testing pipelines
4. **Full metric support** - All RAGAS metrics work when you include `retrieved_contexts` in outputs

The only requirement is that your RAG pipeline returns both the answer and the retrieved contexts, which most RAG implementations already do.
