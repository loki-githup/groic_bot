# greeting.py
import random

WELCOME_POOL = [
    "Welcome @USERNAME! Good to see you! 🎉",
    "Hey @USERNAME, welcome to the room! 🥰",
]

def generate_greeting(username: str) -> str:
    if not username:
        username = "Guest"
    clean_name = username.strip().replace("@", "")
    msg = random.choice(WELCOME_POOL)
    return msg.replace("@USERNAME", "@" + clean_name)