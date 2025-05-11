import tkinter as tk
from tkinter import filedialog, messagebox
from src.Obfuscation.rename import rename_variables_and_functions
from src.Obfuscation.DeadCode import inject_dead_code
from src.Obfuscation.ControlFlowFlattening import control_flow_flattening
from src.Obfuscation.DummyFunction import dummy_function
from src.Obfuscation.FunctionInlining import function_inlining
from src.Obfuscation.EquivalentExpression import equaivalent_expression

def select_input_file():
    filepath = filedialog.askopenfilename(filetypes=[("MiniC files", "*.mc *.c"), ("All files", "*.*")])
    if filepath:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, filepath)

def select_output_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".mc", filetypes=[("MiniC files", "*.mc"), ("All files", "*.*")])
    if filepath:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, filepath)

def run_obfuscator():
    input_path = input_entry.get()
    output_path = output_entry.get()
    
    if not input_path or not output_path:
        messagebox.showerror("Error", "Both input and output files must be selected.")
        return

    try:
        if rename_var.get():
            rename_variables_and_functions(input_path, output_path)
        if inject_dead.get():
            inject_dead_code(output_path, output_path)
        if flatten_var.get():
            control_flow_flattening(output_path, output_path)
        if dummy_var.get():
            dummy_function(output_path, output_path)
        if inline_var.get():
            function_inlining(output_path, output_path)
        if equiv_var.get():
            equaivalent_expression(output_path, output_path)

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
tk.Button(root, text="Save As", command=select_output_file).grid(row=1, column=2)

# Obfuscation options
rename_var = tk.BooleanVar(value=True)
inject_dead = tk.BooleanVar(value=True)
flatten_var = tk.BooleanVar(value=False)
dummy_var = tk.BooleanVar(value=False)
inline_var = tk.BooleanVar(value=False)
equiv_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Rename Variables & Functions", variable=rename_var).grid(row=2, column=1, sticky='w')
tk.Checkbutton(root, text="Inject Dead Code", variable=inject_dead).grid(row=3, column=1, sticky='w')
tk.Checkbutton(root, text="Control Flow Flattening", variable=flatten_var).grid(row=4, column=1, sticky='w')
tk.Checkbutton(root, text="Insert Dummy Functions", variable=dummy_var).grid(row=5, column=1, sticky='w')
tk.Checkbutton(root, text="Inline Functions", variable=inline_var).grid(row=6, column=1, sticky='w')
tk.Checkbutton(root, text="Equivalent Expression Replacement", variable=equiv_var).grid(row=7, column=1, sticky='w')

tk.Button(root, text="Run Obfuscator", command=run_obfuscator).grid(row=8, column=1, pady=10)

root.mainloop()
