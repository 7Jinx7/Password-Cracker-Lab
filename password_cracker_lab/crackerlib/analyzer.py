# Author: Sanjana Suresh

import csv
from crackerlib.constants import GUESSES_PER_SECOND, LOWERCASE, UPPERCASE, DIGITS, SYMBOLS

class PasswordAnalyzer: # Base class
    def __init__(self, filepath):
        self.filepath = filepath
        self.passwords = []

    def load_passwords(self): # Loaading the CSV
        with open(self.filepath, newline='', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    self.passwords.append(row[0].strip())

    def basic_stats(self): # Stats frrom the dataset
        stats = {
            "Breaking down the dataset:\n"
            "total number of passwords": len(self.passwords),
            "lowercase_only": 0,
            "letters_and_digits": 0,
            "symbols_present": 0,
            "length_over_12": 0
        }

        for pw in self.passwords: 
            has_digit = any(c.isdigit() for c in pw)
            has_alpha = any(c.isalpha() for c in pw)
            has_symbol = any(c in SYMBOLS for c in pw)

            # Analyzing each pwd
            if pw.islower() and pw.isalpha():
                stats["lowercase_only"] += 1
            if has_alpha and has_digit and not has_symbol:
                stats["letters_and_digits"] += 1
            if has_symbol:
                stats["symbols_present"] += 1
            if len(pw) >= 12:
                stats["length_over_12"] += 1

        return stats

class BruteForceAnalyzer(PasswordAnalyzer): 

    def estimate_crack_time(self, password): # Crack pwd --> record time 
        charset = 0
        if any(c in LOWERCASE for c in password):
            charset += len(LOWERCASE)
        if any(c in UPPERCASE for c in password):
            charset += len(UPPERCASE)
        if any(c in DIGITS for c in password):
            charset += len(DIGITS)
        if any(c in SYMBOLS for c in password):
            charset += len(SYMBOLS)

        if charset == 0:
            return 0

        guesses = charset ** len(password)
        return guesses / GUESSES_PER_SECOND


    def improvement_suggestions(self, password): # Stronger pwd suggestion
        suggestions = []

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in SYMBOLS for c in password)

        # print("Try adding some ")
        if not has_upper:
            suggestions.append(" uppercase letters")
        if not has_lower:
            suggestions.append(" lowercase letters")
        if not has_digit:
            suggestions.append(" numbers")
        if not has_symbol:
            suggestions.append(" special characters")
        if len(password) < 12:
            suggestions.append(" length to your password")

        if not suggestions:
            return "Nice! Your password uses a strong mix of characters."

        return "Try adding some " + ", and ".join(suggestions) + " to make it even stronger!"
    

    def strength_label(self, seconds): # Label for pwd strength
        if seconds < 1:
            return "Instantly Cracked 💀"
        elif seconds < 3600:
            return "Very Weak 😭"
        elif seconds < 86400:
            return "Weak 👎"
        elif seconds < 31536000:
            return "Moderate 🙃"
        else:
            return "Strong! 🥳"

    
