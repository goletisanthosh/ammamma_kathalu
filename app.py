# app.py
# Ammamma Kathalu – Streamlit Frontend with Modes + Simple Menu
# type: ignore

import streamlit as st
from auth.auth_handler import create_user, validate_user, ensure_admin_user, get_profile
from pages.traditional_mode import render_traditional
from pages.meme_mode import render_meme_mode
from pages.admin_panel import render_admin_panel

# -----------------------------
# Menu function (only profile, admin, logout)
# -----------------------------
def show_top_right_menu():
    if not st.session_state.get("logged_in"):
        return

    # create a floating column on the top-right
    cols = st.columns([10,1])
    with cols[-1]:
        with st.popover("☰", use_container_width=True):
            username = st.session_state.get("username", "")
            profile = get_profile(username) if username else {}

            st.markdown("### 📋 Menu")
            st.markdown(f"**👤 {profile.get('name', username)}**")
            st.caption(f"📧 {profile.get('email','-')}")
            st.caption(f"Role: {profile.get('role','user')}")

            st.divider()
            if profile.get("role") == "admin":
                if st.button("👑 Admin Panel"):
                    st.session_state.page = "admin"
                    st.rerun()

            if st.button("🚪 Logout"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.session_state.role = None
                st.session_state.page = "select"
                st.rerun()


# -----------------------------
# Session state defaults
# -----------------------------
if "page" not in st.session_state: st.session_state.page = "select"
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "username" not in st.session_state: st.session_state.username = ""
if "role" not in st.session_state: st.session_state.role = None
if "mode" not in st.session_state: st.session_state.mode = "Traditional"
if "show_sidebar" not in st.session_state: st.session_state.show_sidebar = False

ensure_admin_user()

# -----------------------------
# Pages
# -----------------------------
def page_select():
    st.title("Welcome to Ammamma Kathalu")
    st.write("Choose Login or Sign Up to continue")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 Login"):
            st.session_state.page = "login"; st.rerun()
    with col2:
        if st.button("📝 Sign Up"):
            st.session_state.page = "signup"; st.rerun()

def page_signup():
    st.header("Sign Up")
    name = st.text_input("Full name")
    email = st.text_input("Email (optional)")
    username = st.text_input("Choose username")
    password = st.text_input("Choose password", type="password")
    if st.button("Create Account"):
        if not username or not password:
            st.error("Username and password required")
        else:
            ok = create_user(username.strip(), password.strip(), name=name.strip(), email=email.strip())
            if not ok:
                st.error("Username exists")
            else:
                st.success("Account created. Please login.")
                st.session_state.page = "login"; st.rerun()
    if st.button("Back"):
        st.session_state.page = "select"; st.rerun()

def page_login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = validate_user(username.strip(), password.strip())
        if user:
            st.success("Login successful")
            st.session_state.logged_in = True
            st.session_state.username = user.get("username")
            st.session_state.role = user.get("role", "user")
            st.session_state.page = "home"
            st.session_state.mode = "Traditional"   # ✅ default mode after login
            st.rerun()
        else:
            st.error("Invalid credentials or user not found")
    if st.button("Back"):
        st.session_state.page = "select"; st.rerun()

def page_home():
    st.title("Ammamma Kathalu")
    st.write(f"Welcome, {st.session_state.username}")
    show_top_right_menu()

    st.markdown("### Choose Mode")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👵 Traditional Mode"):
            st.session_state.mode = "Traditional"
    with c2:
        if st.button("🎭 Meme Mode"):
            st.session_state.mode = "Meme"
    st.divider()

    if st.session_state.mode == "Traditional":
        render_traditional(st.session_state.username)
    else:
        render_meme_mode(st.session_state.username)
        


# -----------------------------
# Router
# -----------------------------
if st.session_state.page == "select":
    page_select()
elif st.session_state.page == "signup":
    page_signup()
elif st.session_state.page == "login":
    page_login()
elif st.session_state.page == "home":
    if not st.session_state.logged_in:
        st.session_state.page = "login"; st.rerun()
    else:
        page_home()
elif st.session_state.page == "admin":
    if st.session_state.get("role") == "admin":
        render_admin_panel(username=st.session_state.get("username","admin"))
    else:
        st.error("Access denied — admin only.")
        st.session_state.page = "home" if st.session_state.get("logged_in") else "select"
        st.rerun()
else:
    page_select()
