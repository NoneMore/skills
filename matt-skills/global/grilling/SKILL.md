---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it. A decision may have more than one prerequisite; the tree is the conversational shape, while prerequisites determine when a question is ready.

Work the tree in **logical rounds**. The **frontier** is every unsettled decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one logical round.

Before presenting a round, dependency-check its questions against each other. They must be **mutually independent**. If answering one question could change whether another should be asked, what it means, which answers are valid, or what you would recommend, they are not parallel: ask the upstream question first and leave the downstream question for a later round. Questions may share already-settled ancestors; they must not depend on another question that is still open in the same round. Never batch a parent with its child or descendant merely to reduce turns.

Prefer the harness's native structured question tool when one is available (for example, an `ask_question`-style tool). Treat each frontier node as a separate structured question, use finite choices when the decision naturally has them, preserve clear question identifiers, and include your recommended answer. If the harness limits how many questions or choices fit in one tool call, split the same frontier across multiple calls; those calls are still one logical round, and no downstream question may advance until the whole frontier has been answered. If no structured question tool is available, fall back to plain text.

Format a plain-text round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Then wait for the user's answers before advancing the tree.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier before every new round rather than carrying forward questions drafted under assumptions the user may just have changed.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
