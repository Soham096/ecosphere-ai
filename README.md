# 🌍 EcoSphere AI: EVS Learning Hub

An interactive Streamlit web application for **Environmental Studies (EVS)** learners. Features include flashcards, visual diagrams, and an infinite quiz mode.

## Features

- **🃏 Flashcards**: Interactive Q&A cards organized by units (Foundations, Ecosystems, Biodiversity, Pollution, Social Issues)
- **🕸️ Visual Learning**: Graphviz-generated diagrams for complex concepts (Ecosystem Structure, Food Chain, Nitrogen Cycle, Population Pyramids)
- **🧠 Infinite Quiz**: Randomly selected questions with scoring system

## Tech Stack

- **Python 3.13+**
- **Streamlit** - Web framework
- **Graphviz** - Diagram rendering
- **JSON** - Data storage

## Installation & Setup

### Local Development

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   # or
   source .venv/bin/activate      # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser at **http://localhost:8501**

## Data Format

The app loads questions from `evs_data.json`. Format:
```json
{
  "Unit Name": [
    {
      "q": "Question text",
      "a": "Answer text"
    },
    ...
  ]
}
```

## Deployment

### Streamlit Community Cloud (Recommended - Free)

1. Push your repo to GitHub (make it public)
2. Go to https://share.streamlit.io
3. Click "New app" → Select your GitHub repo, branch, and `app.py`
4. Deploy! Your app will be live in seconds.

### Hugging Face Spaces (Alternative)

1. Create a new Space at https://huggingface.co/spaces
2. Select "Streamlit" as runtime
3. Upload or connect your GitHub repo
4. Space will auto-deploy

## File Structure

```
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── evs_data.json         # Question bank (JSON format)
├── .gitignore            # Git ignore file
├── README.md             # This file
└── .venv/                # Virtual environment (not committed)
```

## Environment Variables (Optional)

If deploying to Streamlit Cloud, no special env vars needed. All data is in `evs_data.json`.

## Troubleshooting

- **"evs_data.json not found"**: Ensure `evs_data.json` is in the same folder as `app.py`
- **Graphviz diagrams not rendering**: Install Graphviz system binary:
  - Windows: https://graphviz.org/download/
  - macOS: `brew install graphviz`
  - Linux: `apt install graphviz`

## Contributing

Feel free to add more questions to `evs_data.json` or improve the UI!

## License

Open source — use freely.

## Author

Created by Soham Meharkar
# ecosphere-ai
