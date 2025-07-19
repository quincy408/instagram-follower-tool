# IG 粉絲追隨神器 | IG Follower Tracker Tool

📱 一個基於 Django 的本地網頁工具，可紀錄 Instagram 粉絲清單，在變動時幫助你找出誰取消追蹤你、誰是新粉絲。<br>
*A local web tool built with Django to record your Instagram followers list — helping you identify who unfollowed you and who your new followers are.* <br>

## 🚀 專案特色 | Features

- 🔍 爬取 Instagram 的追蹤或粉絲名單 
  *Scrape your Instagram following or follower list*
- 💡 爾後再次使用便可偵測新增或取消追蹤者 
  *Detect new followers or unfollowers on subsequent scans*
- 🌐 提供本地端簡易網頁介面操作(基於 Django)
  *Local web interface powered by Django for easy operation*
<br>

## 🖼️ 使用畫面教學 | Demo
![Demo](./static/PNG/7.gif)

<br>

## 🛠️ 安裝與啟動方式 | Installation & Setup

### 第一步：下載專案 | Clone the repository

```bash
git clone https://github.com/quincy408/instagram-follower-tool.git
cd instagram-follower-tool
```
<br>

### 第二步：建立虛擬環境 | Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
<br>

### 第三步：安裝依賴套件 | Install dependencies

```bash
pip install -r requirements.txt
```
<br>

### 第四步：啟動 Django 專案 | Start the Django server

```bash
python manage.py runserver
```

<br>

### 🎉 開啟網址查看頁面 | Open in browser<br>
👉 [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)

