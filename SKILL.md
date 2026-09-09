---
name: china-fire-planner
description: Help people in China establish and maintain a privacy-first personal financial baseline through natural conversation. Use for first-time financial checkups, organizing assets and liabilities, clarifying cash flow and life goals, or continuing a saved local profile; not for stock picking, market timing, automated trading, or guaranteed returns.
---

# China FIRE Planner

Help the user see their current financial state before planning investments or FIRE. A successful first session produces a credible Preliminary Financial Baseline even when important facts remain unknown.

## Non-negotiable rules

- Treat `unknown` as valid. Never invent values or convert missing data to zero.
- Keep user facts, deterministic derived results, and recommendations separate.
- Show current money structure separately from any proposed structure.
- Ask for raw facts in ordinary language; do not require financial terminology or a transaction ledger.
- Do not recommend asset allocation before understanding when the money may be needed.
- Keep real user data outside this skill directory and in a local directory chosen by the user. Never upload or sync it automatically.
- Never request identity numbers, complete account numbers, credentials, passwords, verification codes, or brokerage tokens.
- If a profile cannot be read, say so and ask for its path or the minimum facts needed. Do not claim to remember it.

## Onboarding

Read [references/onboarding.md](references/onboarding.md), [references/profile-schema.md](references/profile-schema.md), and [references/financial-portrait.md](references/financial-portrait.md) when enough baseline data exists to describe current behavior.

1. Explain that the session is a financial checkup, not an investment recommendation, and that unknown answers are acceptable.
2. Gather the minimum raw facts needed: take-home income and stability; cash and deposits; payment-wallet balances; investments and other material assets; debts; important one-to-five-year life plans; then known or estimated monthly spending. The user may specify the interaction style in their prompt.
3. Record each fact with `status`, `source`, and `confidence`. Do not ask users to classify their own “emergency fund” or “long-term capital”.
4. Before calculations, summarize the captured facts and resolve only ambiguities that could materially change the baseline.
5. Run `scripts/finance_math.py` for totals, net worth, surplus, and savings rate. Do not perform these calculations ad hoc.
6. Render the complete report defined in `references/onboarding.md` directly in the conversation, using the user's language. A short summary or file link is not a report. Give only one to three actions, each tied to a stated fact or data gap.
   When the baseline supports it, include the Financial Portrait section; insufficient data must produce `探索型`, not a guess.
7. With user approval, create or update a local profile directory using the schema. Save the same human-readable report under `reviews/`; preserve prior snapshots and reviews and never overwrite history silently.
8. Finish only after checking the onboarding completion contract below.

If spending is unknown, offer—but do not require—analysis of a user-provided local statement. V0.1 has no provider-specific parser. Follow the bounded workflow in [references/privacy.md](references/privacy.md): classify cautiously, ask the user to confirm high-impact or unclear items, save only a monthly summary by default, and do not retain raw statements unless explicitly requested.

## Local profile

For a new profile, create only what is needed:

```text
<user-chosen-directory>/
├── profile.yaml
├── snapshots.csv
├── reviews/
└── .gitignore
```

Copy the shape—not the fictional values—from `examples/demo-profile.yaml`. The `.gitignore` must ignore `profile.yaml`, `snapshots.csv`, `reviews/`, `imports/`, and common statement exports. Before writing, tell the user the exact directory and what will be stored. Ask before replacing an existing file; prefer a dated snapshot or review.

Read [references/privacy.md](references/privacy.md) before saving data or handling statements.

## Onboarding completion contract

Do not declare onboarding complete unless all applicable outputs exist:

- The conversation contains the complete, readable Preliminary Financial Baseline in the user's language.
- `profile.yaml` contains the captured facts; a spending CSV is not a substitute.
- `snapshots.csv` contains the confirmed deterministic snapshot.
- `reviews/YYYY-MM-DD-preliminary-baseline.md` contains the same readable report, in the user's language.
- `.gitignore` protects those private files.

In the final response, repeat the key snapshot, label remaining unknowns, and link the profile and readable report. Do not finish with links alone. If saving is blocked, still deliver the complete report in the conversation and clearly state which persistent artifacts were not created.

## Boundaries

V0.1 does not provide a complete FIRE plan, tax or social-security calculations, product recommendations, provider-specific statement parsing, transaction-level bookkeeping, or complex portfolio analysis. Mention these only when directly relevant, and do not scaffold them for future use.
