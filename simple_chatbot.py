# ============================================================
#  simple_chatbot.py  –  Rule-Based Chatbot (Internship v1.0)
#  Author  : [KHATRI ISHA]
#  Project : White-Box AI Internship Demo
#  Why     : Zero hallucination, full traceability (input → logic → output)
# ============================================================

def get_response(user_input: str) -> str:
    """
    Core rule engine.
    Every branch is explicit → fully traceable → safe for regulated domains.
    """

    # ── normalise: strip whitespace, lowercase ──────────────────────────────
    text = user_input.strip().lower()

    # ── 1. GREETINGS ─────────────────────────────────────────────────────────
    if text in ["hi", "hello", "hey", "howdy", "good morning", "good evening"]:
        return "Hello! 👋  I'm your rule-based assistant. How can I help you today?"

    # ── 2. HOW ARE YOU ───────────────────────────────────────────────────────
    elif text in ["how are you", "how are you?", "how r u", "you okay?"]:
        return "I'm just code, but I'm running perfectly! 😄 What can I do for you?"

    # ── 3. NAME ENQUIRY ──────────────────────────────────────────────────────
    elif "your name" in text or "who are you" in text:
        return "I'm RuleBot — a simple rule-based chatbot with no hidden magic!"

    # ── 4. HELP ──────────────────────────────────────────────────────────────
    elif text in ["help", "help me", "what can you do", "options"]:
        return (
            "I can respond to:\n"
            "  • Greetings        → hi / hello / hey\n"
            "  • Status check     → how are you?\n"
            "  • Identity         → what is your name?\n"
            "  • Jokes            → tell me a joke\n"
            "  • Current time     → what time is it?\n"
            "  • Farewell         → bye / exit / quit\n"
            "  • Help             → help"
        )

    # ── 5. JOKES ─────────────────────────────────────────────────────────────
    elif "joke" in text:
        return (
            "Why do programmers prefer dark mode?\n"
            "Because light attracts bugs! 🐛"
        )

    # ── 6. TIME (uses Python stdlib — still deterministic) ───────────────────
    elif "time" in text or "what time" in text:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current local time is {now}."

    # ── 7. DATE ──────────────────────────────────────────────────────────────
    elif "date" in text or "today" in text:
        from datetime import date
        today = date.today().strftime("%A, %d %B %Y")
        return f"Today is {today}."

    # ── 8. THANKS ────────────────────────────────────────────────────────────
    elif text in ["thanks", "thank you", "thx", "ty"]:
        return "You're welcome! 😊"

    # ── 9. EXIT COMMANDS ─────────────────────────────────────────────────────
    elif text in ["bye", "goodbye", "exit", "quit", "q", "close"]:
        return "__EXIT__"          # sentinel — main loop watches for this

    # ── 10. FALLBACK (no hallucination — honest about limits) ────────────────
    else:
        return (
            f"Sorry, I don't have a rule for '{user_input}'. "
            "Type 'help' to see what I understand."
        )


# ── MAIN LOOP ────────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  RuleBot — Rule-Based Chatbot  |  type 'help' to start")
    print("=" * 55)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Session ended.")
            break

        if not user_input:          # ignore blank lines
            continue

        response = get_response(user_input)

        if response == "__EXIT__":
            print("Bot: Goodbye! 👋  Have a great day!")
            break

        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
