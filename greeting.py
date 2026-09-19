# greeting.py
import random

WELCOME_POOL = [
    "Welcome to the room @USERNAME! 🎧",
    "Hey @USERNAME, glad you could join! ✨",
    "Welcome @USERNAME! Enjoy the vibe! 🎵",
    "Hello @USERNAME! Welcome aboard! 🌟",
    "Hey @USERNAME! Grab a seat and vibe with us! 🎶",
    "Welcome @USERNAME! Good to see you! 🎉",
    "Hey @USERNAME, welcome to the room! 🎸"
]

def generate_greeting(username: str) -> str:
    if not username:
        username = "Guest"
    clean_name = username.strip().replace("@", "")
    msg = random.choice(WELCOME_POOL)
    return msg.replace("@USERNAME", "@" + clean_name)