# Author: Sanjana Suresh
# Rubn to generate output file locally

from crackerlib.analyzer import BruteForceAnalyzer

DATA_FILE = "data/common_passwords.csv"
OUTPUT_FILE = "output/report.txt"

analyzer = BruteForceAnalyzer(DATA_FILE) # callling the class
analyzer.load_passwords()
user_password = input("Enter password here: ")
seconds = analyzer.estimate_crack_time(user_password)
label = analyzer.strength_label(seconds)
suggestion = analyzer.improvement_suggestions(user_password)
stats = analyzer.basic_stats()

with open(OUTPUT_FILE, "w") as out: # Generate and write to output file
    out.write("Password Cracker Lab Report\n")
    out.write("===========================\n")
    out.write("\nYour Password Analysis: \n")
    out.write(f"Password Entered: {user_password}\n")
    out.write(f"Estimated crack time (seconds): {seconds}\n")
    out.write(f"Strength rating: {label}\n")
    out.write(f"Suggestion: {suggestion}\n")
    out.write("----------------------\n")
    out.write("----------------------\n")

    for key, value in stats.items():
        out.write(f"{key}: {value}\n")

print("Report generated in output/report.txt")
