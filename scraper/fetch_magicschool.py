import requests
from bs4 import BeautifulSoup
from pathlib import Path

URLS = [
    "https://www.magicschool.ai/",
    "https://www.magicschool.ai/magic-tools",
    "https://www.magicschool.ai/magicschool-for-districts",
    "https://www.magicschool.ai/pricing",
    "https://www.magicschool.ai/blog-posts/ai-teaching-tools-updates-2026".
    "https://www.magicschool.ai/blog-posts/strengthening-teaching-and-learning-with-ai"
]

OUTPUT_DIR = Path("../data_sources/magicschoolai")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_text(text):
    return " ".join(text.split())

def extract_page_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    parts = []

    for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
        text = clean_text(tag.get_text(" ", strip=True))
        if len(text) > 20:
            parts.append(text)

    return "\n".join(parts)

for i, url in enumerate(URLS, start=1):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    text = extract_page_text(response.text)

    file = OUTPUT_DIR / f"page_{i}.txt"
    file.write_text(text, encoding="utf-8")

    print(f"Saved: {file}")