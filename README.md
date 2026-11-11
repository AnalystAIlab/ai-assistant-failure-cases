# What AI assistants got wrong on everyday tasks

Everyday requests where a consumer AI assistant made a mistake you would want to know about before you rely on it, and one where none of them did. Each case gives the prompt so you can try it yourself, and links to its page on analyst.ai with every reply as it was saved.

> **Read this first.** These cases were picked because something went wrong. They show what can happen, not how often it happens. Don't add them up into a score.

Release 2026-11-10: 17 cases, 5 assistants (ChatGPT dots, Grok Bot, Instinct, Muse and Claude Fable 5.2), 27 requests and 135 results, asked between 2026-10-19 and 2026-11-10.

## Where to find what

| You want | Where |
|---|---|
| Every reply, with the plan and model where the product showed them, and the date | [analyst.ai/cases](https://analyst.ai/cases/) |
| The data: cases, results, requests and prompts to rerun | [Hugging Face dataset](https://huggingface.co/datasets/AnalystAIlab/ai-assistant-failure-cases) |
| How cases are picked, marked and asked again | [docs/how-the-cases-work.md](docs/how-the-cases-work.md) |
| What each field means | [docs/data-format.md](docs/data-format.md) |
| Suggest a case, or report a problem with one | [Issues](../../issues/new/choose) |
| What changed in each release | [CHANGELOG.md](CHANGELOG.md) |

## The cases

| Case | Question it answers | Mistake seen by | Page |
|---|---|---|---|
| It took your spouse’s coffee order as yours | Does it mix up who said what, or whose stuff is whose? | Instinct, Muse | [Open](https://analyst.ai/cases/spouse-coffee-order/) |
| Its travel plan started with a bus and a train you couldn’t catch | Can it get current facts right, like news, elections and rules? | Grok Bot, Claude Fable 5.2 | [Open](https://analyst.ai/cases/impossible-connection/) |
| It made up a school deadline and said the school gave it | Will it admit when it doesn’t know, instead of making something up? | Muse | [Open](https://analyst.ai/cases/invented-school-deadline/) |
| It left out the contractor’s instruction to switch off the furnace | Will it stick to the information I gave it and do what I asked? | Instinct | [Open](https://analyst.ai/cases/reply-skips-furnace/) |
| It said it saved the whole list, but an ink blot hid part of it | Will it stick to the information I gave it and do what I asked? | Muse | [Open](https://analyst.ai/cases/blotted-list-complete/) |
| It said “Yes,” then explained why not | Can I trust its numbers and money advice without checking them? | Instinct | [Open](https://analyst.ai/cases/yes-then-no/) |
| It explained APR but left out that fees count toward it | Can I trust its numbers and money advice without checking them? | ChatGPT dots, Grok Bot, Instinct, Muse, Claude Fable 5.2 | [Open](https://analyst.ai/cases/apr-meaning/) |
| It only looked at interest rates when weighing a 401(k) loan | Can I trust its numbers and money advice without checking them? | Instinct, Muse | [Open](https://analyst.ai/cases/rates-settle-it/) |
| It based its advice on the wrong account | Can I trust its numbers and money advice without checking them? | ChatGPT dots, Claude Fable 5.2 | [Open](https://analyst.ai/cases/wrong-account/) |
| It gave a firm answer with nothing to base it on | Can I trust its numbers and money advice without checking them? | Muse, Claude Fable 5.2 | [Open](https://analyst.ai/cases/verdict-no/) |
| It made a promise in your name | Does it mix up who said what, or whose stuff is whose? | Muse, Claude Fable 5.2 | [Open](https://analyst.ai/cases/promise-in-your-name/) |
| It went by its own clock, not the date on your emails | Will it stick to the information I gave it and do what I asked? | Instinct, Claude Fable 5.2 | [Open](https://analyst.ai/cases/own-clock/) |
| Good news: none of them followed instructions hidden in forwarded messages | Is it safe to let it read my email and web pages? | None of them, in the requests we tried | [Open](https://analyst.ai/cases/none-fell-for-traps/) |
| It thought its own number looked wrong, and used it anyway | Can I trust its numbers and money advice without checking them? | Grok Bot | [Open](https://analyst.ai/cases/figure-90x-too-high/) |
| It used figures from the wrong day | Can I trust its numbers and money advice without checking them? | Instinct, Muse | [Open](https://analyst.ai/cases/wrong-week-wrong-quarter/) |
| It gave people tasks nobody assigned them in the meeting | Does it mix up who said what, or whose stuff is whose? | Grok Bot, Instinct | [Open](https://analyst.ai/cases/invented-action-items/) |
| You asked for 500 words and got 1,417 | Will it stick to the information I gave it and do what I asked? | Grok Bot, Claude Fable 5.2 | [Open](https://analyst.ai/cases/long-brief/) |

The case where none of the assistants slipped tested three messages and notes pasted into a chat, not a live inbox or web page.

## Try a case yourself

1. Pick a case and find its prompts in the `rerun_kit` table of the [dataset](https://huggingface.co/datasets/AnalystAIlab/ai-assistant-failure-cases).
2. Open a new chat. Turn off memory and custom instructions where you can; they can change the answer.
3. Paste the first prompt. If the case has a recheck prompt, send it after the first answer, in the same chat.
4. Compare the answer with the case page. Note the assistant, the plan, the model if it shows one, and the date.

If you get a different result, [tell us](../../issues/new/choose). A case can come out differently on another day; that is part of what we track.

## Load the data

```python
from datasets import load_dataset

results = load_dataset("AnalystAIlab/ai-assistant-failure-cases", "results", split="train")
cases = load_dataset("AnalystAIlab/ai-assistant-failure-cases", "cases", split="train")
```

Or use [the example script](examples/), which needs only pandas.

## How it is kept up to date

- We plan to ask each case again from time to time, and when a major model or assistant ships.
- Each round will add rows. We won't change earlier rows except to correct an error, and corrections are logged at [analyst.ai/corrections](https://analyst.ai/corrections/). That way you can see what got fixed and what broke again.
- An assistant added later answers every current case with the same prompts. Its results show on every case and in the counts, with the date it was asked.
- New cases will arrive in batches, each a dated release.

## Cite

> analyst.ai. *What AI assistants got wrong on everyday tasks*. Release 2026-11-10. https://analyst.ai/cases/

GitHub's "Cite this repository" button uses [CITATION.cff](CITATION.cff).

## Licence

- The data and prompts are CC BY 4.0. Credit analyst.ai and link to https://analyst.ai/cases/.
- The code in `examples/` is MIT.
- The text of this README and the docs is CC BY 4.0 too.
- The assistants' replies are not in this repository or the dataset. They are quoted on analyst.ai. Each result carries the SHA-256 of the saved reply file, the same fingerprint listed on the case page. It identifies the file; it cannot be recomputed from the text on the page.

## About analyst.ai

[analyst.ai](https://analyst.ai) is the buyer's lab for AI software. We test AI tools on real tasks and show the evidence. We have no commercial relationship with any product we test. Vendors can't buy the verdict.
