# Privacy and Local Data

- Store real data only in a directory the user identifies and approves. Never place it in the skill directory.
- Before writing, show the exact target path, files, and whether the operation creates, appends, or replaces data.
- Do not upload, sync, commit, or transmit financial data without a separate explicit request.
- Never request or retain passwords, verification codes, identity numbers, complete account numbers, or access tokens.
- Use labels such as “工资卡” instead of bank account numbers. Avoid real names, employer names, addresses, and other unnecessary identifiers.
- Create a `.gitignore` that excludes profile data, reviews, imports, and statement files. Warn that `.gitignore` does not protect files already committed.

## Optional statement interface

V0.1 may inspect a local CSV/XLSX supplied by the user when the environment can read it, but has no provider-specific parser. First identify columns and coverage; then classify consumption, transfers, own-account movements, investment purchases/redemptions, credit-card repayment, income, reimbursement, refunds, and unknown items.

Never treat every negative transaction as spending. Present a preliminary summary and ask the user to confirm unclear or high-impact items. Only confirmed summaries may enter the profile with `source: user_confirmed`. By default save a monthly aggregate summary, not the raw statement or transaction rows. If the format cannot be interpreted reliably, stop and ask for a simpler export or a user-provided monthly estimate.
