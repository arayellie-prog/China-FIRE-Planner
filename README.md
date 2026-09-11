# China FIRE Planner

一个面向中国年轻人的隐私优先 Agent Skill：先帮你看清收入、支出、资产和目标，再逐步建立自己的财务基线。

V0.2 已包含 onboarding、本地 Financial Profile、确定性计算、中文可读报告，以及从生活变化出发的自然月度复盘。它不会连接银行或券商，不推荐具体证券，不预测市场，也不保证收益。

## 最快开始

如果你已经在使用 Codex，最简单的方法是在 Codex 的新任务中输入：

```text
使用 $skill-installer 从 https://github.com/arayellie-prog/China-FIRE-Planner 安装 china-fire-planner。
```

安装完成后，重新打开一个 Codex 任务，输入：

```text
使用 $china-fire-planner 帮我做第一次财务体检。

请用中文，像朋友聊天一样逐步问我，不要一次发问题清单。
最后生成一份口语化、容易读懂的报告，并保存我的本地财务档案。
```

## 这份说明适用于哪些平台

本项目的 Skill 文件采用 Agent Skills 的 Markdown 结构。当前仓库实际验证过：

- Windows + Codex Desktop：已验证。

尚未在 macOS、Linux、Claude Code 或其他 Agent 环境中完成本项目的完整安装与运行验证，因此本文不声称这些平台已经得到支持。它们可能支持相同格式，但请将其视为自行验证路径。

## 安装方式一：在 Codex 中从 GitHub 安装（推荐）

这条方式不要求你会 Git，也不要求你知道 Skill 文件应该放在哪里。

### 在哪里操作

在 Codex Desktop 中，新建一个任务，在输入框里输入：

```text
使用 $skill-installer 从 https://github.com/arayellie-prog/China-FIRE-Planner 安装 china-fire-planner。
```

如果 Codex 询问安装路径或确认操作，接受默认的用户 Skill 目录即可。安装结束后重新打开一个 Codex 任务，再用 `$china-fire-planner` 调用。

### 如何确认安装成功

在新的 Codex 任务中输入：

```text
请确认你现在能识别并使用 $china-fire-planner，然后只回复它的用途和当前版本范围。
```

如果 Codex 仍然说找不到这个 Skill，先重新启动 Codex，再重复确认。不要在原来已经打开的旧任务中判断，因为旧任务可能在启动时还没有加载新 Skill。

## 安装方式二：GitHub Download ZIP（不会 Git 也可以）

### Windows

1. 用浏览器打开本仓库：<https://github.com/arayellie-prog/China-FIRE-Planner>。
2. 点击绿色的 **Code** 按钮，再点击 **Download ZIP**。
3. 打开下载的 ZIP 文件，点击“全部解压”。记住解压后的文件夹位置。
4. 打开 Codex Desktop，在 Skills 管理界面选择 **Create → Upload from computer**，选择解压后的 `china-fire-planner` 文件夹；如果界面只接受压缩包，则选择下载的 ZIP 文件。
5. 安装完成后，重新打开一个 Codex 任务。
6. 输入：

   ```text
   使用 $china-fire-planner 帮我做第一次财务体检。
   ```

### macOS

macOS 的 GitHub 下载和 ZIP 解压步骤与 Windows 基本相同：打开仓库，点击 **Code → Download ZIP**，双击 ZIP 解压。然后在 Codex 的 Skills 管理界面选择 **Create → Upload from computer**，上传解压后的 `china-fire-planner` 文件夹或界面允许的 ZIP 文件。

本项目目前没有 macOS Codex Desktop 的实际验证记录；如果你的界面名称或上传方式不同，以当前 Codex 界面为准。安装后请新建任务，用下面的提示确认：

```text
请确认你能识别 $china-fire-planner。然后使用它帮我做第一次财务体检。
```

## 安装方式三：会 Git 的用户使用 git clone

### 在哪里操作

在 Windows 的 PowerShell，或 macOS 的 Terminal 中执行：

```bash
git clone https://github.com/arayellie-prog/China-FIRE-Planner.git
```

这只会把仓库下载到你当前所在的目录，不会自动安装 Skill。之后请在 Codex 的 Skills 管理界面上传仓库中的 `china-fire-planner` 文件夹，或在 Codex 中使用 `$skill-installer` 从上面的 GitHub URL 安装。

不要把仓库克隆到用户财务数据目录，也不要把真实的 `profile.yaml`、`snapshots.csv`、review 或账单文件复制进这个公开仓库。

## 第一次使用

安装并重新打开 Codex 后，在新任务中输入：

```text
使用 $china-fire-planner 帮我做第一次财务体检。

我以前没有认真管理过自己的财务，对每月支出也不完全清楚。
请根据我知道的信息建立 Preliminary Financial Baseline；不知道的地方保留为未知，不要猜。
最后用中文给我一份口语化报告，并告诉我下一步最重要的 1–3 件事。
```

你也可以自己指定互动方式，例如：

```text
我会一次性告诉你目前知道的收入、资产和负债，请直接整理，不需要逐步提问。
```

## 每月复盘

完成第一次财务体检并保存本地档案后，可以在新的 Codex 任务中输入：

```text
使用 $china-fire-planner 读取我的本地财务档案，帮我做这个月的财务复盘。
先看看历史，再从“这个月发生了什么”开始和我聊；不要让我填表。
```

Skill 会根据历史决定本月需要追问什么，把换工作、旅行、奖金、搬家或大额消费等生活事实转换成财务变化。你确认后，它才会计算并保存。月度报告可以有一个有趣但不评判人的当月标题；这不是长期人格标签，也不会写入数值快照。

## 数据和隐私

用户数据应保存在 Skill 目录之外、由用户选择的本地目录中。默认不要上传、同步或提交真实财务数据。

不要把身份证号、完整银行卡号、账户密码、验证码、券商凭证或真实账单提交到这个公开仓库。`.gitignore` 只能防止未追踪文件被提交，不能撤回已经提交的敏感信息。

## 项目内容

- `SKILL.md`：核心触发条件和工作流
- `references/profile-schema.md`：本地 Financial Profile 数据结构
- `references/onboarding.md`：Baseline 报告结构
- `references/monthly-review.md`：自然月度复盘和月度标题规则
- `references/privacy.md`：隐私和可选账单导入边界
- `scripts/finance_math.py`：确定性财务计算
- `examples/demo-profile.yaml`：匿名示例数据

## 当前边界

V0.2 不提供完整 FIRE 年限计算、长期财务人格、税务或社保计算、个股推荐、自动交易、银行/券商连接、自动账单解析或收益保证。
