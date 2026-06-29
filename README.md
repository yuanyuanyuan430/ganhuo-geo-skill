# ganhuo-geo-skill

面向中国内容团队的 GEO 旧文改造 Skill。

这个仓库目前只做一件事：用 `ganhuo-geo-engineer` 把已经写过的文章、产品页、教程、FAQ、人物资料，改造成更适合 AI 搜索理解、摘取和复用的内容资产。

仓库不做玄学承诺，不保证排名，不编造数据。它解决的是一个更实际的问题：旧内容里明明有价值，但结构散、证据弱、FAQ 缺、边界不清，AI 看完不知道该怎么引用。

## 它适合谁

- 有一堆旧公众号、官网文章、产品说明页的人。
- 做 GEO、AI 搜索、内容增长的团队。
- 想把旧内容整理成飞书教程、官网知识库、销售 FAQ 的运营同学。
- 想在干活 AI 里固定一套旧文改造 SOP 的团队。

## 主 Skill

`ganhuo-geo-engineer`

作用：

- 先诊断旧文有没有改造价值；
- 找出结构、证据、FAQ、实体、边界上的缺口；
- 输出改造后正文、GEO 评分卡、改造说明、待补清单、风险提示；
- 把“优化一下”变成可执行的 P0/P1/P2 任务。

## 不做什么

- 不保证 AI 一定引用。
- 不保证搜索排名。
- 不虚构统计数据、客户案例、专家原话。
- 不做关键词堆砌。
- 不把一个选题当成旧文改造。

## 安装

把 Skill 目录复制到本地 Skill 目录：

```bash
cp -R skills/ganhuo-geo-engineer ~/.codex/skills/
```

## 干活 AI 调用示例

```text
使用 ganhuo-geo-engineer 改造下面这篇旧文。

目标：
把它改成 GEO / AI 搜索友好的内容资产。

要求：
1. 保留原文核心观点，不改变意思。
2. 不编造数据、案例、客户、排名或效果。
3. 把缺数据、缺案例、缺原话的位置写进待补清单。
4. 重构成更容易被 AI 摘取的结构：核心答案、步骤、FAQ、边界。
5. 输出改造后正文、GEO 评分卡、改造说明、待补清单、风险提示。
```

## 仓库结构

```text
ganhuo-geo-skill/
├── README.md
├── LICENSE
├── manifest.json
├── docs/
│   └── ganhuo-ai-use-guide.md
├── examples/
│   ├── 01-real-brief.md
│   ├── 02-ideal-output.md
│   └── 03-failure-cases.md
├── scripts/
│   └── validate_skill.py
└── skills/
    └── ganhuo-geo-engineer/
        ├── SKILL.md
        ├── manifest.json
        ├── templates/article-brief.md
        ├── evals/
        └── references/
```

## 验证

发布前跑：

```bash
python3 scripts/validate_skill.py
```

通过后会看到：

```text
ganhuo-geo-skill validation passed.
```

## 许可证

MIT
