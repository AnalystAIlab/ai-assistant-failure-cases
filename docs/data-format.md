# Data format

The data lives in the [Hugging Face dataset](https://huggingface.co/datasets/AnalystAIlab/ai-assistant-failure-cases) as four JSON Lines tables. They join on `case_id` and `request_id`. This page describes release 2026-11-11.

## cases

One row per case.

| Field | Type | Meaning |
|---|---|---|
| `case_id` | string | Short name. The case page is `https://analyst.ai/cases/<case_id>/` |
| `title` | string | What happened, in one line |
| `question` | string | The reader question the case answers |
| `summary` | string | What the assistants did |
| `what_to_check` | string | What to look at yourself before acting on such an answer |
| `status` | string | `mistake_seen` if any assistant made the mistake in the latest round, otherwise `no_mistake_seen` |
| `mistake_seen_by` | list of strings | The assistants that made the mistake in the latest round |
| `assistants` | list of strings | The assistants asked |
| `first_seen` | date | First date the case was asked |
| `last_asked` | date | Most recent date it was asked |
| `rounds` | integer | How many rounds of asking the case has been through |
| `request_count` | integer | How many different requests make up the case |
| `rerun_setup` | string | `paste` (self-contained), `web` (needs web search) or `files` (attach the files in `inputs/<case_id>/`) |
| `how_to_rerun` | string | Short instructions |
| `page_url` | string | The case page |
| `source_reviews` | list of objects | The analyst.ai reviews the case came from: `title`, `url` |
| `release` | string | The release the row belongs to |

## results

One row per case, request and assistant in each round.

| Field | Type | Meaning |
|---|---|---|
| `case_id` | string | Joins to `cases` |
| `request_id` | string | Joins to `requests` |
| `how_it_was_asked` | string | For example "You pasted your notes into the chat" or "It searched your notes" |
| `round` | integer | 1 for the first round; each repeat adds a round |
| `assistant` | string | The product |
| `plan_and_model_shown` | string | The plan and model as the product showed them, from the source review's product list |
| `asked_on` | date | The date the request was sent |
| `outcome` | string | `mistake_seen`: the reply made the mistake the case describes. `no_mistake_seen`: it did not. `no_answer`: no reply arrived within the time allowed. `not_tested`: we could not test this request with this assistant |
| `note` | string or null | Anything that affects how to read the reply, such as a line our tester added when saving it |
| `reply_sha256` | list of strings | SHA-256 of each saved reply file, the fingerprint listed on the case page. A reply saved in parts has several; `no_answer` has none. It identifies the file; it cannot be recomputed from the page text |
| `follow_up_reply_sha256` | string or null | SHA-256 of the reply to the recheck, where one was sent |
| `page_url` | string | Where the reply is quoted in full |
| `source_review_url` | string | The review the request came from |
| `release` | string | The release the row belongs to |

An outcome is set by reading the saved reply against what the case describes, never by a score threshold. A few saved replies contain a line our tester added; the case page leaves those lines out and says so, and the SHA-256 is of the saved file as it is.

## requests

One row per request, as it was saved when sent. One request contains the placeholder `TEST_RECIPIENT_TEACHER` where an address would go; that is how it was sent.

| Field | Type | Meaning |
|---|---|---|
| `request_id` | string | `<case_id>-<n>` |
| `case_id` | string | Joins to `cases` |
| `how_it_was_asked` | string | As in `results` |
| `text` | string | The request |
| `sha256` | string | SHA-256 of `text` |
| `follow_up_text` | string or null | The recheck sent after the first answer, if any |
| `follow_up_sha256` | string or null | SHA-256 of `follow_up_text` |

Some requests refer to a connected inbox, notes library or spreadsheet that a plain chat doesn't have. For those, use the paste-ready prompts in `rerun_kit`.

## rerun_kit

One row per prompt to paste, in the order to send them.

| Field | Type | Meaning |
|---|---|---|
| `case_id` | string | Joins to `cases` |
| `order` | integer | Send in this order |
| `kind` | string | `paste-ready` (the material is inside the prompt), `as sent in our run` (may refer to a connected account), or `recheck` (send after the first answer, in the same chat) |
| `label` | string | What the prompt is |
| `setup` | string | As `rerun_setup` in `cases` |
| `text` | string | The prompt |
| `sha256` | string | SHA-256 of `text` |
| `inputs` | list of strings | Files to attach, relative to the dataset root |

Every prompt is a byte-for-byte copy of one sent in one of our reviews. Some paste-ready prompts come from a related review that asked the same question with the data pasted in; those were not used for the results in this release.

Lines such as `--- SUPPLIED S1 ---` inside a prompt mark where material was attached in the original run; they were part of what was sent.

## Stability

Field names and meanings stay the same within this format. If a field has to change, the release that changes it says so in the [changelog](../CHANGELOG.md).
