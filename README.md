# IG 粉絲追隨神器

📱 一個基於 Django 的本地網頁工具，可追蹤 Instagram 粉絲變動，幫助你找出誰取消追蹤你、誰是新粉絲。

---

## 🚀 專案特色

- 🔍 爬取 Instagram 的追蹤與粉絲名單
- 🔔 爾後使用便能偵測新增粉絲與取消追蹤者
- 🗂 清楚顯示帳號變動記錄
- 🌐 提供本地端簡易網頁介面操作（基於 Django）

---

## 🛠️ 安裝與啟動方式

### 第一步：下載專案

```bash
git clone https://github.com/quincy408/instagram-follower-tool.git
cd instagram-follower-tool
```

### 第二步：建立虛擬環境

```bash
python -m venv venv
source venv/bin/activate  # Windows 系統請執行：venv\Scripts\activate
```
### 第三步：安裝依賴套件

```bash
pip install -r requirements.txt
```

### 第四步：啟動 Django 專案

```bash
python manage.py runserver
```

### 🎉 啟動伺服器後，前往 [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)，你將看到 IG 粉絲追隨神器的首頁介面！
---
🔽 使用畫面教學：
![教學演示](./static/PNG/7.gif)
