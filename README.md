
---

# Tic Tac Toe Tkinter Project

A simple Tic Tac Toe game built using Python's Tkinter library. Includes instructions for running in **normal Python** and as an **EXE**.

---

## 1️⃣ Main Things Used in Tkinter

* **Tk()** → Creates the main application window.
* **title()** → Sets the window title.
* **geometry()** → Sets the window size.
* **iconbitmap()** → Sets the window icon (`.ico` file).
* **Button()** → Creates buttons for game actions.
* **pack() / grid()** → Layout managers for placing widgets.
* **messagebox.showinfo()** → Shows popup message box.
* **mainloop()** → Starts the Tkinter event loop.

---

## 2️⃣ Things Often Forgotten

* **Base path handling for EXE** → Use `sys._MEIPASS` to load icons inside EXE.
* **Adding icon to message boxes** → Ensure icons are bundled.
* **Try-except wrapping** → Catch runtime errors in EXE.
* **Using `--add-data` in PyInstaller** → Include external files like `icon.ico`.
* **File name spaces** → Always use quotes if files have spaces.

---

## 3️⃣ Main Commands & Syntax

### Creating the Window

```python
from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")
root.iconbitmap("icon.ico")
```

### Creating a Button

```python
from tkinter import messagebox

def click_action():
    messagebox.showinfo("Info", "You clicked!")

Button(root, text="Click Me", command=click_action).pack()
```

### Starting the App

```python
root.mainloop()
```

### Handling Icon for EXE vs Normal Python

```python
import sys
import os

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Path for EXE
else:
    base_path = os.path.abspath(".")  # Path for normal Python

icon_path = os.path.join(base_path, "icon.ico")
root.iconbitmap(icon_path)
```

### PyInstaller Command to Create EXE

```bash
pyinstaller --onefile --windowed --icon="icon.ico" --add-data "icon.ico;." --name="TicTacToe" TicTacToe.py
```

---

## Notes

* `sys._MEIPASS` → Needed because EXE extracts bundled files to a temporary folder.
* `--add-data` → Ensures files like `icon.ico` are included in the EXE.
* Quotes around file names → Required if they contain spaces.

---

