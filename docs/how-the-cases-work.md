# How the cases work

## Where they come from

analyst.ai tests AI tools on everyday jobs: reading email, keeping notes, household money, investment research, looking things up. Each review asks the same requests of every product under the same conditions. Its findings are on [analyst.ai/reviews](https://analyst.ai/reviews/).

While doing that work we record the moments an assistant surprised us: a mistake with consequences, something invented, an instruction ignored. A case is one of those moments that anyone can rerun from a prompt. One case in this release is a good surprise: none of the assistants fell for instructions hidden in an email or a note.

## How a case is picked

- The mistake matters for an everyday job a person would hand to an assistant today.
- Anyone can rerun it from a prompt, either pasted into a chat or with web search or attached files.
- It is backed by saved replies and the review's own scoring record.

This makes the set a selection, not a sample. It shows what can happen, not how often.

## How a result is marked

Each result says whether the reply made the mistake the case describes. It is set by reading the saved reply against the case, with the review's scoring record beside it, never by a score threshold. Where a case was asked more than one way, each way has its own result.

Every result carries the assistant, the plan and model where the product showed them, and the date it was asked. Most consumer assistants don't show a model name, and some don't show a plan; the result says so.

## Repeats

We plan to ask each case again from time to time, and when a major model or assistant ships. A repeat will add a dated round to each case. Earlier rounds change only to correct an error, logged at [analyst.ai/corrections](https://analyst.ai/corrections/), so a case shows when a mistake was fixed and when it came back.

An assistant added later answers every current case with the same prompts and rules. Its results show on every case and in the counts, with the date it was asked.

## Suggesting a case

Send it through [an issue](../../../issues/new/choose). We accept cases about assistants and AI tools a person can buy and use today, on tasks we can run ourselves. Give a prompt someone else can paste, with made-up details only: no personal information.

Issues here are public. We test every suggestion before publishing it and write the published case ourselves, and we don't name the person who suggested it in what we publish.

## Corrections

If a case gets something wrong, [report it](../../../issues/new/choose) or use [analyst.ai/corrections](https://analyst.ai/corrections/). Corrections are logged with their date.

## Independence

We have no commercial relationship with any product we test. Vendors can't buy the verdict.
