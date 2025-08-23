# Mini-C Obfuscator

A **compiler-based obfuscation tool** for the Mini-C language.
It parses Mini-C source files, builds an Abstract Syntax Tree (AST), applies multiple obfuscation passes, and outputs equivalent but **hard-to-read C code**.

---

## Features

The obfuscator transforms readable Mini-C code into **unreadable equivalents** while keeping the same functionality:

* **Variable Renaming** → All identifiers are replaced with meaningless randomized names.
* **Dead Code Insertion** → Insertion of unreachable blocks (`if(0){...}`) or unused variables.
* **Expression Transformation** → Simple expressions are rewritten into more complex equivalents (`a + b → a - (-b)`).
* **Control Flow Flattening** → Converts structured control flow into a dispatcher-based state machine using `switch` and `goto`.
* **Function Inlining** → Small functions are expanded inline, with optional meaningless splitting of logic.
* **Preserves Behavior** → Despite transformations, the output program produces the same results as the input.
* **Supports Control Constructs** → Handles Mini-C `if`, `while`, `for`, `switch`, and `return`.
* **I/O Compatibility** → Keeps `printf` and `scanf` functional.

---

## 📂 Project Structure

```
|   .gitignore
|   .python-version
|   antlr-4.13.1-complete.jar
|   cli.py
|   gui.py
|   main.py
|   output.mc
|   pyproject.toml
|   README.md
|   requirements.txt
|   uv.lock
|
+---grammar
|       ObfuMiniC.g4
|       run_antlr.bat
|       run_antlr.sh
|
+---input
|       input.mc
|       input1.mc
|       input2.mc
|
+---obfuscator
|   |   ast.py
|   |   ast_builder.py
|   |   code_generator.py
|   |   control_flattening.py
|   |   deadcode.py
|   |   expression_transform.py
|   |   inliner.py
|   |   name_obfuscator.py
|   |   __init__.py
|   |
|   +---parser
|   |   |   ObfuMiniC.interp
|   |   |   ObfuMiniC.tokens
|   |   |   ObfuMiniCLexer.interp
|   |   |   ObfuMiniCLexer.py
|   |   |   ObfuMiniCLexer.tokens
|   |   |   ObfuMiniCListener.py
|   |   |   ObfuMiniCParser.py
|   |   |   ObfuMiniCVisitor.py
|   |   |   __init__.py
|   |   |
|   |   \---__pycache__
|   |           ObfuMiniCLexer.cpython-312.pyc
|   |           ObfuMiniCParser.cpython-312.pyc
|   |           ObfuMiniCVisitor.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |
|   \---__pycache__
|           ast.cpython-312.pyc
|           ast_builder.cpython-312.pyc
|           code_generator.cpython-312.pyc
|           control_flattening.cpython-312.pyc
|           deadcode.cpython-312.pyc
|           expression_transform.cpython-312.pyc
|           inliner.cpython-312.pyc
|           name_obfuscator.cpython-312.pyc
|           obfuscator.cpython-312.pyc
|           __init__.cpython-312.pyc
|
+---output
|       output.mc
|
+---output_gui
|       output.mc
|

---

## Requirements

* **Python 3.8+**
* **ANTLR4** (for parsing Mini-C)
* **GCC / Clang** (for compiling obfuscated output and testing)

Install Python dependencies:

```bash
pip install antlr4-python3-runtime
```

Generate parser classes (only needed if grammar changes):

```bash
antlr4 -Dlanguage=Python3 grammar/ObfuMiniC.g4 -o obfuscator/gen
```

---

## ▶️ Running the Project

1. Place your Mini-C source program in the `input/` directory (e.g., `input/input.mc`).

2. Run the obfuscator:

```bash
python main.py
```

3. The obfuscated program will be saved into `output/output.mc`.

---

## Testing Obfuscation

To ensure behavior is preserved:

1. Compile and run the original input program:

```bash
gcc input/input.mc -o orig.out
./orig.out
```

2. Compile and run the obfuscated output program:

```bash
gcc output/output.mc -o obf.out
./obf.out
```

3. Compare results → both should produce the **same output**.

---

## Example Workflow

* Input: clean Mini-C program
* Output: obfuscated version with renamed variables, dead code, flattened control flow, and inlined functions
* Both versions run and print identical results

---

## 📌 Notes

* Obfuscation is deterministic unless randomization is introduced in variable renaming or dead code.
* Complex nested inlining may require additional handling.
* Generated code is syntactically valid C and compilable by standard compilers.

---