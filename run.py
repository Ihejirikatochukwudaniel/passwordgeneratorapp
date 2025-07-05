#!/usr/bin/env python3
"""
Simple launcher script for the Password Generator
Run this file to start the application
"""

import sys
import os

# Add the current directory to the path so we can import the main module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from password_generator import main
    
    if __name__ == "__main__":
        print("🔐 Starting Secure Password Generator...")
        print("Close the window or press Ctrl+C to exit")
        main()
        
except ImportError as e:
    print(f"❌ Error importing required modules: {e}")
    print("Please install required dependencies:")
    print("pip install pyperclip")
    sys.exit(1)
    
except KeyboardInterrupt:
    print("\n👋 Goodbye!")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ An error occurred: {e}")
    sys.exit(1)