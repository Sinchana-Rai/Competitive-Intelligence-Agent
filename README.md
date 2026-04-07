# Competitive Intelligence Agent for Colleague AI
AA beginner-friendly project to build a **Colleague AI Competitive Intelligence Agent** that analyzes K–12 education AI competitors and generates structured strategic reports.

## 1) What this project does
This project builds an **AI agent** that acts like a junior product marketer / strategy analyst / competitive analyst for the K–12 AI market.

Its job is to:
- collect competitor information
- analyze product positioning and messaging
- compare competitors to Colleague AI
- assess threat level (Low / Medium / High)
- generate strategic recommendations
- produce structured competitor reports

Your 3 target competitors are:
1. MagicSchool
2. SchoolAI
3. Brisk Teaching

---

## 2) What an "agent" means in this project
An agent performs **4 key steps**:

1. **Collect information**  
   (websites, pricing, blogs, etc.)

2. **Analyze information**  
   (identify positioning, audience, strengths)

3. **Decide what matters**  
   (evaluate competitive threat)

4. **Output a useful result**  
   (structured report + recommendations)

---

## 3) System Architecture
### End-to-End Workflow

Public Websites -> Scraper (fetch_schoolai.py) -> Raw Data (data_sources/) -> Notes Builder (build_notes.py) -> Structured Notes (.md) -> AI Agent (simple_ci_agent.py) -> LLM (Groq / OpenAI) -> Final Report (output/)

---

## 4) Key Components
1. Data Collection Layer (NEW)
Automatically collects competitor data from public websites
Uses:
requests
BeautifulSoup

File:
scraper/fetch_schoolai.py

2. Source Notes Layer
Converts raw scraped text into structured markdown notes

File:
scraper/build_notes.py

Output:
schoolai_notes.md

3. Prompt Layer
Defines how AI should analyze data

File:
agent_prompt.txt

4. Agent Layer
Main processing engine

File:
simple_ci_agent.py

Responsibilities:
read notes
read prompt
call LLM
generate report

5. LLM Layer
Groq or OpenAI processes data
Performs reasoning and structured analysis

6. Output Layer
Final reports saved as:
output_schoolai.md
output_magic_school.md
output_brisk.md

---

## 5) Project Structure
```text
colleague_ai_ci_starter/
│
├── scraper/
│   ├── fetch_schoolai.py
│   └── build_notes.py
│
├── data_sources/
│   └── schoolai/
│
├── templates/
│
├── output/
│
├── simple_ci_agent.py
├── agent_prompt.txt
├── schoolai_notes.md
├── sample_magic_school_notes.md
├── requirements.txt
└── README.md
```
---

## 6) Installation
Step 1 — Clone / open project
cd colleague_ai_ci_starter

Step 2 — Install dependencies
pip install -r requirements.txt
pip install groq python-dotenv beautifulsoup4 requests

Step 3 — Add API key
Create .env file:
GROQ_API_KEY=your_api_key_here

---

## 7) Execution
Step 1 — Scrape competitor data
cd scraper
python fetch_schoolai.py

Output:
data_sources/schoolai/page_1.txt

Step 2 — Build notes automatically
python build_notes.py

Output:
schoolai_notes.md

Step 3 — Run AI agent
cd ..
python simple_ci_agent.py --input schoolai_notes.md --output output_schoolai.md

Step 4 — View report
Open:
output_schoolai.md


---

## 8) Alternative
You can skip scraping and use:
sample_magic_school_notes.md

Then run:
python simple_ci_agent.py --input sample_magic_school_notes.md --output output_magic_school.md

---

## 9) Data Source Strategy
For each competitor, collect:
- homepage
- product/features page
- pricing or district page
- one blog/news/update page

This ensures:
- reliable data
- clean analysis
- easy explanation

---

## 10) Output Format
Each report includes:

**Competitor Snapshot**
- product
- buyer
- use case
**Positioning Analysis**
- messaging
- target audience
**Comparison to Colleague AI**
**Threat Assessment**
- Low / Medium / High
**Recent Updates**
**Strategic Recommendation**


---

## 11) 11) Why this is a real AI agent
This system:
✔ accepts input
✔ applies reasoning
✔ makes decisions
✔ produces structured output

---

## 12) Business Value
This project helps:
- product teams track competitors
- strategy teams make decisions
- organizations reduce manual analysis effort

---

## 13) Future Improvements
1. Weekly Automation (Real Agent Behavior)
- schedule scraper (cron job / scheduler)
- auto-refresh data weekly
- auto-generate updated reports
- send alerts on major changes

2. Improve Notes Quality
- remove noise from scraped data
- extract only relevant sections
- structure notes better before LLM input
- improve accuracy of analysis

3. Multi-Competitor Comparison
- compare all competitors together
- generate side-by-side insights

4. Dashboard / UI
- build simple dashboard (Streamlit)
- visualize competitor trends

5. Historical Tracking
- store previous reports
- track competitor evolution over time

---

## 14) Summary
This project evolves from manual competitive analysis into an automated AI-powered intelligence system capable of monitoring, analyzing, and responding to competitor activity.
