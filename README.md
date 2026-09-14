# CodeAlpha Python Internship Projects

This repository contains all 3 completed Python programming tasks for the **CodeAlpha Internship**. Each task is organized in its own folder with dedicated source code.

---

## 📁 Repository Structure

* **`CodeAlpha_Hangman/`** — Task 1: Hangman Game
* **`CodeAlpha_StockPortfolioTracker/`** — Task 2: Stock Portfolio Tracker
* **`CodeAlpha_TaskAutomation/`** — Task 3: Email Extractor Script

---

## 🛠️ Task Explanations & Key Features

### 1. Hangman Game (`CodeAlpha_Hangman`)
* **Goal:** A text-based console game where players guess a secret word letter by letter.
* **Features:**
  * Predefined list of secret words picked randomly using Python's `random` module.
  * Guess limit set strictly to 6 incorrect attempts.
  * Input validation to ensure valid single-letter inputs.
* **Core Concepts:** `random.choice`, `while` loop, `if-else` statements, list operations, string iteration.

### 2. Stock Portfolio Tracker (`CodeAlpha_StockPortfolioTracker`)
* **Goal:** An interactive tool to calculate total stock portfolio investments using defined stock market prices.
* **Features:**
  * Hardcoded price lookup table (Dictionary) for stock symbols (e.g., AAPL, TSLA, GOOGL, MSFT, AMZN).
  * Interactive quantity entry with real-time total portfolio calculation.
  * Automated generation of a text summary report saved locally (`portfolio_summary.txt`).
* **Core Concepts:** Dictionaries, `try-except` error handling, mathematical operations, file writing (`open()`).

### 3. Task Automation - Email Extractor (`CodeAlpha_TaskAutomation`)
* **Goal:** An automated utility script that parses text files to extract email addresses and organize them into an output document.
* **Features:**
  * Auto-generates a sample input file if none exists for quick testing.
  * Regex search pattern to scan, identify, and extract clean email addresses.
  * Filters out duplicate email entries and outputs results into `extracted_emails.txt`.
* **Core Concepts:** Regular Expressions (`re` module), OS path checking (`os.path`), file I/O operations.
