# Onboarding and Preliminary Baseline

## Input handling

Use the interaction style requested by the user. If they ask for a natural, gradual conversation, follow that preference; if they provide a structured batch of facts, process it directly. Do not add a separate onboarding persona or scripted conversational policy. In all styles, accept estimates and “不知道”, avoid inventing precision, and never ask the user to calculate emergency funds, surplus, savings rate, or long-term capital.

Collect only the minimum missing facts needed for a useful baseline. A preliminary baseline may be produced with unknown spending or unknown goal details.

## Report delivery

Write the full report in the conversation before or alongside saving it. Match the user's language for headings, labels, explanations, filenames, and recommendations. Keep schema keys in English only where machine readability requires them.

For a Chinese conversation, title the report `初步财务基线报告` and save it as `reviews/YYYY-MM-DD-初步财务基线.md`. Do not create an ad-hoc expense CSV in place of `profile.yaml` and `snapshots.csv`.

The report is a user-facing explanation, not an audit dump. Read [user-facing-output.md](user-facing-output.md) and open with a warm, evidence-based description of how the user currently relates to money. Include one current financial portrait when evidence supports it; use `探索型` when it does not. This is not a psychological test or permanent identity.

Possible portrait language includes `老实人攒钱型` for steady accumulation, `想要就要型` for goal-driven saving, `人生是旷野型` for meaningful experience spending, `过冬仓鼠型` for a strong safety/liquidity preference, and `钱钱迷路型` when money exists but lacks clear jobs. These are style anchors, not a closed classifier. The Agent may write a better fitting, non-judgmental name. Explain every portrait with specific facts, include confidence, and never infer spending behavior from income alone.

For proportions, use lightweight text visuals instead of requiring a chart tool:

```text
资产结构（约 ¥57,500）
基金/投资   ¥36,000  62.6%  ████████████
现金/存款   ¥21,500  37.4%  ███████
```

Only show a proportion when the relevant total is known or estimated from complete components. Clearly label estimates. Keep the report layered around meaning: current portrait and life context first, then a compact money overview, goals, gaps, and actions.

## Report

```markdown
# [一个温暖、有生活感的 Baseline 标题] — YYYY-MM-DD

用两三句话讲清用户目前过着怎样的财务生活、钱主要在支持什么，以及最值得关注的事情。

## 🌱 你现在的财务画像
- 当前画像：[基于事实生成；证据不足时为探索型]
- 用口语解释这个名字，并列出一至三条事实依据。
- 画像可信度：高 / 中 / 低

## 💰 钱袋子速览
- 只展示帮助用户理解现状的关键数字；不要机械输出所有字段。
- 将 Known / Estimated / Unknown 融入对应数字或简短说明，不单独制造审计清单。

## 🧺 钱现在放在哪里
- 用简短叙述和必要的横向条形图说明资产结构。
- 解释结构意味着什么，不要只列账户和金额。

## 🧭 钱要带你去哪里
- 用用户的人生目标组织这一节，并说明当前资金与目标之间的关系。
- 只展开真正重要的优势、风险或未知，不做长清单。

## ✨ 接下来
- 零至三项真正必要的行动；若暂时无需改变，明确说出来。

## 说明
- 简短列出会影响结论的估算、未知和限制。
```

Display unavailable calculations as `Unknown — needs ...`, not `¥0`, `0%`, or a guessed range. A portrait, strength, risk, or action must cite at least one captured fact or data gap. Avoid generic praise, long advice lists, and section-by-section data dumps.

Before finishing, verify that the report is understandable without opening YAML or CSV. In the final chat response, include the key numbers, unknowns, and next actions even when files were saved successfully.
