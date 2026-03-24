import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

SYSTEM_PROMPT = Path("agent_prompt.txt").read_text(encoding="utf-8")


def build_user_prompt(source_notes: str) -> str:
    return f"""
Analyze the following competitor source notes and generate a structured competitive intelligence report.

SOURCE NOTES
============
{source_notes}
""".strip()


def generate_report(source_notes: str, model: str = "llama-3.1-8b-instant") -> str:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is missing. Add it to your .env file.")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(source_notes)},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content or ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Competitive Intelligence Agent for Colleague AI")
    parser.add_argument("--input", required=True, help="Path to source notes markdown/txt file")
    parser.add_argument("--output", required=True, help="Path to save generated markdown report")
    parser.add_argument("--model", default="llama-3.1-8b-instant", help="Groq model name")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    source_notes = input_path.read_text(encoding="utf-8")
    report = generate_report(source_notes=source_notes, model=args.model)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"Report written to: {output_path}")


if __name__ == "__main__":
    main()