---
name: ganhuo-geo-engineer
description: Use this Skill when the user provides an existing article, product page, tutorial, FAQ, or knowledge note and wants to rebuild it into a GEO or AI-search-friendly content asset. Use it for old-content refresh, citation-readiness improvement, answer-first restructuring, GEO upgrades, and Ganhuo AI content workflows. Do not use it for topic-only drafting, fabricated statistics, ranking guarantees, keyword stuffing, legal compliance audits, or GEOFlow system operations.
metadata:
  owner: Ganhuo AI
  maturity: production-draft
  review_cadence: quarterly
---

# Ganhuo GEO Engineer

## 这个 Skill 解决什么问题

`ganhuo-geo-engineer` 专门处理一种很常见、也最容易被浪费的内容：已经写过、确实有价值，但结构散、证据弱、答案不前置、FAQ 不完整、AI 很难直接摘取的旧文章。

它的目标不是“玄学保证被 AI 引用”，而是把旧内容改造成更容易被人读懂、被 AI 摘要、被销售复用、被知识库沉淀的内容资产。

核心原则很简单：

- 保留原文意思，不改观点；
- 先诊断，再改造；
- 有材料就写实，没有材料就标成待补；
- 让文章从“作者自说自话”变成“读者和 AI 都能快速抓住答案”；
- 最后交付一套能继续编辑、发布、复用的成品包。

## 什么时候使用

当用户提供下面这些内容时，使用这个 Skill：

- 公众号旧文；
- 官网文章、产品页、服务页；
- 教程、FAQ、知识库文章；
- 创始人随笔、案例笔记、行业观察；
- `.md`、`.txt`、`.html`、`.docx`、`.pdf` 等本地文件；
- 一批需要统一升级的历史内容。

如果用户只给了一个选题，想从零写新文章，不要直接使用这个 Skill。应先让用户提供旧文，或者转到新内容创作流程。

## 必读文件

- `references/geo-playbook.md` for the rebuild workflow.
- `references/geo-output-standard.md` for the delivery package.
- `references/geo-anti-patterns.md` when the request includes ranking promises, fake proof, keyword stuffing, or thin content.
- `references/geo-material-notes.md` when the user provides mixed materials or asks for evidence handling.
- `templates/article-brief.md` when the user needs an input template.

## 执行流程

1. 读取输入。如果文章无法读取，要求用户粘贴正文。
2. 先保留原文标题、核心观点、事实、案例、语气和限制条件。
3. 盘点材料：核心论点、证据、数据、引语、案例、实体、术语、结构、问题、可复用句子、缺失材料。
4. 保守打分：证据、结构、可回答性、实体清晰度、语义覆盖、可信信号、术语、稳定性、可读性、堆词风险。
5. 选择改造深度：
   - `light`：保留原结构，补核心答案、FAQ 和轻量清理；
   - `standard`：重构结构，补评分卡、FAQ、待补清单和风险提示；
   - `deep`：改造成完整内容资产，补章节、表格、FAQ、待补清单和多渠道复用建议。
6. 按优先级改写：答案前置、证据承载、可复用段落、FAQ、实体说明、实操步骤、边界限制、可读性。
7. 凡是用户材料里没有支撑的新增内容，都放入待补清单。不要编造数据、客户、引语、排名、产品能力或研究结论。
8. 按 `references/geo-output-standard.md` 返回完整交付包。
9. 最后做质量检查：原意是否保留，是否有虚构证据，是否堆词，待补清单是否清楚，结构是否可以发布。

## 默认交付

1. 改造后正文
2. GEO 评分卡
3. 改造说明
4. 待补清单
5. 风险提示

如果用于干活 AI 教程、飞书文档、官网知识库等场景，再补充：

6. 飞书、官网、公众号、知乎、销售 FAQ、知识库的复用建议

## 质量底线

宁可少写，也不要空泛。

每一个强结论都必须处在下面四种状态之一：

- 用户材料已经支撑；
- 执行任务时已经核验；
- 明确放入待补清单；
- 删除或弱化表达。

永远不要把缺失的数据写成假数据。永远不要承诺排名、流量、引用、推荐或模型偏好。

## 发布前校验

仓库发布前运行：

```bash
python3 scripts/validate_skill.py
```
