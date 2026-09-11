# Monthly Review

## Purpose

A monthly review is a short conversation about what changed in the user's life and money. It is not a form, bookkeeping session, personality test, or investment-performance report.

## Workflow

1. Read `profile.yaml`, all rows needed from `snapshots.csv`, and the latest relevant review.
2. Identify likely changes and open questions from history. Ask about life first: “这个月发生了什么？” Mention one relevant prior fact when helpful, such as an upcoming trip or an previously unknown expense.
3. Follow the user's answer naturally. Translate salary changes, bonuses, travel, moving, medical costs, purchases, debt repayment, goal changes, and account-balance changes into candidate facts. Ask one focused follow-up at a time only when it materially affects the review. `unknown` is valid.
4. Before calculation or saving, summarize what will change, what will stay unchanged, and what remains unknown. Ask for confirmation.
5. Calculate totals, cash-flow results, savings rate, and net-worth change with `scripts/finance_math.py`. Compare against prior snapshots only when periods and definitions are comparable.
6. Tell the story of the month first, using only a few key numbers as evidence. Then save after confirmation.

Do not ask the user to provide “月末资产”“目标变化” or similar schema labels unless they already use those terms. A statement like “这个月换了工作，空档两周，还去了一趟成都” is valid input; the Agent determines which fields may have changed.

## Evidence rules

- A larger account balance is not automatically saving; it may include market gains, transfers, refunds, or gifts.
- Separate cash-flow surplus from investment-value change when facts permit. Otherwise label the cause of net-worth change unknown.
- Do not carry forward a volatile balance as current without checking its date.
- Keep user facts, deterministic results, Agent interpretation, and recommendations in separate report sections.
- Never invent missing monthly spending or force the user to reconcile every yuan.

## Monthly life pattern

Create at most one short title that captures this month, not the person. The title is free-form Agent interpretation grounded in observed spending or events. Make it sound like a human remembering their month, not a meeting summary or category label. Keep it playful, humane, and non-judgmental; immediately explain the facts behind it. Confidence may be high, medium, or low.

Examples of tone—not templates or a taxonomy—include `🌻 热热闹闹生活的一个月`, `☀️ 比平时热闹一点的 8 月`, and `🏡✈️ 家人来了，也出去走了走`. Generate a title from the actual month. Never convert it into a persistent “财务人格” or “Financial Portrait”.

Major life events take priority over a cute title. If the evidence is thin, use a modest title such as `仍在探索月` or omit the pattern.

## Writing priorities

Apply the shared requirements in [user-facing-output.md](user-facing-output.md).

**Compress the stable, explain the unusual.** Recurring costs that stayed broadly normal—such as rent, connectivity, subscriptions, or an ordinary gym payment—should usually become one sentence: “固定生活开支基本稳定。” Do not list them line by line. Expand only changes that help explain why this month felt or cost different.

Lead with lived experience, not accounts or categories. The reader should understand within 30 seconds what happened and why spending was higher or lower. Use a few relevant numbers to support that story; do not turn salary, rent, utilities, meals, and every purchase into a ledger.

Use a small number of emojis as visual landmarks when they fit, such as `💰`, `🏡`, `✈️`, `📚`, or `🧭`. Do not decorate every heading or bullet.

Recommendations may contain zero to three actions. Do not invent chores or demand category tracking to appear useful. “暂时不用改变什么” is a valid evidence-based conclusion.

## Report

```markdown
# [根据真实生活生成的月度标题]

用两三句话讲清这个月过着怎样的生活，以及为什么花得更多、更少或差不多。先说人和事情，再说钱。

## 🏡 这个月的生活
- 围绕真正改变这个月的事件组织叙事。
- 将稳定的固定开支压缩成一句话；只展开异常变化。

## 💰 钱袋子速览
- 只选择帮助理解本月的关键数字，通常包括支出、结余以及必要的环比变化。
- 不要默认逐项展示所有指标或账目。
- 无法计算的重要项目写 Unknown 及原因。

## 值得注意的变化
- 解释“为什么”，并只做口径可比的变化。
- 无法区分储蓄与市场波动时明确说明。

## 🎯 目标有没有被影响
- 仅讨论已有目标或用户本月提出的新目标。

## 🧭 下个月
- 给出零至三项真正值得做的事；没有必要调整时直接说明。

## 说明
- 简短标明影响结论的估算、未知项或不可比口径。
- 月度标题属于 Agent interpretation，不是长期人格判断。
```

Save the report as `reviews/YYYY-MM-月度复盘.md` for Chinese. Append the confirmed deterministic row to `snapshots.csv`; do not add the monthly title, recommendations, or interpretation to the CSV.
