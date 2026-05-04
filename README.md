<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=LocalDrop&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Wireless%20File%20Transfer%20over%20LAN&descAlignY=60&descSize=18" width="100%"/>

# 📡 LocalDrop

**Transfer files between any devices on the same WiFi — no cables, no cloud, no nonsense.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)](https://github.com/BhavneeshBanga)

</div>

---

## ✨ What is LocalDrop?

**LocalDrop** is a lightweight Flask web app that lets you transfer files wirelessly between your phone, laptop, or any device — as long as they're on the **same WiFi network**.

No Bluetooth pairing. No USB cables. No uploading to Google Drive. Just open a browser and send.

---

## 🚀 Features

- 📤 Upload **multiple files** at once from any device
- 📂 Browse and **download** previously uploaded files
- 📱 Works on **mobile browsers** — no app needed
- ⚡ Runs **locally on your network** — fast & private
- 🔒 No internet required — your files never leave your LAN

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

---

## ⚙️ Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/BhavneeshBanga/LocalDrop.git
cd LocalDrop
```

### 2. Install dependencies

```bash
pip install flask
```

### 3. Run the server

```bash
python app.py
```

### 4. Open on your phone

Make sure your phone and laptop are on the **same WiFi**, then open:

```
http://<your-laptop-ip>:5173
```

> 💡 Find your laptop IP:
> - **Windows** → `ipconfig` → look for IPv4 Address
> - **Mac/Linux** → `ifconfig` or `ip a`

---

## 📁 Project Structure

```
LocalDrop/
├── app.py                  # Flask backend
├── uploads/                # Uploaded files stored here
└── templates/
    └── index.html          # Frontend UI
```

---

## 📸 How it works

```
📱 Phone (browser)                    💻 Laptop (Flask server)
       |                                        |
       |  --- POST /upload (file) ---------->  |
       |                                        |  saves to /uploads
       |  <-- ✅ Upload success! -------------  |
       |                                        |
       |  --- GET /files -------------------->  |
       |  <-- 📂 List of files  -------------  |
       |                                        |
       |  --- GET /download/<file> -------->   |
       |  <-- 📥 File download -------------   |
```

---

## 🔮 Roadmap

- [ ] Drag & drop UI
- [ ] Progress bar for large files
- [ ] QR code for easy mobile access
- [ ] Password protection
- [ ] File expiry / auto-delete

---

## 👨‍💻 Author

**Bhavneesh Banga** — B.Tech CSE 2nd Year

[![GitHub](https://img.shields.io/badge/GitHub-BhavneeshBanga-181717?style=flat&logo=github)](https://github.com/BhavneeshBanga)
[![LeetCode](https://img.shields.io/badge/LeetCode-BhavneeshBanga-FFA116?style=flat&logo=leetcode&logoColor=black)](https://leetcode.com/BhavneeshBanga)

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>