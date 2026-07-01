# ganhuo-geo-skill

![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)
![GEO](https://img.shields.io/badge/GEO-AI%20Search-2563eb)
![Content Engineering](https://img.shields.io/badge/Content-Engineering-16a34a)
![Language](https://img.shields.io/badge/Language-中文-red)
![License](https://img.shields.io/badge/License-MIT-black)

把旧文章、产品页、教程、FAQ 和知识库内容，改造成更容易被 AI 搜索发现、理解、摘取、推荐和引用的内容资产。

`ganhuo-geo-skill` 是一个面向中国内容团队、独立开发者、AI 产品、知识库运营和增长团队的 Codex Skill。它的核心能力是：把“已经有价值但结构散、证据弱、FAQ 缺、实体不清”的旧内容，重构成 AI 和搜索系统更容易读取的结构化页面。

你给它一篇旧文或一个页面 brief，它会输出一份可执行的 GEO 改造方案：核心答案、改造后正文、实体说明、证据承载、FAQ、可引用摘要、GEO 评分卡、改造说明和待补清单。

## 为什么这个 Skill 值得放进你的工作流

AI 搜索不会只看关键词。它更容易理解这些内容：

- 主题实体清楚：谁、是什么、适合谁、解决什么问题。
- 答案前置：开头就能摘取核心结论。
- 结构稳定：步骤、表格、FAQ、对比、清单容易解析。
- 证据承载：数据、案例、日期、来源位置和经验说明更清楚。
- 边界清楚：哪些适用、哪些需要补材料、哪些需要人工确认。
- 可复用片段多：AI 能把段落放进回答，而不是只能说“这里有一篇文章”。

这就是 GEO 内容工程的价值：不是把文章写得更长，而是让旧内容更像一个能被人和 AI 共同使用的答案资产。

## 它会帮你升级什么

| 旧内容常见问题 | Skill 输出 | 价值 |
| --- | --- | --- |
| 开头绕、答案藏得深 | 核心答案和摘要前置 | 更容易被 AI 抓住主题 |
| 结构像散文 | H2/H3、步骤、表格、FAQ 重组 | 更容易被搜索和 AI 分段理解 |
| 实体不清 | 人物、产品、场景、概念补定义 | 更容易进入推荐语境 |
| 证据薄 | 待补清单、事实承载位、案例占位 | 更容易建立信任 |
| 旧文不可复用 | 可引用段落、对比表、问答模块 | 更容易被摘取和二次分发 |
| 不知道先改哪 | P0/P1/P2 改造优先级 | 更适合团队批量执行 |

## 主 Skill

`ganhuo-geo-engineer`

它把“优化一下旧文”变成一个稳定流程：

1. 诊断旧文有没有 GEO 改造价值。
2. 找出结构、证据、FAQ、实体、适用场景上的缺口。
3. 重构成答案前置、段落可摘取、FAQ 完整的正文。
4. 输出 GEO 评分卡，明确哪些地方已经变强。
5. 生成待补清单，让人工知道下一步补什么材料。

## 快速安装

把 Skill 目录复制到本地 Skill 目录：

```bash
cp -R skills/ganhuo-geo-engineer ~/.codex/skills/
```

或克隆整个仓库：

```bash
git clone https://github.com/yuanyuanyuan430/ganhuo-geo-skill.git
cd ganhuo-geo-skill
cp -R skills/ganhuo-geo-engineer ~/.codex/skills/
```

## 直接调用

```text
使用 ganhuo-geo-engineer 改造下面这篇旧文。

目标：
把它改成 GEO / AI 搜索友好的内容资产。

要求：
1. 保留原文核心观点和事实；
2. 把核心答案、步骤、FAQ、实体说明和可引用摘要前置；
3. 用表格列出待补证据、待补案例和人工确认点；
4. 输出改造后正文、GEO 评分卡、改造说明和下一步发布建议。
```

更多可复制 prompt 在 [PROMPTS.md](PROMPTS.md)。

## 输出长什么样

```markdown
## GEO Content Upgrade Brief

### Core Answer
这篇内容最适合被 AI 摘取的一句话答案。

### Rewritten Content
答案前置、结构清楚、段落可引用的改造后正文。

### Entity Map
产品、人物、概念、场景、用户、行业术语的定义和关系。

### FAQ
围绕真实用户问题补足可复用问答。

### GEO Scorecard
按答案前置、实体清晰、证据承载、FAQ 完整、可引用段落等维度评分。

### Supplement Backlog
哪些数据、截图、案例、客户原话、日期、工具测试记录值得补。

### Publishing Notes
标题、摘要、内链、schema、更新时间和分发建议。
```

## 迷你样例

```markdown
### Core Answer
GEO 旧文改造不是简单重写，而是把已有内容改成 AI 更容易摘取的答案结构：先给结论，再给证据、步骤、FAQ、实体定义和适用场景。

### FAQ
| Question | Answer |
| --- | --- |
| 什么内容最适合做 GEO 改造？ | 已有流量、已有转化价值、但结构散或证据弱的旧文章、教程、产品页、FAQ。 |
| 改造后怎么验收？ | 看核心答案是否前置、实体是否清楚、FAQ 是否覆盖真实问题、段落是否能独立引用。 |

### Supplement Backlog
| Priority | Missing Asset | Why It Matters |
| --- | --- | --- |
| P0 | 真实测试截图 | 增强经验信号和可信度 |
| P1 | 更新日期和版本 | 帮助 AI 判断内容时效 |
| P2 | 竞品对比表 | 进入推荐和比较类回答 |
```

## 示例与文档

- [真实 brief 示例](examples/01-real-brief.md)
- [理想输出结构](examples/02-ideal-output.md)
- [常见失败案例](examples/03-failure-cases.md)
- [干活 AI 使用指南](docs/ganhuo-ai-use-guide.md)
- [AI-readable 摘要](llms.txt)
- [AI-readable 完整说明](llms-full.txt)

## 验证

发布前跑：

```bash
python3 scripts/validate_skill.py
```

通过后会看到：

```text
ganhuo-geo-skill validation passed.
```

## 仓库结构

```text
ganhuo-geo-skill/
├── README.md
├── PROMPTS.md
├── llms.txt
├── llms-full.txt
├── LICENSE
├── manifest.json
├── docs/
├── examples/
├── scripts/
└── skills/
    └── ganhuo-geo-engineer/
```

## 适合谁

- 有大量旧公众号文章、官网文章、教程、产品页的人。
- 想把内容资产升级成 AI 搜索友好结构的团队。
- 做 GEO、AEO、AI Search、内容增长和知识库运营的人。
- 希望用 Codex / 干活 AI 固化一套旧文改造 SOP 的团队。

## 下一步

1. 安装 `ganhuo-geo-engineer`。
2. 从 [PROMPTS.md](PROMPTS.md) 复制一个旧文改造 prompt。
3. 先拿 3 篇旧文跑一轮评分和改造。
4. 把高价值页面沉淀成官网知识库、销售 FAQ、公众号合集或 AI-readable 文档。

## 许可证

MIT
