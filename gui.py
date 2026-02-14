import tkinter as tk
from tkinter import ttk

# Core window setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x300")
root.resizable(False, False)

# Title lable
title = ttk.Label(root, text="Rock, Paper, Scissors!", font=("Arial", 18, "bold"))
title.pack(pady=(12, 6))

# Lines that separate the title and the rest of the GUI
line_canvas = tk.Canvas(root, height=30, highlightthickness=0)
line_canvas.pack(fill="x", padx=10)
line_canvas.create_line(10, 10, 410, 10)
line_canvas.create_line(10, 20, 410, 20)

# Section of the window that houses choices
btn_frame = ttk.LabelFrame(root, text="Choose", padding=10)
btn_frame.pack(padx=12, pady=10, fill="x")

ttk.Button(btn_frame, text="Rock", width=12).grid(row=0, column=0, padx=6, pady=6)
ttk.Button(btn_frame, text="Paper", width=12).grid(row=0, column=1, padx=6, pady=6)
ttk.Button(btn_frame, text="Scissors", width=12).grid(row=0, column=2, padx=6, pady=6)

# A checkbox under the choices window for a hypothetical sound option.
sound_var = tk.BooleanVar(value=False)
ttk.Checkbutton(root, text="Enable sound", variable=sound_var).pack(anchor="w", padx=18)

# Section of the window that houses radio buttons for a hypothetical theme change.
theme_var = tk.StringVar(value="Light")
theme_box = ttk.LabelFrame(root, text="Theme", padding=10)
theme_box.pack(padx=12, pady=10, fill="x")

ttk.Radiobutton(theme_box, text="Light", variable=theme_var, value="Light").grid(row=0, column=0, padx=6, sticky="w")
ttk.Radiobutton(theme_box, text="Dark", variable=theme_var, value="Dark").grid(row=0, column=1, padx=6, sticky="w")
ttk.Radiobutton(theme_box, text="Blue", variable=theme_var, value="Blue").grid(row=0, column=2, padx=6, sticky="w")

root.mainloop()