import tkinter as tk
import re
import time

class PasswordComplexityChecker:
    def __init__(self, master):
        self.master = master
        master.title("Password Complexity Checker")

        # Create banner
        banner_label = tk.Label(master, text="Password Complexity Checker", font=("Arial", 24))
        banner_label.pack(pady=20)

        # Create password input field
        password_label = tk.Label(master, text="Enter a password:")
        password_label.pack()
        self.password_entry = tk.Entry(master, width=40, show="*")
        self.password_entry.pack()
        self.password_entry.bind("<KeyRelease>", self.update_feedback)

        # Create feedback label
        self.feedback_label = tk.Label(master, text="", wraplength=400)
        self.feedback_label.pack(pady=20)

        # Create auto-clear and re-run functionality
        self.auto_clear_and_re_run()

    def update_feedback(self, event):
        password = self.password_entry.get()
        strength = self.password_complexity_checker(password)

        feedback = f"Password strength: {strength}"
        if strength == 'weak':
            feedback += "\nPassword is weak. Consider using a stronger password."
        elif strength == 'medium':
            feedback += "\nPassword is medium. Consider adding more complexity."
        else:
            feedback += "\nPassword is strong!"

        self.feedback_label.config(text=feedback)

    def password_complexity_checker(self, password):
        strength = 'bad'

        # Check password length
        if len(password) < 12:
            strength = 'bad'
        elif len(password) < 16:
            strength = 'weak'
        elif len(password) < 20:
            strength = 'medium'
        else:
            strength = 'strong'

        # Check for uppercase letters
        if re.search(r"[A-Z]", password):
            if strength == 'bad':
                strength = 'weak'
            elif strength == 'weak':
                strength = 'medium'
            elif strength == 'medium':
                strength = 'strong'

        # Check for lowercase letters
        if re.search(r"[a-z]", password):
            if strength == 'bad':
                strength = 'weak'
            elif strength == 'weak':
                strength = 'medium'
            elif strength == 'medium':
                strength = 'strong'

        # Check for numbers
        if re.search(r"\d", password):
            if strength == 'bad':
                strength = 'weak'
            elif strength == 'weak':
                strength = 'medium'
            elif strength == 'medium':
                strength = 'strong'

        # Check for special characters
        if re.search(r"\W", password):
            if strength == 'medium':
                strength = 'strong'
            elif strength == 'strong':
                strength = 'very strong'

        # Check for repeating characters
        if len(set(password)) < len(password) - 2:
            strength = 'bad'

        # Check for common patterns
        common_patterns = ["qwerty", "123456", "abcdef"]
        if any(pattern in password.lower() for pattern in common_patterns):
            strength = 'bad'

        return strength

    def auto_clear_and_re_run(self):
        self.password_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.master.after(2000, self.update_feedback, None)

root = tk.Tk()
my_gui = PasswordComplexityChecker(root)
root.mainloop()
