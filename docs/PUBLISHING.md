# GitHub 发布材料

## 建议仓库信息

- 仓库名：`michael-damaige-skill`
- 简介：`把刷到时的触动，变成需要时找得到的答案。Michael大麦哥视频字幕 AI 技能：原文引用、视频出处、时间点，离线可检索。`
- Topics：`agent-skills`, `ai-skills`, `chinese`, `subtitles`, `srt`, `knowledge-base`, `douyin`, `python`
- 首版标签：`v0.1.0`
- 首版标题：`原文有出处：让 AI 带你回到大麦哥说出那句话的时刻`

## 可直接使用的发布文案

有些话，刷到时很触动；真正需要它时，却怎么也找不到了。

我把 Michael大麦哥的 19 份视频字幕，做成了一个 AI 技能：
问低谷、问内耗、问成长，也可以直接问“那句话出自哪条视频？”

它会从 11,428 条字幕中寻找相关原文，并附上视频标题、抖音入口和字幕时间点。
不是只给你一句脱离上下文的金句，而是让你可以回到视频里，重新听完整段表达。

Python 标准库即可运行，离线检索，无需 API key。安装到支持 SKILL.md 的助手后，可以显式调用，也支持宿主自动选择。

感谢原作者创作。第三方整理，字幕权利与代码授权分开说明；引用时间以字幕为依据。

## 数据证据补齐后可使用的增强版开头

仅在补齐统计依据并确定覆盖范围后，替换下述括号中的信息：

> 把大麦哥的爆款表达，变成随时能查、句句有出处的 AI 技能。
> 本项目收录的【具体数量】条作品，累计获赞超过 3000 万（截至【统计日期】，依据【证据链接】）。聊到低谷、内耗和成长时，让打动过你的那句话，重新回到身边。

若 3000 万实际指账号总获赞，应改为“作者账号累计获赞超过 3000 万”，不要暗示是这 19 份资料的合计；“爆款作品”也应与具体视频数据对应。“全部往期作品”需要完整作品清单才能使用。

## 发布操作

项目尚未连接 GitHub 远程仓库。首次发布前，把可公开授权说明和点赞证据补到 `docs/PROVENANCE.md`，确认 README 中的状态与实际一致。

在 GitHub 创建名为 `michael-damaige-skill` 的空仓库，不要让网页额外生成 README 或 LICENSE。在本地项目目录依次执行：

```bash
git init -b main
git add .
git commit -m "Initial release: searchable Michael Damaige subtitle skill"
```

再将 GitHub 显示的**你自己的仓库地址**配置为 origin，执行 `git push -u origin main`。也可使用 GitHub Desktop 的 Add existing repository / Publish repository。

首版发布说明可使用上方文案，补上真实仓库地址；需要 Release 附件时，可将整个技能目录打包为 ZIP，目录名为 `michael-damaige`。

## 首版验证记录

运行 `python -m unittest discover -s tests -v` 校验字幕解析、检索结果原文与时间、来源链接及空命中行为。GitHub Actions 在 Windows / Linux 的 Python 3.10 / 3.12 上执行同样的检查。
