from pathlib import Path
from typing import List, Dict
import uuid
import os
import json

UPLOADS_BASE = Path("data/uploads")
UPLOADS_BASE.mkdir(parents=True, exist_ok=True)

MEME_FOLDER = Path("assets/memes")
MEME_FOLDER.mkdir(parents=True, exist_ok=True)

def list_memes() -> List[str]:
    return [p.name for p in MEME_FOLDER.iterdir() if p.is_file()]

def save_meme_file(file) -> str:
    MEME_FOLDER.mkdir(parents=True, exist_ok=True)
    file_id = uuid.uuid4().hex[:8]
    out = MEME_FOLDER / f"{file_id}_{file.name}"
    with out.open("wb") as f:
        f.write(file.getbuffer())
    return out.name

def delete_meme_file(filename: str) -> bool:
    p = MEME_FOLDER / filename
    if p.exists():
        p.unlink()
        return True
    return False

def save_uploaded_file(username: str, folder: str, uploaded_file) -> Dict:
    user_dir = UPLOADS_BASE / username / folder
    user_dir.mkdir(parents=True, exist_ok=True)
    file_id = uuid.uuid4().hex
    out = user_dir / f"{file_id}_{uploaded_file.name}"
    with out.open("wb") as f:
        f.write(uploaded_file.getbuffer())
    return {
        "username": username,
        "folder": folder,
        "filename": uploaded_file.name,
        "saved_path": str(out),
        "file_id": file_id
    }

def save_user_text(username: str, folder: str, text: str):
    import os, uuid, datetime, json
    
    # make folder
    os.makedirs(f"user_data/{username}/{folder}", exist_ok=True)

    # filename
    filename = f"{uuid.uuid4().hex}.txt"
    filepath = f"user_data/{username}/{folder}/{filename}"

    # save text
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    meta = {
        "username": username,
        "folder": folder,
        "filename": filename,
        "saved_at": str(datetime.datetime.now())
    }
    return meta

