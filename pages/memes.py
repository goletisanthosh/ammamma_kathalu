#type: ignore

import streamlit as st
import os
from utils.storage import load_memes, UPLOAD_FOLDER

def show_memes():
    st.title("😂 Meme Gallery")
    memes = load_memes()
    if not memes:
        st.warning("No memes uploaded yet!")
    else:
        for meme in memes:
            st.image(os.path.join(UPLOAD_FOLDER, meme), width=300)
