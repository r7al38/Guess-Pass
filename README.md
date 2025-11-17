# 🔐 GuessPass - Password Insight Generator

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

**GuessPass** is an advanced password analysis tool that generates potential passwords based on personal information patterns. It demonstrates how attackers might guess passwords using publicly available data.

**Developer:** r7al38

## 🎯 What It Does

GuessPass analyzes personal information to generate likely passwords that users might create based on their:

- **Personal Details**: Full name, nickname, birth date
- **Location**: City, country, address patterns  
- **Interests**: Hobbies, favorite sports, activities
- **Preferences**: Pet names, favorite numbers, important dates
- **Behavior**: Common password patterns and substitutions

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Terminal/Command Prompt

### Installation & Usage

```bash
# Clone the repository
git clone https://github.com/r7al38/GuessPass.git
cd GuessPass

# Run the tool
python3 guesspass.py

# Or make it executable and run
chmod +x guesspass.py
./guesspass.py
```
## 🔒 Command Line Options

```bash
# Interactive mode (recommended)
python3 guesspass.py

# Generate strong password only
python3 guesspass.py --generate

# Analyze specific password
python3 guesspass.py --analyze "MyPassword123"

# Quick analysis with basic info
python3 guesspass.py --quick --name "John Doe" --birth-year 1990

# Save results to file
python3 guesspass.py --output results.txt
```

## 📊 Example Output

```bash
[!] Generated 24 weak password possibilities:
[01] john1990       [02] john123        [03] johndoe
[04] j0hn1990       [05] john!          [06] johndoe123
...
[!] Security Score: 2/4 - Medium Risk
[!] Recommendations:
    • Avoid using personal names in passwords
    • Use longer passwords (12+ characters)
    • Mix uppercase, lowercase, numbers, and symbols
```

## 🙏 Acknowledgments
Inspired by real-world password analysis techniques Thanks to
the security community for pattern research Common password lists from security researchers.

## 👨‍💻 Developer - r7al38

**Remember**: Strong passwords are your first line of defense. Use this tool to understand vulnerabilities and improve your security posture!
