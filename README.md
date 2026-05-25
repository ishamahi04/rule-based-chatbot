# rule-based-chatbot

A simple rule-based chatbot built in Python — Internship Project 01.

## What it does

Responds to predefined user inputs using `if-elif-else` logic inside a continuous loop. No external libraries, no ML model — fully transparent and auditable.

## Why rule-based? (White Box AI)

| Property | Benefit |
|---|---|
| Traceability | Every input maps to exactly one output path |
| Zero hallucination | Responses are hardcoded strings — nothing is inferred |
| Compliance-ready | Auditors can read every rule in 5 minutes |

## Project structure

```
rule-based-chatbot/
│
├── simple_chatbot.py     # Main chatbot script
└── README.md             # This file
```

## File details

| File | Format | Purpose |
|---|---|---|
| `simple_chatbot.py` | `.py` | Core chatbot logic — run this |
| `README.md` | `.md` | Project documentation |

## How to run

```bash
# No install needed — pure Python stdlib
python simple_chatbot.py
```

Tested on Python 3.8+.

## Supported commands

| You type | Bot replies |
|---|---|
| `hi` / `hello` / `hey` | Greeting |
| `how are you` | Status |
| `what is your name` | Identity |
| `help` | Lists all commands |
| `tell me a joke` | Programmer joke |
| `what time is it` | Current local time |
| `today's date` | Today's date |
| `thanks` | Acknowledgement |
| `bye` / `quit` / `exit` | Ends the session |
| *anything else* | Honest fallback message |

## Key concepts demonstrated

- Control flow (`if / elif / else`)
- String normalization (`.strip().lower()`)
- Infinite loop with clean exit (`while True` + `break`)
- Sentinel value pattern (`__EXIT__`)
- Separation of logic (`get_response`) from I/O (`main`)

## Skills practised

`Python basics` · `Control flow` · `Decision-making logic` · `White-box AI` · `CLI applications`

---

*Part of internship project series — built with Python 3, zero dependencies.*
