#!/usr/bin/env python3
"""
Render 入口 — Flask web server + ema99_bot 背景執行
"""
import threading
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "EMA99 Bot is running ✅"

@app.route("/health")
def health():
    return "ok", 200

def start_bot():
    import ema99_bot
    ema99_bot.main()

if __name__ == "__main__":
    # 背景執行交易 bot
    t = threading.Thread(target=start_bot, daemon=True)
    t.start()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
