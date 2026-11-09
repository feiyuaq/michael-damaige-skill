# Michael大麦哥 · 原文有出处

### 把刷到时的触动，变成需要时找得到的答案。

**汇集大麦哥往期爆款作品文案 · 收录作品累计获赞超 2700 万 · 原文、出处、时间点一起查。**

点赞依据与统计口径见 [点赞统计](docs/LIKES.md)。

你也许记得大麦哥讲过一句话，却想不起在哪条视频、哪一分钟。

这个项目汇集 **Michael大麦哥往期爆款作品文案**，把一篇篇关于生活与成长的表达，整理成可以被 AI 助手随时调用的内容库。从低谷、内耗到爱情、自由与人生选择，让打动过你的话，在需要时重新被找到——有原文、有出处，也有具体的时间。

**不止“他好像说过”。而是原文、出处、时间点，一起给你。**

### 跟着大麦哥的更新，让内容库继续生长。

这个技能会持续跟进 Michael大麦哥的视频动态，陆续补充新作品文案、原视频出处与字幕时间点。让你每次带着新的问题回来，都有机会找到新的启发。内容经整理后更新至本仓库；已安装的用户需下载最新版或拉取仓库更新，即可使用新增内容。

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Code license](https://img.shields.io/badge/Code-MIT-green)](LICENSE)
[![Offline](https://img.shields.io/badge/Search-Offline-blue)](#快速开始)

> 第三方整理项目，非作者官方产品。原内容权利归各自权利人；代码与字幕的权利范围分开说明，详见 [内容权利说明](CONTENT_RIGHTS.md)。

## 你可以拿它做什么

- **找原话**：“大麦哥关于走出低谷说过什么？”
- **带着问题找启发**：“总忍不住和别人比较，能从大麦哥的视频里找点建议吗？”
- **回到视频现场**：“这句话是哪条视频、几分几秒说的？”
- **做有出处的学习笔记**：保留短引、原视频链接和字幕时间，区分作者观点与自己的理解。

## 它怎么回答

回答会包含相关的字幕短引，并提供：

| 信息 | 来源 |
| --- | --- |
| 原文字词 | 原始 SRT 字幕 |
| 视频标题 | 收录目录名称 |
| 起止时间、字幕序号 | SRT 时间轴 |
| 原视频入口 | 配套 `视频信息.txt` 中的抖音分享链接 |
| 解读与建议 | 明确标注为助手的理解，不冒充作者原话 |

字幕可能包含自动识别错误；当前时间点未经视频逐条校准，视频标题与链接对应关系也未逐条联网核验。脚本返回的是检索候选，AI 还需要阅读上下文。

## 快速开始

需要 Python 3.10 或以上；不需要安装第三方依赖，不需要 API key。

下载本仓库并进入目录后执行：

```bash
python scripts/search.py "低谷" --limit 3
python scripts/search.py "比较" --limit 5
python scripts/search.py "放过自己" --video "260831" --limit 3
```

输出 UTF-8 JSON，包含 `quote`、`title`、`start`、`end`、`cue_start`、`cue_end`、`srt`、`douyin_url`。无命中时 `results` 为空。搜索采用中文双字词与英文词的词面匹配，并非向量语义检索；短关键词通常比整段提问效果更好。

## 安装为 AI 技能

本仓库根目录就是一个完整技能，技能名为 `michael-damaige`。把下载后的**整个目录**放到支持 `SKILL.md` 的助手技能目录，并把文件夹命名为 `michael-damaige`；保留 `STR/` 和 `scripts/`。

例如，Codex 的个人技能目录通常为：

```text
Windows: %USERPROFILE%\.codex\skills\michael-damaige\SKILL.md
macOS / Linux: ~/.codex/skills/michael-damaige/SKILL.md
```

如果配置了自定义技能目录，以你的配置为准。刷新技能列表或开启新会话后，可显式使用：

```text
使用 $michael-damaige：我最近处在人生低谷，想看看大麦哥怎么讲。
请引用字幕原文，告诉我视频标题和几分几秒，并给原视频链接。
```

本技能允许自动选择；安装后，在支持自动发现的助手中，点名大麦哥、询问其观点等相关问题可触发技能。是否实际触发由宿主助手决定；仅下载到普通项目目录不等于已安装。其他助手如支持 `SKILL.md`，请按其技能安装机制接入；未承诺所有平台开箱即用。

## 当前收录

收录往期作品文案与配套字幕，保留原始时间轴和视频入口，方便检索、引用与回看。完整标题、文件、收录数量与链接见 [视频目录](docs/VIDEOS.md) 和机器可读的 [catalog.json](catalog.json)。

主题包括：走出低谷、放过自己、与他人比较、自由、珍惜当下、时间感、独立思考、爱情、自我管理、人性与成长。当前是所提供资料的整理版，并非作者全部作品合集；截图中对应作品的点赞统计见 [逐项清单](docs/LIKES.md)。

## 项目结构

```text
SKILL.md                 AI 技能入口
agents/openai.yaml       技能展示信息与自动选择设置
STR/                     保留的原始字幕与视频分享信息
catalog.json             从原文件生成的视频元数据
scripts/search.py        离线检索与出处返回
scripts/build_catalog.py 重新生成视频目录数据
tests/                   原文、时间与来源一致性检查
docs/                    视频列表、来源记录与发布材料
```

## 添加和纠错

新增资料时，在 `STR/` 下创建一个独立视频目录，放入一个 `.srt` 文件与 `视频信息.txt`（含原视频链接），然后运行：

```bash
python scripts/build_catalog.py
python -m unittest discover -s tests -v
```

更新 [视频列表](docs/VIDEOS.md) 和本页统计。贡献规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。请勿将未经核对的机器润色当作原字幕提交。

## 授权与致谢

感谢 Michael大麦哥的创作。请优先回到原视频观看、关注和支持作者。

检索代码、技能指令和项目原创说明采用 [MIT License](LICENSE)；字幕、视频分享文案、作者名称及第三方引文不在 MIT 授权范围内，详见 [CONTENT_RIGHTS.md](CONTENT_RIGHTS.md)。资料与统计来源见 [来源记录](docs/PROVENANCE.md)。

如果这个项目帮你找回了一句当时打动你的话，欢迎 Star，也欢迎带着准确出处来补充和纠错。
