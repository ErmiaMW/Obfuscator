from src.Obfuscation.rename import rename_variables_and_functions
from src.Obfuscation.DeadCode import inject_dead_code

if __name__ == "__main__":
    rename_variables_and_functions("input.mc", "output.mc")
    inject_dead_code("output.mc", "output.mc")
