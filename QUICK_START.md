# Quick Start

## 1. Create a virtual environment
### Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2. Install dependencies
```powershell
pip install -r requirements.txt
```

## 3. Add your API key
Copy `.env.example` to `.env` and add your OpenAI API key:

```text
OPENAI_API_KEY=your_key_here
```

## 4. Run the sample analysis
```powershell
python simple_ci_agent.py --input sample_magic_school_notes.md --output output/magicschool_generated_report.md
```

## 5. Open the result
Check the generated file in the `output/` folder.

## 6. Create your own report
- Copy `templates/source_notes_template.md`
- Fill it with notes for SchoolAI or Brisk
- Run the same command with your new file
