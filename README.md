# 🇮🇹 Patente A&B — 意大利驾照题库 PWA

## 📁 文件说明

```
patente-ab/
├── index.html      ← 主应用（7134道题全部内嵌）
├── manifest.json   ← PWA配置
├── sw.js           ← Service Worker（离线支持）
└── icons/
    ├── icon-192.png
    └── icon-512.png
```

---

## 🚀 部署到 GitHub Pages（免费、5分钟完成）

### 第一步：创建 GitHub 账号
1. 打开 https://github.com
2. 注册免费账号（已有账号跳过）

### 第二步：新建仓库
1. 登录后点右上角 **+** → **New repository**
2. Repository name 填：`patente-ab`
3. 选 **Public**（必须，GitHub Pages免费版需要公开）
4. 点击 **Create repository**

### 第三步：上传文件
1. 在新建的仓库页面，点击 **uploading an existing file**
2. 把 `patente-ab/` 文件夹里的**所有文件**拖入上传区域
   - index.html
   - manifest.json
   - sw.js
   - icons/ 文件夹（含两个png）
3. 点击 **Commit changes**

### 第四步：开启 GitHub Pages
1. 进入仓库 **Settings**（顶部导航）
2. 左侧菜单找 **Pages**
3. Source 选择 **main** 分支，文件夹选 **/ (root)**
4. 点击 **Save**
5. 等1~2分钟，页面会显示：
   > Your site is published at `https://你的用户名.github.io/patente-ab/`

### 第五步：Android 安装为 App
1. 用 **Chrome** 打开上面的网址
2. 浏览器会自动弹出 **"添加到主屏幕"** 横幅 → 点 **安装**
3. 或者：点浏览器右上角菜单 **⋮** → **添加到主屏幕**
4. 完成！主屏幕出现意大利国旗图标，点开就是 App

---

## 📱 功能

- 🎯 **练习模式**：随机抽题，VERO/FALSO答题，自动评分
- 📖 **浏览题库**：搜索、筛选分类、点击查看中文翻译
- 📊 **统计**：各分类题目分布
- 🌐 **中文翻译**：点击按需翻译（需要网络）
- 📴 **离线可用**：题库本体离线可用，翻译需要网络
- 📲 **可安装**：添加到主屏幕后像原生App一样使用

---

## 💡 提示

- 题库来源：意大利交通部官方 Listato A&B（2025年2月版）
- 通过标准：正确率 ≥ 90%
- 建议先按分类练习，再混合模式备考
