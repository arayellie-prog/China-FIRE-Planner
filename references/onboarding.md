# Onboarding and Preliminary Baseline

## Input handling

Use the interaction style requested by the user. If they ask for a natural, gradual conversation, follow that preference; if they provide a structured batch of facts, process it directly. Do not add a separate onboarding persona or scripted conversational policy. In all styles, accept estimates and “不知道”, avoid inventing precision, and never ask the user to calculate emergency funds, surplus, savings rate, or long-term capital.

Collect only the minimum missing facts needed for a useful baseline. A preliminary baseline may be produced with unknown spending or unknown goal details.

## Report delivery

Write the full report in the conversation before or alongside saving it. Match the user's language for headings, labels, explanations, filenames, and recommendations. Keep schema keys in English only where machine readability requires them.

For a Chinese conversation, title the report `初步财务基线报告` and save it as `reviews/YYYY-MM-DD-初步财务基线.md`. Do not create an ad-hoc expense CSV in place of `profile.yaml` and `snapshots.csv`.

The report is a user-facing explanation, not an audit dump. Start with a short plain-language portrait based on evidence, such as “目前看，你属于高储蓄型” or “目前还不能判断储蓄能力，因为月支出未知”. Do not label a person “月光族” unless the data actually supports spending at or above income, and frame it as a current pattern rather than a character judgment. Use warm, spoken Chinese when the user speaks Chinese.

For proportions, use lightweight text visuals instead of requiring a chart tool:

```text
资产结构（约 ¥57,500）
基金/投资   ¥36,000  62.6%  ████████████
现金/存款   ¥21,500  37.4%  ███████
```

Only show a proportion when the relevant total is known or estimated from complete components. Clearly label estimates. Keep the report layered: first the plain-language summary and Financial Portrait, then the financial snapshot, then money structure visualization, then goals, risks, and actions.

When enough baseline data exists, insert the Financial Portrait after the opening summary. Read [financial-portrait.md](financial-portrait.md). It is a formal product feature describing current financial behavior, not a psychological test.

## Report

```markdown
# 初步财务基线报告 — YYYY-MM-DD

## 先说结论
- 你现在属于：高储蓄型 / 收支接近平衡 / 目前无法判断（选择有事实依据的一项）
- 用大白话说：用一两句话解释收入、支出、结余和当前状态。
- 你做得比较好的地方：
- 现在最需要看清的地方：

## 数据状态
- 已知：
- 估算：
- 未知：

## 财务快照
- 总资产：
- 总负债：
- 净资产：
- 月收入：
- 月支出：
- 月结余：
- 储蓄率：

## 资产结构（文字可视化）
- 用横向条形图展示资产类别及占比；没有可靠金额时写“暂时无法展示”。

## 当前资金结构
- 钱目前在哪里
- 哪些钱已有用户确认的用途
- 哪些钱用途尚未明确

## 重要人生目标
- 用户提出的目标、时间、金额及未知项

## 当前优势
- 判断——因为[具体事实]

## 当前风险或缺口
- 判断——因为[具体事实或缺失数据]

## 建议资金结构
- 日常资金 / 安全资金 / 有明确任务的钱 / 长期资金
- 未解决的金额标为待定，不得写成当前事实

## 接下来最重要的行动
1. 最多三项具体行动

## 假设与限制
- 哪些是估算、未知、计算结果或尚未评估
```

Display unavailable calculations as `Unknown — needs ...`, not `¥0`, `0%`, or a guessed range. A strength, risk, or action must cite at least one captured fact or data gap. Avoid generic praise and long advice lists.

Before finishing, verify that the report is understandable without opening YAML or CSV. In the final chat response, include the key numbers, unknowns, and next actions even when files were saved successfully.
