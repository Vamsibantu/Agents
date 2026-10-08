# Groq Command-Line Assistant

A minimal interactive command-line assistant powered by Groq and the
`openai/gpt-oss-20b` model.

## Requirements

- Python 3.9 or newer
- A Groq API key

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install groq python-dotenv
```

Create a `.env` file in the repository root:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit the `.env` file or share the API key.

## Run

Start the assistant with:

```powershell
python agent.py
```

Enter a question at the prompt. Type `exit` to stop the program. The
assistant displays each response along with cumulative input, output, and
total token counts.

## Behavior

- Empty queries are rejected.
- The assistant uses a concise system instruction and retains a short recent
  conversation context.
- API errors are printed to the console without terminating the chat loop.

## Project Structure

```text
.
├── agent.py
└── README.md
```