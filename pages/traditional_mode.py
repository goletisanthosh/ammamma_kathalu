#type: ignore
import streamlit as st
from utils.file_handler import save_uploaded_file, save_user_text


try:
    from streamlit_webrtc import webrtc_streamer, WebRtcMode
    WEBSUPPORT = True
except Exception:
    WEBSUPPORT = False

def render_traditional(username: str):
    st.subheader("👵 Traditional Mode")
    st.caption("Contribute by Text / Image / Audio / Video.")

    input_type = st.radio("Choose input type", ["Text", "Image", "Audio", "Video"], horizontal=True)

    if input_type == "Text":
        txt = st.text_area("Type your proverb / story / lore", height=150, placeholder="Type here in any language...")
        if st.button("Submit Text"):
            if not txt.strip():
                st.warning("Please enter some text.")
            else:
                meta = save_user_text(username, "texts", txt.strip())
                st.success("Saved ✅")
                st.json(meta)

    elif input_type == "Image":
        img = st.file_uploader("Upload image (jpg/png)", type=["jpg", "jpeg", "png"])
        if img is not None:
            st.image(img, caption="Preview", use_container_width=True)
        if st.button("Submit Image"):
            if not img:
                st.warning("Please upload an image")
            else:
                meta = save_uploaded_file(username, "images", img)
                st.success("Saved ✅")
                st.json(meta)

    elif input_type == "Audio":
        st.caption("You can upload a file. (Recording via browser is optional and depends on browser support)")
        if WEBSUPPORT:
            webrtc_streamer(key="audio-only", mode=WebRtcMode.SENDONLY, media_stream_constraints={"audio": True, "video": False})
        aud = st.file_uploader("Upload audio (mp3/wav/m4a)", type=["mp3", "wav", "m4a"])
        if st.button("Submit Audio"):
            if not aud:
                st.warning("Please upload an audio file")
            else:
                meta = save_uploaded_file(username, "audio", aud)
                st.success("Saved ✅")
                st.json(meta)

    else:
        st.caption("You can upload a file. (Optional recording if supported)")
        if WEBSUPPORT:
            webrtc_streamer(key="video-only", mode=WebRtcMode.SENDONLY, media_stream_constraints={"audio": True, "video": True})
        vid = st.file_uploader("Upload video (mp4/mov)", type=["mp4", "mov"])
        if vid is not None:
            try:
                st.video(vid)
            except Exception:
                st.info("Video preview not available.")
        if st.button("Submit Video"):
            if not vid:
                st.warning("Please upload a video file")
            else:
                meta = save_uploaded_file(username, "video", vid)
                st.success("Saved ✅")
                st.json(meta)
