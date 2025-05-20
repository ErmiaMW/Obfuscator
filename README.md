# Developed by :
- Ermia Mirzaei
- Ali Norouzi
- Amirali Mohammadpour
# Obfuscator for Mini-C Language

A powerful Python-based obfuscator for the Mini-C programming language, designed to transform readable source code into a harder-to-understand version — while preserving its original functionality. This tool is perfect for protecting intellectual property or educational exploration of obfuscation techniques.

---

## About Mini-C

**Mini-C** is a simplified subset of the C language that includes:

- Data Types: `int`, `char`, `bool`  
- Variables & Operators  
- Control Flow: `if`, `else`, `while`, `for`, `return`  
- I/O Functions: `printf`, `scanf`  
- User-defined Functions  

---

## What This Project Does

This project:
1. Parses `Mini-C` code using **ANTLR** and a custom grammar
2. Builds an **Abstract Syntax Tree (AST)**
3. Applies **multiple obfuscation techniques** on the AST
4. Generates obfuscated code and outputs it in `output.mc`
5. Provides a **user-friendly GUI** to select obfuscation methods interactively

---

## Implemented Obfuscation Techniques

- **Renaming** (variables & functions)
- **Dead Code Insertion**
- **Equivalent Expression Replacement**
- **Control Flow Flattening**
- **Function Inlining**
- **Dummy Function Insertion**

---

## GUI Support

The project includes a **Tkinter-based graphical interface** to allow users to:
- Select the input file (`input.mc`)
- Choose which techniques to apply
- Generate the obfuscated file (`output.mc`) with a click

---

## Getting Started

###  Requirements
- Python 3.6+
- `antlr4-python3-runtime==4.13.1`

Install the ANTLR runtime via pip:
```bash
pip install antlr4-python3-runtime