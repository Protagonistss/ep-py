# 初始化环境指南(零基础)

面向第一次接触 Git 和 Python 的同学,从零开始把环境搭好。全部完成约 15~30 分钟。

> 需要安装的只有两个东西:
>
> | 软件 | 用途 |
> | ---- | ---- |
> | Git | 版本管理,负责拉取和提交代码 |
> | uv | 管理 Python 版本和依赖 |

---

## 1. 安装 Git

**Windows:**

1. 下载安装包:<https://git-scm.com/download/win>
2. 双击运行,所有选项保持默认,一路"下一步"即可
3. 安装完成后,右键菜单出现 `Open Git Bash Here` 就说明装好了

**macOS:** 打开"终端"执行(弹出窗口点"安装"):

```bash
xcode-select --install
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt install git
```

**验证安装**(任何平台,能打印版本号即可):

```bash
git --version
```

---

## 2. 配置 Git(安装后必做一次)

Git 需要知道"你是谁",每次提交代码都会带上这个署名:

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

例如:

```bash
git config --global user.name "zhangsan"
git config --global user.email "zhangsan@example.com"
```

> ⚠️ 邮箱建议与你的 GitHub 注册邮箱一致,这样提交记录才能正确关联到你的 GitHub 账号。

再设置两个推荐项(默认分支名、换行符处理):

```bash
git config --global init.defaultBranch main
git config --global core.autocrlf input
```

查看自己配置了什么:

```bash
git config --list
```

---

## 3. 注册 GitHub 并配置访问权限

先注册 GitHub 账号:<https://github.com/signup>

然后**二选一**配置身份验证:

### 方式 A:HTTPS(最简单,适合先跑通)

什么都不用配,直接跳到第 4 步用 HTTPS 地址克隆。

但每次推送代码时 GitHub 会要求输入:

- Username:GitHub 用户名
- Password:**不是账号密码**,而是 Personal Access Token(见下)

创建 Token:`GitHub 头像 → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token`,勾选 `repo` 权限,生成后**立即复制保存**(只显示一次)。

### 方式 B:SSH(推荐,配置一次终身免密)

1. 生成密钥(邮箱换成你自己的,一路回车即可):

```bash
ssh-keygen -t ed25519 -C "你的邮箱"
```

2. 查看并复制公钥内容(一长串以 `ssh-ed25519` 开头的文本):

```bash
# Windows(Git Bash)
cat ~/.ssh/id_ed25519.pub

# 或 PowerShell
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

3. 添加到 GitHub:`头像 → Settings → SSH and GPG keys → New SSH key`,Title 随便填(如"我的电脑"),Key 粘贴公钥内容,点 `Add SSH key`。

4. 测试连接:

```bash
ssh -T git@github.com
```

第一次会问 `Are you sure you want to continue connecting?`,输入 `yes`。看到下面这行就是成功:

```
Hi 你的用户名! You've successfully authenticated, but GitHub does not provide shell access.
```

> 💡 如果 SSH 连接超时,可让 SSH 走 443 端口:创建 `~/.ssh/config` 文件,写入:
>
> ```
> Host github.com
>     Hostname ssh.github.com
>     Port 443
>     User git
> ```

---

## 4. 拉取(克隆)仓库

选一个存放代码的目录,右键 `Open Git Bash Here`(或用 `cd` 进入),执行:

```bash
# SSH 方式(配了方式 B 用这个)
git clone git@github.com:Protagonistss/ep-py.git

# HTTPS 方式(配了方式 A 用这个)
git clone https://github.com/Protagonistss/ep-py.git
```

进入仓库目录:

```bash
cd ep-py
```

> 📌 `git clone` 只需要做一次。以后获取最新代码用:
>
> ```bash
> git pull
> ```

---

## 5. 安装 uv 并准备 Python 环境

安装 uv:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows(PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> 安装后如果提示 `uv: command not found`,关闭终端重新打开再试。

在仓库目录里初始化环境(会自动创建 `.venv` 虚拟环境并装好依赖):

```bash
uv sync
```

运行第一个程序验证:

```bash
uv run python main.py
```

运行测试:

```bash
uv run pytest
```

### 关于下载速度:PyPI 镜像(项目已内置,无需配置)

Python 的包都来自官方仓库 PyPI,服务器在国外,直连下载可能很慢甚至超时。

**本项目已在 `pyproject.toml` 里内置了华为云镜像**,`uv sync` / `uv add` 会自动走国内源,什么都不用做。

想给你自己的其他项目也配置镜像(全局生效,二选一):

```bash
# 方式一:环境变量(写入 ~/.bashrc 或系统环境变量)
export UV_DEFAULT_INDEX="https://repo.huaweicloud.com/repository/pypi/simple/"
```

```toml
# 方式二:用户级配置文件
#   Windows:%USERPROFILE%\AppData\Roaming\uv\uv.toml
#   macOS / Linux:~/.config/uv/uv.toml
[[index]]
url = "https://repo.huaweicloud.com/repository/pypi/simple/"
default = true
```

常用国内镜像还有:清华 `https://pypi.tuna.tsinghua.edu.cn/simple` 等。
如果你在国外或有自己的加速方式,设置环境变量 `UV_DEFAULT_INDEX` 即可覆盖项目内置的镜像。

---

## 6. 日常流程:改代码 → 提交 → 推送

```bash
# 1. 开始前先拉最新代码
git pull

# 2. 修改/新增文件后,看看改了什么
git status        # 哪些文件变了
git diff          # 具体改了哪些内容

# 3. 把改动加入暂存区(可用文件名,或 . 表示全部)
git add 文件名

# 4. 提交到本地仓库,-m 后面写这次改了什么
git commit -m "完成 01_basics 练习"

# 5. 推送到 GitHub
git push
```

---

## 7. 常见问题(FAQ)

| 报错/现象 | 原因与解决 |
| --------- | ---------- |
| `Permission denied (publickey)` | SSH 没配好,回到第 3 步方式 B 检查密钥 |
| 推送时要求输密码且总失败 | 用的是 HTTPS,密码处要填 Token(第 3 步方式 A) |
| 连接 `github.com` 超时 | 网络问题;SSH 可改走 443 端口(见第 3 步) |
| `uv: command not found` | 重开终端让 PATH 生效;仍不行就重启电脑 |
| `uv sync` 卡住/下载极慢 | 网络问题;本项目已内置华为云镜像,若仍慢可设置 `UV_DEFAULT_INDEX` 换清华源(见第 5 节) |
| `git pull` 报冲突 | 本地改动和别人冲突了,先 `git stash` 暂存,拉完再 `git stash pop` |
| 不想每次输 Token | `git config --global credential.helper store`(明文保存,个人电脑可用) |

---

环境搭好后,回到 [README.md](README.md) 开始学习路线吧 🎉
