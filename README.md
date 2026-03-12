# 🎲 Articulate Card Generator (Streamlit)

A mobile-friendly, browser-based version of **Articulate-style** clue cards — built to replace physical cards with a fast, no-install web app. Generate random cards by category, roll a virtual die to choose a category, and run a timed round with **Correct / Skip** tracking.

## ✨ Features

- **Random card generation** from a CSV dataset
- **Category die roll** (auto-selects a category for you)
- **Round mode**
  - ✅ Correct counter
  - ⏭️ Skip counter
  - 🧾 End-of-round summary + reset
- **Mobile-friendly UI** (works great as an “add to home screen” web app)
- **Easy content updates**: edit `cards.csv` without changing code

## 🧰 Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **CSV-based content store**

## 📁 Project Structure


.
├── app.py # Streamlit app entrypoint
├── cards.csv # Card dataset (categories + prompts)
├── requirements.txt # Dependencies
└── README.md


## ✅ Getting Started (Local)

### 1) Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
2) Create & activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
3) Install dependencies
pip install -r requirements.txt
4) Run the app
streamlit run app.py

Streamlit will open the app in your browser.

🗃️ Editing / Adding Cards

Cards are stored in cards.csv.
At minimum you’ll want columns like:

category (e.g., Person / Action / Object / Nature / World — whatever your set uses)

card (the clue text)

Example:

category,card
Person,David Attenborough
Action,Doing the Macarena
Object,Toaster

If your CSV uses different column names, update the column references in app.py.

🚀 Deploy (Streamlit Community Cloud)

Push your repo to GitHub

Go to Streamlit Community Cloud and deploy from your repo

Set:

Main file path: app.py

Add your dependencies in requirements.txt

🧠 Notes / Roadmap Ideas

Timed rounds with a countdown timer

Team scoring + multiple rounds

Difficulty modes (easy/medium/hard)

“No repeats” mode or recently-used card history

Upload a custom CSV via the UI

📜 License

Choose one:

MIT License (recommended for open source)

Or keep it private / “All Rights Reserved”

Built for fun, speed, and portability — because the cards always run out mid-game.


