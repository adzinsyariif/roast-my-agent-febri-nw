import os

LINE = "My agent is so autonomous it hallucinates the tool call, apologizes to the hallucination, and marks the task complete."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
