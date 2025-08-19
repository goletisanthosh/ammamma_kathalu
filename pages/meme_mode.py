#type: ignore
import streamlit as st
import os, json
from datetime import datetime

MEMES_FOLDER = os.path.join("assets", "memes")
RESPONSES_FILE = os.path.join("data", "user_responses.json")

os.makedirs(MEMES_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

def load_responses():
    if os.path.exists(RESPONSES_FILE):
        try:
            with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_responses(data):
    with open(RESPONSES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def list_memes():
    return [f for f in os.listdir(MEMES_FOLDER) if os.path.isfile(os.path.join(MEMES_FOLDER, f))]

def render_meme_mode(username: str):
    st.subheader("🎭 Meme Mode")
    memes = list_memes()
    if not memes:
        st.info("No memes available yet. Ask admin to upload some to `assets/memes`.")
        return

    selected = st.selectbox("Choose a meme", memes)
    path = os.path.join(MEMES_FOLDER, selected)
    st.image(path, use_container_width=True)

    dialogue = st.text_area("Your dialogue / caption", placeholder="Type in your language...", height=120)

    if st.button("Save Dialogue"):
        if not dialogue.strip():
            st.warning("Please enter a dialogue.")
        else:
            data = load_responses()
            data.append({
                "username": username,
                "meme": selected,
                "dialogue": dialogue.strip(),
                "timestamp": datetime.utcnow().isoformat()
            })
            save_responses(data)
            st.success("Saved ✅")
