# Monthly Review

## Purpose

A monthly review is a short conversation about what changed in the user's life and money. It is not a form, bookkeeping session, personality test, or investment-performance report.

## Workflow

1. Read `profile.yaml`, all rows needed from `snapshots.csv`, and the latest relevant review.
2. Identify likely changes and open questions from history. Ask about life first: “这个月发生了什么？” Mention one relevant prior fact when helpful, such as an upcoming trip or an previously unknown expense.
3. Follow the user's answer naturally. Translate salary changes, bonuses, travel, moving, medical costs, purchases, debt repayment, goal changes, and account-balance changes into candidate facts. Ask one focused follow-up at a time only when it materially affects the review. `unknown` is valid.
4. Before calculation or saving, summarize what will change, what will stay unchanged, and what remains unknown. Ask for confirmation.
5. Calculate totals, cash-flow results, savings rate, and net-worth change with `scripts/finance_math.py`. Compare against prior snapshots only when periods and definitions are comparable.
6. Explain the month in plain language, then save after confirmation.

Do not ask the user to provide “月末资产”“目标变化” or similar schema labels unless they already use those terms. A statement like “这个月换了工作，空档两周，还去了一趟成都” is valid input; the Agent determines which fields may have changed.

## Evidence rules

- A larger account balance is not automatically saving; it may include market gains, transfers, refunds, or gifts.
- Separate cash-flow surplus from investment-value change when facts permit. Otherwise label the cause of net-worth change unknown.
- Do not carry forward a volatile balance as current without checking its date.
- Keep user facts, deterministic results, Agent interpretation, and recommendations in separate report sections.
- Never invent missing monthly spending or force the user to reconcile every yuan.

## Monthly life pattern

Create at most one short title that captures this month, not the person. The title is free-form Agent interpretation grounded in observed spending or events. Keep it playful, humane, and non-judgmental; immediately explain the facts behind it. Confidence may be high, medium, or low.

These are style examples, not a taxonomy and not exhaustive: `稳稳攒钱月`, `目标冲刺月`, `人生体验月`, `过冬囤粮月`, `钱钱迷路月`, `计划赶不上变化月`, `大事落地月`, `仍在探索月`. Generate a better new title when the month calls for one. Never convert the title into a persistent “财务人格” or “Financial Portrait”.

Major life events take priority over a cute title. If the evidence is thin, use a modest title such as `仍在探索月` or omit the pattern.

## Report

```markdown
# 月度财务复盘 — YYYY-MM

## 这个月，一句话
- 月度标题：自由生成；证据不足时可省略
- 用大白话说明本月最重要的变化。

## 这个月发生了什么（用户事实）
- 只写已确认事实，并标明估算和未知。

## 数字发生了什么（确定性结果）
- 总资产 / 总负债 / 净资产
- 月收入 / 月支出 / 月结余 / 储蓄率
- 较上次净资产变化
- 无法计算的项目写 Unknown 及原因

## 和过去相比
- 只做口径可比的变化解释。
- 无法区分储蓄与市场波动时明确说明。

## 目标有没有被影响
- 仅讨论已有目标或用户本月提出的新目标。

## 下个月最值得做的事
1. 最多三项，分别引用本月事实或数据缺口。

## Agent 解读与限制
- 月度标题及解释属于 Agent interpretation，不是长期人格判断。
- 列出假设、未知项和可信度。
```

Save the report as `reviews/YYYY-MM-月度复盘.md` for Chinese. Append the confirmed deterministic row to `snapshots.csv`; do not add the monthly title, recommendations, or interpretation to the CSV.
