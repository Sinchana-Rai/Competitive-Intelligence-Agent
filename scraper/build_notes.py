from pathlib import Path

SOURCE_DIR = Path("../data_sources/schoolai")
OUTPUT_FILE = Path("../schoolai_notes.md")

notes = ["# Competitor Notes: SchoolAI\n"]

for file_path in sorted(SOURCE_DIR.glob("page_*.txt")):
    content = file_path.read_text(encoding="utf-8")

    notes.append(f"## Source: {file_path.name}\n")
    notes.append(content[:3000])  # limit size
    notes.append("\n")

OUTPUT_FILE.write_text("\n".join(notes), encoding="utf-8")

print("✅ Built schoolai_notes.md")