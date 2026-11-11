"""Load the analyst.ai assistant cases with pandas only.

    pip install pandas
    python examples/load_cases.py

The data is CC BY 4.0: credit analyst.ai and link to https://analyst.ai/cases/.
"""
import pandas as pd

BASE = "https://huggingface.co/datasets/AnalystAIlab/ai-assistant-failure-cases/resolve/main/data/"

cases = pd.read_json(BASE + "cases.jsonl", lines=True)
results = pd.read_json(BASE + "results.jsonl", lines=True)

# Which assistants made the mistake in each case, with the plan, model and date.
# These cases were picked because something went wrong: don't read the counts as failure rates.
seen = results[results["outcome"] == "mistake_seen"]
table = seen.merge(cases[["case_id", "title"]], on="case_id")
print(table[["title", "assistant", "plan_and_model_shown", "asked_on"]].to_string(index=False))
