# Minimal Financial Profile Schema

Use YAML for the current profile, CSV for append-only monthly snapshots, and Markdown for dated reviews. Do not create a transaction ledger by default.

## Value state

Every financial value has this shape:

```yaml
value: 8000
status: estimated
source: user
confidence: medium
as_of: 2026-09-09
```

- `status`: `known`, `estimated`, or `unknown`.
- `source`: `user`, `user_confirmed`, `imported_statement`, `agent_classified`, or `calculated`.
- `confidence`: `high`, `medium`, or `low`; use `null` when status is `unknown`.
- `value`: non-negative number, or `null` only when status is `unknown`.

`known` means explicitly supplied or confirmed, not objectively exact. Use `estimated` for ranges, approximations, stale balances, or incomplete statement coverage.

## Profile

```yaml
schema_version: "0.1"
base_currency: CNY
baseline:
  state: preliminary
  created_at: 2026-09-09
  updated_at: 2026-09-09
income:
  monthly_take_home: {value: 8000, status: estimated, source: user, confidence: medium, as_of: 2026-09-09}
assets:
  status: estimated
  items: []
liabilities:
  status: known
  items: []
spending:
  monthly_total: {value: null, status: unknown, source: null, confidence: null, as_of: null}
goals: []
```

Each asset or liability item has `id`, `label`, `category`, `amount`, and optional `notes`. IDs are stable lowercase identifiers. A known empty liabilities list means the user confirmed no current liabilities; an unknown collection must not be treated as zero.

Goals contain only user facts: `id`, `name`, optional `target_date`, optional `target_amount`, `status`, `source`, and `confidence`. Do not store Agent advice as a goal fact.

## Separation

- `profile.yaml`: user facts and user-confirmed classifications only.
- `snapshots.csv`: deterministic monthly results: `period,assets_total,liabilities_total,net_worth,income,spending,surplus,savings_rate,baseline_state,data_quality`.
- `reviews/YYYY-MM-DD-初步财务基线.md` for Chinese onboarding, or an equivalent user-language filename: the complete readable report, with derived interpretation and recommendations clearly labeled.

Do not write derived totals back into fact fields. Append a snapshot only after the user confirms the underlying facts. Never revise a prior row silently; append a corrected row with an ISO timestamp if correction support becomes necessary.

## Baseline state

`preliminary` is valid when a useful asset/liability picture exists but spending or another key input is unknown. Move to `established` only after assets and liabilities have been reviewed, income is usable, at least one month of spending is known or estimated, and the user has completed one review. Record the transition date; do not infer it from elapsed time.
