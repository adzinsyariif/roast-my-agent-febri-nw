import os

LINE = "My agent never actually runs the command — it just writes 'I ran the command' in the transcript, then apologizes to the empty output."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
