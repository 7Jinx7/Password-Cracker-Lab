# 🔐 Password Cracker Lab

## Overview

**Password Cracker Lab** is an educational cybersecurity and data science project designed to demonstrate how weak and predictable passwords can be compromised quickly. Rather than performing real password cracking, the project simulates attacker behavior using statistical analysis and brute-force estimation to teach password hygiene in a safe, ethical way.

The project combines:

* Data analysis on real-world leaked password patterns
* Object-oriented Python programming
* File input/output
* A command-line interface and a lightweight web interface

---

## Project Goals

* Analyze common password patterns using a large real-world dataset
* Simulate how long a password would survive a brute-force attack
* Provide actionable feedback on how to improve weak passwords
* Demonstrate core programming concepts learned during the semester

---

## Dataset

This project uses a publicly available dataset from Kaggle containing the **10,000 most common leaked passwords**.

**Dataset credit:**

* *Shivam Bansal – 10000 Common Passwords*
* Kaggle link:
  [https://www.kaggle.com/code/shivamb/10000-common-passwords](https://www.kaggle.com/code/shivamb/10000-common-passwords)

The dataset is used **only for statistical analysis and educational simulation**. No real accounts are accessed or attacked.

---

## Features

* Loads and analyzes 10,000 real-world passwords
* Computes dataset-wide statistics such as:

  * lowercase-only passwords
  * use of digits and symbols
  * password length distribution
* Estimates brute-force crack time for a user-entered password
* Classifies password strength using decision logic
* Provides personalized suggestions to improve password strength
* Outputs results to a file for reproducibility
* Includes a Flask-based website for interactive use

---

## Technologies Used

* **Python**
* **Flask** (only third-party dependency)
* Python Standard Library (`csv`, file I/O, etc.)
* HTML and CSS (for the web interface)

---

## Project Structure

```
password_cracker_lab/
├── app.py                  
├── main.py                 
├── crackerlib/
│   ├── analyzer.py         
│   └── constants.py        
├── data/
│   └── common_passwords.csv
├── output/
│   └── report.txt
├── templates/
│   └── index.html
└── README.txt
```

---

## How to Run the Project

### Command-Line Version

```bash
python main.py
```

This will:

* Load the dataset
* Analyze password statistics
* Prompt for a user password
* Write results to `output/report.txt`

---

### Website Version

Install Flask (if not already installed):

```bash
pip install flask
```

Run the web app:

```bash
python app.py
```

Then open a browser and go to:

```
http://127.0.0.1:5000
```

---

## Educational Focus

This project emphasizes:

* Object-oriented programming with inheritance
* Iteration and conditional logic
* File input and output
* Data structures (lists, dictionaries, tuples)
* Real-world data analysis
* Ethical cybersecurity education

---

## Disclaimer

This project does **not** perform real password cracking. All results are simulations intended for educational purposes only. The goal is to raise awareness about password security, not to exploit vulnerabilities.
