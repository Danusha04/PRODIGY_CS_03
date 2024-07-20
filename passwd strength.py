import tkinter as tk
from tkinter import messagebox
import string
import math

# Common passwords list
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", 
    "password1", "123123", "qwerty", "abc123", "football", "monkey", 
    "letmein", "dragon", "111111", "baseball", "iloveyou"
]

# Dictionary words (a small sample for demonstration purposes)
dictionary_words = ["apple", "banana", "orange", "grape", "watermelon", "strawberry", "blueberry", "raspberry"]

def check_password_strength(password):
    # Length of the password
    length_score = len(password) / 8
    length_score = min(length_score, 1)

    # Check for character diversity
    diversity_score = 0
    if any(c.islower() for c in password):
        diversity_score += 1
    if any(c.isupper() for c in password):
        diversity_score += 1
    if any(c.isdigit() for c in password):
        diversity_score += 1
    if any(c in string.punctuation for c in password):
        diversity_score += 1

    diversity_score /= 4

    # Check against common passwords
    common_password_score = 1 if password not in common_passwords else 0

    # Check against dictionary words
    dictionary_score = 1 if not any(word in password.lower() for word in dictionary_words) else 0

    # Calculate entropy
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    entropy = len(password) * math.log2(pool) if pool > 0 else 0
    entropy_score = min(entropy / 50, 1)

    # Calculate final score
    final_score = (length_score + diversity_score + common_password_score + dictionary_score + entropy_score) / 5

    # Generate feedback
    feedback = []
    if length_score < 1:
        feedback.append("Password is too short.")
    if diversity_score < 1:
        feedback.append("Password lacks character diversity.")
    if common_password_score == 0:
        feedback.append("Password is too common.")
    if dictionary_score == 0:
        feedback.append("Password contains dictionary words.")
    if entropy_score < 1:
        feedback.append("Password entropy is too low.")

    return final_score, feedback

def evaluate_password():
    password = password_entry.get()
    score, feedback = check_password_strength(password)

    result_text = f"Password Strength: {score*100:.2f}%\n"
    result_text += "\n".join(feedback) if feedback else "Password is strong."

    messagebox.showinfo("Password Strength", result_text)

# Create the main window
root = tk.Tk()
root.title("Password Strength Tester")

# Create a label and entry for password input
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create a button to evaluate the password
evaluate_button = tk.Button(root, text="Evaluate Password", command=evaluate_password)
evaluate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
