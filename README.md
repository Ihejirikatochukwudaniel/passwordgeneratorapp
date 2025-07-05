# 🔐 Secure Password Generator

A beautiful, modern Python application for generating secure passwords with customizable criteria. Built with tkinter for a native desktop experience.

![C:\Users\Admin\Documents\password generator project\password generator screenshot-1.PNG](<password generator screenshot-1.PNG>)

## ✨ Features

- **🎨 Beautiful Modern UI**: Clean, intuitive interface with smooth animations
- **🔒 Cryptographically Secure**: Uses Python's `secrets` module for secure randomization
- **⚙️ Customizable Criteria**: 
  - Variable password length (4-128 characters)
  - Character types: lowercase, uppercase, numbers, symbols
  - Option to exclude ambiguous characters (0, O, l, I, 1)
- **📊 Password Strength Meter**: Real-time visual feedback on password security
- **📋 One-Click Copy**: Instantly copy passwords to clipboard
- **🎯 Smart Generation**: Ensures at least one character from each selected type
- **🎪 Fun Animations**: Engaging visual feedback during generation

## 🚀 Installation

### Method 1: Direct Run (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/password-generator.git
cd password-generator

# Install dependencies
pip install -r requirements.txt

# Run the application
python password_generator.py
```

### Method 2: Package Installation
```bash
# Install as a package
pip install -e .

# Run from anywhere
password-generator
```

## 📦 Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pyperclip (for clipboard functionality)

## 🎯 Usage

1. **Launch the application**:
   ```bash
   python password_generator.py
   ```

2. **Customize your password**:
   - Adjust the length using the slider (4-128 characters)
   - Select character types using checkboxes
   - Optionally exclude ambiguous characters

3. **Generate password**:
   - Click "🎲 Generate Secure Password"
   - View the real-time strength meter
   - Copy to clipboard with one click

4. **Security Tips**:
   - Use at least 12 characters for good security
   - Include all character types for maximum strength
   - Avoid common patterns and dictionary words

## 🏗️ Project Structure

```
password-generator/
├── password_generator.py    # Main application file
├── requirements.txt         # Python dependencies
├── setup.py                # Package configuration
├── README.md               # This file
├── LICENSE                 # License file
├── assets/                 # Optional assets folder
│   ├── favicon.ico         # Application icon
│   └── screenshot.png      # Application screenshot
└── tests/                  # Unit tests (optional)
    └── test_password_generator.py
```

## 🔧 Advanced Features

### Password Strength Calculation
The application calculates password strength based on:
- Length (8+ characters recommended)
- Character variety (lowercase, uppercase, numbers, symbols)
- Absence of common patterns

### Security Best Practices
- Uses `secrets.choice()` for cryptographically secure randomization
- Ensures character type requirements are met
- Shuffles password components to avoid predictable patterns
- Provides real-time feedback on password quality

## 🎨 Customization

### Modifying Colors
Edit the `colors` dictionary in the `PasswordGenerator` class:
```python
self.colors = {
    'bg': '#667eea',           # Background gradient
    'fg': '#ffffff',           # Text color
    'accent': '#4CAF50',       # Accent color
    'secondary': '#2196F3',    # Secondary color
    'warning': '#ff4444',      # Warning color
    'success': '#4CAF50',      # Success color
    'card_bg': '#f8f9ff',      # Card background
    'card_border': '#e0e6ff'   # Card border
}
```

### Adding New Character Sets
Extend the character options in the `create_character_section` method:
```python
options = [
    ("Custom Characters", self.custom_var, "your_custom_chars"),
    # ... existing options
]
```

## 🧪 Testing

Run the test suite (if implemented):
```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's tkinter for cross-platform compatibility
- Uses the `secrets` module for cryptographically secure random generation
- Clipboard functionality powered by `pyperclip`

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/password-generator/issues) page
2. Create a new issue if your problem isn't already addressed
3. Provide detailed information about your system and the error

---

**Made with ❤️ and Python**