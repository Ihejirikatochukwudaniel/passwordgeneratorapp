#!/usr/bin/env python3
"""
Password Generator Application
A GUI application for generating secure passwords with customizable options.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip


class PasswordGenerator:
    """Main Password Generator Application Class"""
    
    def __init__(self, root):
        """Initialize the Password Generator application"""
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Configure style
        self.setup_styles()
        
        # Initialize variables
        self.setup_variables()
        
        # Create GUI elements
        self.create_widgets()
        
        # Generate initial password
        self.generate_password()
    
    def setup_styles(self):
        """Configure GUI styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
    
    def setup_variables(self):
        """Initialize all tkinter variables"""
        self.length_var = tk.IntVar(value=12)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.exclude_ambiguous_var = tk.BooleanVar(value=False)
        self.generated_password = tk.StringVar()
    
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Password Generator", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Password length section
        length_frame = ttk.LabelFrame(main_frame, text="Password Length", padding="10")
        length_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.length_scale = ttk.Scale(length_frame, from_=4, to=128, 
                                     variable=self.length_var, orient=tk.HORIZONTAL,
                                     command=self.update_length_display)
        self.length_scale.pack(fill=tk.X, pady=(0, 5))
        
        self.length_display = ttk.Label(length_frame, text="12 chars")
        self.length_display.pack()
        
        # Character types section
        types_frame = ttk.LabelFrame(main_frame, text="Character Types", padding="10")
        types_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Checkbutton(types_frame, text="Lowercase (a-z)", 
                       variable=self.lowercase_var).pack(anchor=tk.W)
        ttk.Checkbutton(types_frame, text="Uppercase (A-Z)", 
                       variable=self.uppercase_var).pack(anchor=tk.W)
        ttk.Checkbutton(types_frame, text="Numbers (0-9)", 
                       variable=self.numbers_var).pack(anchor=tk.W)
        ttk.Checkbutton(types_frame, text="Symbols (!@#$%^&*)", 
                       variable=self.symbols_var).pack(anchor=tk.W)
        
        # Options section
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Checkbutton(options_frame, text="Exclude ambiguous characters (0, O, l, 1, I)", 
                       variable=self.exclude_ambiguous_var).pack(anchor=tk.W)
        
        # Generate button
        self.generate_btn = ttk.Button(main_frame, text="Generate Password", 
                                      command=self.generate_password)
        self.generate_btn.pack(pady=(0, 10))
        
        # Password display section
        password_frame = ttk.LabelFrame(main_frame, text="Generated Password", padding="10")
        password_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.password_text = tk.Text(password_frame, height=3, wrap=tk.WORD, 
                                    font=("Courier", 12))
        self.password_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Copy button
        self.copy_btn = ttk.Button(password_frame, text="Copy to Clipboard", 
                                  command=self.copy_password)
        self.copy_btn.pack()
        
        # Strength indicator
        strength_frame = ttk.LabelFrame(main_frame, text="Password Strength", padding="10")
        strength_frame.pack(fill=tk.X)
        
        self.strength_label = ttk.Label(strength_frame, text="")
        self.strength_label.pack()
        
        self.strength_bar = ttk.Progressbar(strength_frame, mode='determinate')
        self.strength_bar.pack(fill=tk.X, pady=(5, 0))
    
    def update_length_display(self, value):
        """Update the length display label"""
        length = int(float(value))
        self.length_display.config(text=f"{length} chars")
    
    def generate_password(self):
        """Generate a password based on current settings"""
        # Get settings
        length = self.length_var.get()
        use_lowercase = self.lowercase_var.get()
        use_uppercase = self.uppercase_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()
        exclude_ambiguous = self.exclude_ambiguous_var.get()
        
        # Build character set
        chars = ""
        
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_numbers:
            chars += string.digits
        if use_symbols:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Handle case where no character types are selected
        if not chars:
            messagebox.showwarning("No Character Types", 
                                 "Please select at least one character type.")
            return
        
        # Remove ambiguous characters if requested
        if exclude_ambiguous:
            ambiguous_chars = "0Ol1I"
            chars = ''.join(c for c in chars if c not in ambiguous_chars)
        
        # Generate password ensuring at least one character from each selected type
        password = []
        
        # Add at least one character from each selected type
        if use_lowercase and not exclude_ambiguous:
            password.append(random.choice(string.ascii_lowercase))
        elif use_lowercase and exclude_ambiguous:
            lowercase_safe = ''.join(c for c in string.ascii_lowercase if c not in "l")
            if lowercase_safe:
                password.append(random.choice(lowercase_safe))
        
        if use_uppercase and not exclude_ambiguous:
            password.append(random.choice(string.ascii_uppercase))
        elif use_uppercase and exclude_ambiguous:
            uppercase_safe = ''.join(c for c in string.ascii_uppercase if c not in "OI")
            if uppercase_safe:
                password.append(random.choice(uppercase_safe))
        
        if use_numbers and not exclude_ambiguous:
            password.append(random.choice(string.digits))
        elif use_numbers and exclude_ambiguous:
            numbers_safe = ''.join(c for c in string.digits if c not in "01")
            if numbers_safe:
                password.append(random.choice(numbers_safe))
        
        if use_symbols:
            symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            password.append(random.choice(symbols))
        
        # Fill remaining length with random characters
        remaining_length = length - len(password)
        for _ in range(remaining_length):
            password.append(random.choice(chars))
        
        # Shuffle the password to avoid predictable patterns
        random.shuffle(password)
        
        # Convert to string
        password_str = ''.join(password)
        
        # Display the password
        self.display_password(password_str)
        
        # Calculate and display strength
        self.calculate_strength(password_str)
    
    def display_password(self, password):
        """Display the generated password"""
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(1.0, password)
        self.generated_password.set(password)
        self.copy_btn.config(state='normal')
    
    def copy_password(self):
        """Copy the generated password to clipboard"""
        password = self.generated_password.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Copied", "Password copied to clipboard!")
            except Exception:
                # Fallback: copy to tkinter clipboard
                self.root.clipboard_clear()
                self.root.clipboard_append(password)
                messagebox.showinfo("Copied", "Password copied to clipboard!")
    
    def calculate_strength(self, password):
        """Calculate and display password strength"""
        if not password:
            return
        
        score = 0
        feedback = []
        
        # Length scoring
        length = len(password)
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if length >= 16:
            score += 1
        
        # Character type scoring
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        char_types = sum([has_lower, has_upper, has_digit, has_symbol])
        score += char_types
        
        # Determine strength level
        if score <= 2:
            strength = "Weak"
            color = "red"
            progress = 25
        elif score <= 4:
            strength = "Fair"
            color = "orange"
            progress = 50
        elif score <= 6:
            strength = "Good"
            color = "yellow"
            progress = 75
        else:
            strength = "Excellent"
            color = "green"
            progress = 100
        
        # Update strength display
        self.strength_label.config(text=f"Strength: {strength}")
        self.strength_bar.config(value=progress)
        
        # Configure progress bar color (if supported)
        try:
            self.style.configure("strength.Horizontal.TProgressbar", 
                               background=color)
            self.strength_bar.config(style="strength.Horizontal.TProgressbar")
        except:
            pass


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()