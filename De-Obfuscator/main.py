import tkinter as tk
from tkinter import filedialog, messagebox
from src.DeObfuscator.Renamer import renamer
from src.DeObfuscator.ExpressionSimplifier import expression_simplifier
from src.DeObfuscator.DeadCodeEliminator import delete_dead_code
import shutil


def select_input_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("MiniC files", "*.mc *.c"), ("All files", "*.*")])
    if filepath:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, filepath)


def select_output_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".mc", filetypes=[
                                            ("MiniC files", "*.mc"), ("All files", "*.*")])
    if filepath:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, filepath)

def remove_all_empty_lines_from_file(input_path: str, output_path: str = None):
    if output_path is None:
        output_path = input_path

    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    non_empty_lines = [line for line in lines if line.strip() != '']

    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(non_empty_lines)


def run_DeObfuscator():
    input_path = input_entry.get()
    output_path = output_entry.get()

    if not input_path or not output_path:
        messagebox.showerror(
            "Error", "Both input and output files must be selected.")
        return

    try:
        shutil.copyfile(input_path, output_path)
        if rename_var.get():
            renamer(output_path, output_path)
        if delete_dead.get():
            expression_simplifier(output_path, output_path)
        if simple_expression.get():
            delete_dead_code(output_path, output_path)
        remove_all_empty_lines_from_file(output_path)  

  

        messagebox.showinfo("Success", "Obfuscation completed successfully.")
    except Exception as e:
        messagebox.showerror("Obfuscation Failed", str(e))


# GUI setup
root = tk.Tk()
root.title("MiniC Obfuscator")

tk.Label(root, text="Input File:").grid(row=0, column=0, sticky='e')
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2)

tk.Label(root, text="Output File:").grid(row=1, column=0, sticky='e')
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1)
tk.Button(root, text="Save As", command=select_output_file).grid(
    row=1, column=2)

# Obfuscation options
rename_var = tk.BooleanVar(value=True)
delete_dead = tk.BooleanVar(value=True)
simple_expression = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Rename Variables & Functions",
               variable=rename_var).grid(row=2, column=1, sticky='w')
tk.Checkbutton(root, text="Inject Dead Code", variable=delete_dead).grid(
    row=3, column=1, sticky='w')
tk.Checkbutton(root, text="Control Flow Flattening",
               variable=simple_expression).grid(row=4, column=1, sticky='w')

tk.Button(root, text="Run Obfuscator", command=run_DeObfuscator).grid(
    row=8, column=1, pady=10)

root.mainloop()
