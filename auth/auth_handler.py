import json
from pathlib import Path
from typing import Optional, Dict, List

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "users.json"

def load_users() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

def save_users(users: List[Dict]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def get_profile(username: str) -> Dict:
    for u in load_users():
        if u.get("username") == username:
            return {
                "username": u.get("username"),
                "name": u.get("name", u.get("username")),
                "email": u.get("email", ""),
                "role": u.get("role", "user"),
            }
    return {}

def add_user(username: str, password: str, *, name: str = "", email: str = "", role: str = "user") -> bool:
    users = load_users()
    if any(u.get("username") == username for u in users):
        return False
    users.append({
        "username": username,
        "password": password,
        "name": name or username,
        "email": email,
        "role": role
    })
    save_users(users)
    return True

# Backwards-compat
create_user = add_user

def validate_user(username: str, password: str) -> Optional[Dict]:
    for u in load_users():
        if u.get("username") == username and u.get("password") == password:
            return u
    return None

def ensure_admin_user() -> None:
    users = load_users()
    if not any(u.get("username") == "admin" for u in users):
        users.append({
            "username": "admin",
            "password": "admin123",
            "name": "Administrator",
            "email": "",
            "role": "admin"
        })
        save_users(users)

def get_profile(username):
    """Fetch user profile details by username."""
    users = load_users()
    for u in users:
        if u["username"] == username:
            return {
                "username": u["username"],
                "name": u.get("name", ""),
                "email": u.get("email", "")
            }
    return None
