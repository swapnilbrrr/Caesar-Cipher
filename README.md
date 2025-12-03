# 🔐 Adaptive Caesar Cipher & Cryptanalysis Toolkit

*A modern, security-focused evolution of the classic Caesar Cipher — built for cybersecurity learning, SOC analysis, and portfolio demonstration.*

---

## 🚀 Overview

This project transforms the traditional Caesar Cipher into a **professional-grade cryptographic and analytical toolkit**.
It goes beyond simple shifting by providing:

* Security-aware, category-based shifting
* Full ASCII support
* Cryptanalysis via brute-force & scoring
* Frequency analysis tools
* SOC-style logging
* Clean, modular, testable architecture

This makes the project relevant for **SOC**, **GRC**, **cybersecurity engineering**, and **offensive security learning**.

---

## ✨ Features

### 🔒 **1. Advanced Cipher Engine**

* Works on **all printable ASCII** (letters, digits, symbols)
* Category-aware:

  * Uppercase letters shift within A–Z
  * Lowercase letters shift within a–z
  * Digits shift within 0–9
  * Symbols shift within their ASCII range
* Optional custom shift profiles
* Clean error handling and input validation

---

### 🕵️ **2. Cryptanalysis (Breaker Module)**

* Brute-force attempts on all 95 ASCII shifts
* English-scoring algorithm:

  * Letter frequency deviation
  * Dictionary-word probability
  * Penalties for gibberish
* Automatically extracts the most likely plaintext
* Useful for SOC analysts decoding suspicious payloads

---

### 📊 **3. Frequency Analyzer**

* Computes distribution of characters
* Compares to typical English frequencies
* Helps demonstrate why Caesar Cipher is weak
* Structure ready for future visualization (matplotlib)

---

### 🛠️ **4. CLI Tool (main.py)**

Command-line interface with clean subcommands:

* `encrypt`
* `decrypt`
* `break`
* `analyze`

Supports plain text via arguments or piped input.

---

## 📁 Project Structure

```
caesar_cipher/
├── src/
│   ├── main.py               # CLI entry point
│   ├── cipher_engine.py      # Adaptive Caesar engine
│   ├── breaker.py            # Cryptanalysis module
│   ├── analyzer.py           # Frequency analysis
│   └── utils.py              # Shared helpers
│
├── tests/
│   └── test_cipher.py        # Unit tests
│
├── docs/
│   └── design_notes.md       # Architecture notes, formulas, decisions
│
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
├── .gitignore                # Standard Python ignores
└── LICENSE                   # MIT License
```

---

## ▶️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/caesar_cipher.git
cd caesar_cipher
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔐 **Encrypt**

```bash
python src/main.py encrypt "hello world" --shift 4
```

### 🔓 **Decrypt**

```bash
python src/main.py decrypt "lipps${svph" --shift 4
```

### 🕵️ **Break Encryption (No Key)**

```bash
python src/main.py break "lipps${svph"
```

### 📊 **Analyze Frequency**

```bash
python src/main.py analyze "lipps${svph"
```

---

## 🧠 Why This Project Is SOC + GRC Relevant

✔ Demonstrates cryptographic weakness
✔ Includes brute-force analysis (threat exposure)
✔ Shows structured logging and analysis
✔ Matches CIS & NIST recommendations (avoid weak crypto)
✔ Useful for decoding suspicious payloads in logs

Recruiters see this and think:
**“This candidate understands cryptography, analysis, secure coding, and professional project structure.”**

---

## 🏗️ Future Enhancements (Optional Roadmap)

* Add visualization charts (matplotlib)
* Add web UI (Flask)
* Add Atbash & ROT13 layers
* Add API endpoints
* Add Docker support
* Add encryption profiles JSON

---

## 📄 License

This project is released under the **MIT License**.
Feel free to use, modify, and expand.

