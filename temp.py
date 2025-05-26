import os
from openai import OpenAI

import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Colors and styles
BG_COLOR = "#222831"
USER_COLOR = "#00adb5"
BOT_COLOR = "#eeeeee"
TEXT_COLOR = "#393e46"
FONT = ("Segoe UI", 11)
ENTRY_BG = "#393e46"
BUTTON_BG = "#00adb5"
BUTTON_FG = "#ffffff"

def chat_with_gpt(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()

def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)
    root.update()
    response = chat_with_gpt(user_input)
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Chatbot: " + response + "\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

# Set up the main window
root = tk.Tk()
root.title("TalkToMe Chatbot")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Chat window
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=60, height=20, wrap=tk.WORD,
                                        bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, bd=0, padx=10, pady=10)
chat_window.pack(padx=10, pady=10)

# Tag configurations for colored messages
chat_window.tag_configure("user", foreground=USER_COLOR, font=(FONT[0], FONT[1], "bold"))
chat_window.tag_configure("bot", foreground=BOT_COLOR, font=FONT)

# Entry and button frame
bottom_frame = tk.Frame(root, bg=BG_COLOR)
bottom_frame.pack(fill=tk.X, padx=10, pady=(0,10))

user_entry = tk.Entry(bottom_frame, width=45, font=FONT, bg=ENTRY_BG, fg=BOT_COLOR, bd=2, relief=tk.FLAT, insertbackground=BOT_COLOR)
user_entry.pack(side=tk.LEFT, padx=(0, 10), pady=5, ipady=6)
user_entry.bind("<Return>", send_message)

send_button = tk.Button(bottom_frame, text="Send", command=send_message,
                        bg=BUTTON_BG, fg=BUTTON_FG, font=(FONT[0], FONT[1], "bold"),
                        activebackground="#007a8a", activeforeground=BUTTON_FG, bd=0, padx=16, pady=6, cursor="hand2")
send_button.pack(side=tk.LEFT)

# Focus on the entry box at startup
user_entry.focus()

root.mainloop()
