import os

LINE = "One star. He asks me to write 500 words, deletes 499, and calls the last one his idea."

assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry must be 1-200 non-blank chars"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
