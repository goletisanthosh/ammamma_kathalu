# pages/admin_panel.py
#type: ignore

import streamlit as st
import os, json
from utils.file_handler import list_memes, save_meme_file, delete_meme_file

RESPONSES_FILE = os.path.join("data", "user_responses.json")

def load_responses():
    if os.path.exists(RESPONSES_FILE):
        try:
            with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def render_admin_panel(username: str):
    st.title("👑 Admin Panel")
    st.caption("Manage meme templates and view user submissions.")

    st.subheader("Add Meme Template")
    mf = st.file_uploader("Upload meme (jpg/png)", type=["jpg", "jpeg", "png"], key="admin_meme_up")
    if mf and st.button("Upload Meme"):
        name = save_meme_file(mf)
        st.success(f"Uploaded: {name}")

    st.subheader("Existing Memes")
    memes = list_memes()
    if not memes:
        st.info("No memes in assets/memes.")
    else:
        for m in memes:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(m)
            with col2:
                if st.button("Delete", key=f"del_{m}"):
                    if delete_meme_file(m):
                        st.success(f"Deleted {m}")
                        st.rerun()

    st.subheader("Recent Dialogues")
    data = load_responses()
    if not data:
        st.info("No user dialogues yet.")
    else:
        for item in data[-50:][::-1]:
            st.markdown(f"**{item.get('username','?')}** on **{item.get('meme','?')}**")
            st.write(item.get("dialogue",""))
            st.caption(item.get("timestamp",""))
            st.divider()
