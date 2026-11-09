# GitHub 发布材料

## 建议仓库信息

- 仓库名：`michael-damaige-skill`
- 简介：`把刷到时的触动，变成需要时找得到的答案。Michael大麦哥视频字幕 AI 技能：原文引用、视频出处、时间点，离线可检索。`
- Topics：`agent-skills`, `ai-skills`, `chinese`, `subtitles`, `srt`, `knowledge-base`, `douyin`, `python`
- 首版标签：`v0.1.0`
- 首版标题：`原文有出处：让 AI 带你回到大麦哥说出那句话的时刻`

## 可直接使用的发布文案

有些话，刷到时很触动；真正需要它时，却怎么也找不到了。

我把 Michael大麦哥往期爆款作品文案，汇集成了一个可以随时调用的 AI 技能：
这些收录作品在所提供截图中的点赞显示值，合计约 2,760.4 万。
问低谷、问内耗、问成长，也可以直接问“那句话出自哪条视频？”

它会从收录的作品文案中寻找相关原文，并附上视频标题、抖音入口和字幕时间点。
不是只给你一句脱离上下文的金句，而是让你可以回到视频里，重新听完整段表达。

Python 标准库即可运行，离线检索，无需 API key。安装到支持 SKILL.md 的助手后，可以显式调用，也支持宿主自动选择。

内容库也会跟着大麦哥的创作继续生长：持续跟进视频动态，陆续补充新作品文案、出处与字幕时间点。更新技能后，就能从新增内容里寻找新的启发。

感谢原作者创作。第三方整理，字幕权利与代码授权分开说明；引用时间以字幕为依据。

## 可直接使用的增强版开头

> 汇集大麦哥往期爆款作品文案，收录作品累计获赞超 2700 万。从低谷与内耗，到爱情与人生选择，把打动过你的表达，变成随时能查、原文有出处的 AI 技能。

依据、截图和详细统计口径见 [点赞统计](LIKES.md)。数据是对应作品截图显示值之和，随时间变化。

## 发布操作

项目已发布至 https://github.com/feiyuaq/michael-damaige-skill 。以下首次发布命令仅供复用参考，现有仓库不必重新初始化。

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
