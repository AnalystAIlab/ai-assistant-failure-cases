"""Load Humanity's First Exam, the analyst.ai assistant cases, with pandas only.

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

# A case series: each question's first answer, one column per assistant.
questions = pd.read_json(BASE + "series_questions.jsonl", lines=True)
series = pd.read_json(BASE + "series_results.jsonl", lines=True)
grid = series.pivot_table(index=["series_id", "question_number"], columns="assistant", values="first_answer", aggfunc="first")
grid = grid.join(questions.set_index(["series_id", "question_number"])["question"])
print(grid.to_string())

# To rerun question 1: paste its prompt, then send the check after the first answer.
q = questions[questions["question_number"] == 1].iloc[0]
print(q["text"])
print(q["follow_up_text"])
print("Right answer:", q["right_answer"])
