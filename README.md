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

## ✨ Core Features

### 🔒 **1. Adaptive Cipher Engine (`cipher_engine.py`)**

- **Full ASCII Support:** Encrypts and decrypts all printable ASCII characters (32-126), including uppercase letters, lowercase letters, digits, and symbols.
- **Uniform Shifting:** Implements a continuous shift across the entire character range, simulating common obfuscation techniques.
- **Robust Validation:** Includes strict key validation and error handling to ensure predictable behavior.

### 🕵️ **2. Automated Cryptanalysis (`breaker.py`)**

- **Brute-Force Attack:** Automatically attempts all 95 possible shifts to find the original plaintext.
- **Frequency-Scoring Algorithm:** Scores each potential decryption against standard English letter frequencies to identify the most probable candidate.
- **Hands-Off Recovery:** Automatically identifies and displays the most likely key, plaintext, and confidence score.

### 📊 **3. Frequency Analyzer (`analyzer.py`)**

- **Statistical Analysis:** Computes the character distribution of any given text.
- **English Language Comparison:** Measures how closely a text's letter frequency matches that of standard English, producing a "deviation score."
- **Demonstrates Weakness:** Clearly illustrates the statistical weaknesses inherent in simple substitution ciphers.

### 🛠️ **4. Interactive CLI (`main.py`)**

- **Menu-Driven Interface:** A simple, interactive command-line menu to access all major functions:
  - Encrypt text with a key.
  - Decrypt text with a key.
  - Automatically break a cipher.
  - Perform frequency analysis on text.

---

## 📁 Project Structure

The project is organized into clear, single-responsibility modules.

```
/
├── src/
│   ├── main.py             # Interactive CLI entry point
│   ├── cipher_engine.py    # Core encryption/decryption engine
│   ├── breaker.py          # Automated cryptanalysis module
│   └── analyzer.py         # Frequency analysis tools
│
├── tests/
│   └── test_cipher.py      # Unit tests for the cipher engine
│
├── docs/
│   └── design_notes.md     # In-depth architecture and design decisions
│
├── requirements.txt        # Project dependencies
└── README.md               # You are here!
```

---

## ▶️ Installation & Usage

### **Installation**

```bash
# 1. Clone the repository
git clone https://github.com/swapnilbrrr/Caesar-Cipher.git
cd caesar_cipher

# 2. Set up a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
# source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### **Running the Tool**

Execute the main script from the project's root directory to launch the interactive menu.

```bash
python src/main.py
```

From the menu, you can choose to **Encrypt**, **Decrypt**, **Break**, or **Analyze** text by following the on-screen prompts.

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

## 🏗️ Project Roadmap & Future Enhancements

This project is designed to be extended. The following features are on the roadmap:

- [x] **Integrate Cipher Breaker:** The `breaker.py` module is now fully integrated into the `main.py` CLI.
- [ ] **Advanced CLI:** Upgrade `main.py` to use `argparse` for powerful command-line subcommands (e.g., `python main.py break <ciphertext>`).
- [ ] **Dictionary-Based Scoring:** Improve the `analyzer` by adding a dictionary lookup to score candidates based on the presence of real English words.
- [ ] **Data Visualization:** Integrate `matplotlib` to create visual charts of frequency distributions.
- [ ] **Expanded Testing:** Add comprehensive unit tests for the `analyzer` and `breaker` modules.
- [ ] **Category-Based Shifting:** Enhance the `cipher_engine` to support independent shifting for different character types (A-Z, a-z, 0-9), more closely mirroring the classic Caesar cipher.
- [ ] **Web Interface:** Build a simple Flask or FastAPI wrapper to demonstrate the toolkit in a web browser.

---

## 📄 License

This project is released under the **MIT License**.
Feel free to use, modify, and expand.

