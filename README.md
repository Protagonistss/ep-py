<div align="center">

# 🐍 ep-py

**零基础友好的 Python 教学仓库**

从装好环境、写下第一行代码,到独立完成小程序,一步一步来。

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/依赖管理-uv-de5fe9)
![pytest](https://img.shields.io/badge/test-pytest-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

[快速开始](#-快速开始) · [环境准备](#-环境准备) · [学习路线](#-学习路线) · [课程目录](#-课程目录) · [零基础指南](init_env.md)

</div>

---

> 🚀 **完全零基础?** 请先阅读 **[init_env.md](init_env.md)** —— Git 安装配置、拉取仓库、SSH/HTTPS 鉴权、环境搭建,一站式搞定,15~30 分钟。

## 🚀 快速开始

```bash
git clone git@github.com:Protagonistss/ep-py.git
cd ep-py
uv run python main.py
```

输出:

```
你好,世界!
我的第一行 Python 代码!
```

没装 uv?👇 往下看环境准备,或者直接走 [init_env.md](init_env.md)。

## 🧰 环境准备

本仓库使用 **[uv](https://docs.astral.sh/uv/)** 管理 Python 环境与依赖:自动安装 Python、创建虚拟环境、锁定依赖版本,不需要手动激活虚拟环境。

> 💡 国内网络不用愁:项目已内置华为云 PyPI 镜像(见 `pyproject.toml`),`uv sync` 自动走国内源,零配置。想换源/覆盖见 [init_env.md](init_env.md)。

<details open>
<summary><b>安装 uv</b></summary>

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows(PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 验证
uv --version
```

</details>

<details open>
<summary><b>uv 常用命令</b></summary>

| 命令 | 作用 |
| ---- | ---- |
| `uv python install 3.12` | 安装指定版本的 Python |
| `uv init` | 初始化项目(生成 `pyproject.toml`) |
| `uv add requests` | 添加依赖并写入 `pyproject.toml` |
| `uv sync` | 按锁文件安装全部依赖(自动创建 `.venv`) |
| `uv run python main.py` | 在项目环境中运行(自动同步依赖) |
| `uv run pytest` | 在项目环境中运行测试 |
| `uvx ruff check` | 临时运行工具,不污染项目环境 |

日常最常用的就两条:**`uv add` 加包、`uv run` 跑命令**。

</details>

<details>
<summary><b>备选:不用 uv,直接用 venv</b></summary>

```bash
python -m venv .venv

# 激活(Windows)
.venv\Scripts\activate
# 激活(macOS / Linux)
source .venv/bin/activate

pip install -e ".[dev]"   # 或手动安装 pytest
```

</details>

## 🧭 学习路线

不背语法表。**每一关都先做出一个能跑的小东西**,知识点只是顺手点亮的能力。

| | 你将做出 | 顺带点亮技能 |
| :---: | ---- | ---- |
| 🥚 Lv.1 | 自我介绍生成器 | `print` · `input` · 变量与类型 |
| 🐣 Lv.2 | 猜数字游戏(和电脑对玩) | `if` / `for` / `while` |
| 🐥 Lv.3 | 命令行待办清单 | 列表 · 字典 · 集合 |
| 🐤 Lv.4 | 单词测验闯关 | 函数 · 参数 · 作用域 |
| 🐱 Lv.5 | 宠物养成小游戏 | 类 · 实例 · 继承 |
| 📂 Lv.6 | 批量文件整理脚本 | 模块 · `pathlib` · `json` |
| 📓 Lv.7 | 记账本(数据存到本地) | 文件读写 · 异常处理 |
| 🎩 Lv.8 | 给旧项目装上新能力 | 迭代器 · 生成器 · 装饰器 |
| 🚀 Lv.9 | 把待办清单变成正式项目 | pytest · 类型注解 · 打包 |

> 📍 **当前进度**:Lv.1 已发布,从 [第 1 课](lessons/01_hello_python.md) 开始吧!

## 📚 课程目录

| # | 关卡 | 状态 | 讲义 | 练习 |
| :-: | ---- | :---: | ---- | ---- |
| 1 | 🥚 你好,Python!——自我介绍生成器 | ✅ 已发布 | [lessons/01_hello_python.md](lessons/01_hello_python.md) | `exercises/01_basics/` |
| 2 | 🐣 猜数字游戏 | ⏳ 计划中 | - | - |

## 📝 练习与作业流程

```bash
# 1. 开始前拉取最新课程
git pull

# 2. 运行课堂项目 / 作业(uv 会自动准备环境)
uv run python exercises/01_basics/intro_generator.py

# 3. 完成后提交
git add exercises/01_basics/
git commit -m "完成第 1 课作业"
git push
```

## 📁 目录结构

```
.
├── README.md           # 本文件
├── init_env.md         # 零基础环境搭建指南
├── LICENSE             # MIT 协议
├── main.py             # 第一个程序
├── pyproject.toml      # 项目配置与依赖(uv 管理)
├── uv.lock             # 依赖锁文件,保证环境可复现
├── lessons/            # 每课讲义
│   └── 01_hello_python.md
├── exercises/          # 每课的课堂项目与作业
│   └── 01_basics/
└── tests/              # pytest 测试
```

## 🤝 如何提交作业

1. 保持练习文件在 `exercises/` 对应课程目录下
2. 提交信息写清楚做了什么,如 `完成第 1 课作业:温度转换器`
3. 遇到报错先查讲义附录的 **报错速查表**,再看 [init_env.md](init_env.md) 的 FAQ

## 📄 License

[MIT](LICENSE) © Protagonistss

---

<div align="center">

**通关 Lv.9,你就正式入门了。现在,回到第一个 🥚 吧!**

</div>
