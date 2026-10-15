# -*- coding: utf-8 -*-
"""مشغّل البوت — يفك ضغط الكود من الأجزاء ثم يشغّل bot.py"""
import base64, glob, io, os, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))

def extract_bot():
    parts = sorted(glob.glob(os.path.join(HERE, "part_*")))
    if not parts:
        print("ERROR: no part_* files found!")
        sys.exit(1)
    b64 = "".join(open(p, "r", encoding="ascii").read().strip() for p in parts)
    raw = base64.b64decode(b64)
    zipfile.ZipFile(io.BytesIO(raw)).extractall(HERE)
    print("Bot files extracted OK:", len(raw), "bytes")

extract_bot()
os.chdir(HERE)
os.execv(sys.executable, [sys.executable, os.path.join(HERE, "bot.py")])
