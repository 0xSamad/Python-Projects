# MyPass v2 — Password Manager
A password manager built with Python's `tkinter`. Generate strong random passwords, save your website credentials, and search saved entries — all stored locally in JSON.

![Demo](demo/demo.gif)

## How It Works
1. Enter the website name and your email/username in the input fields.
2. Click **Generate Password** to create a strong random password, or type your own.
3. Click **ADD** to save the entry — you'll be asked to confirm the details before they're stored.
4. Click **Search** after entering a website name to instantly retrieve its saved email and password.
5. Your credentials are saved locally in `passwords.json` so you can look them up anytime.

## What's New in v2
- Migrated storage from `.txt` to `.json` for structured, reliable read/write
- Added a **Search** feature to look up saved credentials by website
- Fixed empty-field validation bug
- Fixed file read/write crashes on missing or empty data files

## Tech Used
- Python
- `tkinter` (standard library)
- `random` (standard library)
- `json` (standard library)

## Run It Locally
```bash
python main.py
```
Make sure `logo.png` is in the same folder as `main.py`. No external dependencies required — just a standard Python installation.

## License
Feel free to use, modify, or build on this project.
