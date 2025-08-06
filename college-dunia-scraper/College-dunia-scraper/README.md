# CollegeDunia JEE Main College Predictor Scraper

A Python + Selenium tool to scrape college prediction results from CollegeDunia JEE Main Predictor based on your rank, category, and state.

---

## 🚀 Features

- Auto form submission (category, home state, rank)
- Infinite scroll support to fetch all colleges
- Extracts:
  - College Name
  - Location
  - Two Branches and their Fees
  - Direct College Link
- Saves results to `college_results.csv`

---

## 🛠 Requirements

- Python 3.8+
- Google Chrome (latest)
- ChromeDriver (matching your Chrome version)
- `selenium`, `pandas` (install via pip)

---

## 📦 Installation

1. Clone this repo or download the script.
2. Install dependencies:
    ```bash
    pip install selenium pandas
    ```
3. Download ChromeDriver and update the script path:
    ```python
    path = r"C:\path\to\chromedriver.exe"
    ```

---

## ▶️ Usage

Run the script:
```bash
python College_scraper.py
```
Results will be saved as `college_results.csv` in the project folder.

---

## 📁 Output CSV Format

| College Name | Location | Branch 1 | Fees 1 | Branch 2 | Fees 2 | Link |

---

## ⚠️ Notes

- Update ChromeDriver if Chrome updates.
- If the site structure changes, update the XPaths.
- For educational purposes only.

