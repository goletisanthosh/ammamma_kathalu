# Ammamma Kathalu 🎙️

**Ammamma Kathalu** is a community-driven voice collection app built with **Streamlit**.  
It focuses on collecting **regional language data** in two fun modes:  

- **Traditional Mode** → Users can record and save cultural proverbs, folk tales, and stories.  
- **Meme Mode** → Users can upload meme-style audio/video in their local language.  

The project is aimed at **low-network rural areas** with offline compatibility.

---

## 🚀 Features
- 📱 Mobile-friendly Streamlit UI.
- 🔐 Sign-up & Sign-in flow.
- 🏠 Home page with two modes:
  - Traditional Mode (stories & proverbs).
  - Meme Mode (images/videos).
- 💾 Local storage for user data (lightweight JSON/CSV).
- 🌐 Low internet support.
- 📊 Ready for future AI/NLP integration.

---

## 📂 Project Structure
ammamma_kathalu/
├─ app.py
├─ pages/
│  ├─ traditional_mode.py
│  ├─ meme_mode.py
│  └─ admin_panel.py
├─ auth/
│  └─ auth_handler.py
├─ utils/
│  └─ file_handler.py
├─ assets/
│  └─ memes/           # static meme images
├─ data/
│  ├─ users.json       # local users store
│  └─ uploads/         # user submissions
├─ README.md
├─ CONTRIBUTING.md
├─ CHANGELOG.md
├─ LICENSE
└─ requirements.txt

## 🛠️ Tech Stack
- **Frontend/Backend**: Streamlit (Python)
- **Database**: SQLite (or Firebase for cloud support)
- **Storage**: Local file system (extendable to cloud)
- **Styling**: Custom CSS for mobile-friendly UI

---

## 📱 Usage
1. Login or Sign up as a new user.
2. By default, you’ll enter **Traditional Mode (Ammamma Kathalu)**.
3. Toggle to **Meme Mode** if you want to upload/share memes.
4. Access menu options (Profile, Admin, Logout) from the floating menu button.

---

## 🏗️ Installation
Clone this repository:
```bash
git clone https://github.com/yourusername/ammamma-kathalu.git
cd ammamma-kathalu

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py

Screenshots:

￼

￼

￼

Author:
Santhosh Goleti (B.Tech AIML Student, JB Institute of Engineering and Technology)
📧 Email: devaiah670@gmail.com
