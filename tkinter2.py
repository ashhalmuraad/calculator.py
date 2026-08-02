import math
import tkinter as tk
from tkinter import messagebox


# ==================================================
# MATHEMATICAL FUNCTIONS
# These functions only perform calculations.
# They do not interact with the GUI.
# ==================================================

def area_circle(radius):
    return math.pi * radius ** 2


def area_square(side):
    return side ** 2


def area_rectangle(length, width):
    return length * width


def area_triangle(base, height):
    return (base * height) / 2


def volume_sphere(radius):
    return (4 / 3) * math.pi * radius ** 3


def volume_cube(side):
    return side ** 3


def volume_cuboid(length, width, height):
    return length * width * height


def volume_cone(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height


# ==================================================
# ROYAL THEME
# ==================================================

ROYAL_NAVY = "#0B1026"
DEEP_NAVY = "#111A3D"
ROYAL_BLUE = "#243B7A"
ROYAL_PURPLE = "#4A2C72"
GOLD = "#D8B35A"
LIGHT_GOLD = "#F4D77D"
CREAM = "#FFF7E6"
WHITE = "#FFFFFF"
MUTED = "#B9C2DA"
CARD = "#17234D"
CARD_2 = "#1D2C5C"
ENTRY_BG = "#F8F3E7"
DANGER = "#A83F4B"


# ==================================================
# MAIN WINDOW
# ==================================================

root = tk.Tk()
root.title("CHSLO Calculator | Royal Edition")
root.configure(bg=ROYAL_NAVY)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = min(int(screen_width * 0.90), 1100)
window_height = min(int(screen_height * 0.86), 760)

root.geometry(f"{window_width}x{window_height}")
root.minsize(760, 580)
root.resizable(True, True)

scale = min(screen_width, screen_height) / 900
title_size = max(18, int(25 * scale))
subtitle_size = max(9, int(11 * scale))
normal_size = max(10, int(12 * scale))
button_size = max(9, int(11 * scale))


# ==================================================
# REUSABLE GUI HELPERS
# ==================================================

def make_button(parent, text, command, bg=ROYAL_BLUE,
                fg=WHITE, font_size=None, width=None):
    """Creates a themed button with a simple hover effect."""

    if font_size is None:
        font_size = button_size

    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Segoe UI", font_size, "bold"),
        bg=bg,
        fg=fg,
        activebackground=GOLD,
        activeforeground=ROYAL_NAVY,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=14,
        pady=9,
        width=width
    )

    original_bg = bg

    def enter(event):
        button.config(bg=LIGHT_GOLD, fg=ROYAL_NAVY)

    def leave(event):
        button.config(bg=original_bg, fg=fg)

    button.bind("<Enter>", enter)
    button.bind("<Leave>", leave)

    return button


def make_label(parent, text, size=None, bold=False,
               fg=WHITE, bg=CARD, **kwargs):

    if size is None:
        size = normal_size

    weight = "bold" if bold else "normal"

    return tk.Label(
        parent,
        text=text,
        font=("Segoe UI", size, weight),
        fg=fg,
        bg=bg,
        **kwargs
    )


def make_entry(parent, width=24):
    entry = tk.Entry(
        parent,
        font=("Segoe UI", normal_size),
        width=width,
        justify="center",
        bg=ENTRY_BG,
        fg=ROYAL_NAVY,
        insertbackground=ROYAL_NAVY,
        relief="flat",
        bd=0,
        highlightthickness=2,
        highlightbackground=GOLD,
        highlightcolor=LIGHT_GOLD
    )
    return entry


def make_card(parent):
    card = tk.Frame(
        parent,
        bg=CARD,
        highlightthickness=1,
        highlightbackground="#53638F"
    )
    return card


def clear_work_area():
    for widget in work_frame.winfo_children():
        widget.destroy()


def show_result(result):
    result_value.config(text=str(result))
    result_status.config(text="Calculation completed")


def clear_result():
    result_value.config(text="Ready")
    result_status.config(text="Choose a tool to begin")


def page_title(title, subtitle):
    make_label(
        work_frame,
        title,
        size=max(16, title_size - 5),
        bold=True,
        fg=LIGHT_GOLD,
        bg=ROYAL_NAVY
    ).pack(pady=(10, 2))

    make_label(
        work_frame,
        subtitle,
        size=subtitle_size,
        fg=MUTED,
        bg=ROYAL_NAVY
    ).pack(pady=(0, 12))


def set_active(button):
    for item in nav_buttons:
        item.config(bg=ROYAL_BLUE, fg=WHITE)
    button.config(bg=GOLD, fg=ROYAL_NAVY)


# ==================================================
# HEADER
# ==================================================

header = tk.Frame(root, bg=DEEP_NAVY, height=100)
header.pack(fill=tk.X)
header.pack_propagate(False)

brand = tk.Frame(header, bg=DEEP_NAVY)
brand.pack(side=tk.LEFT, padx=28, pady=14)

make_label(
    brand,
    "♛  CHSLO CALCULATOR",
    size=title_size,
    bold=True,
    fg=LIGHT_GOLD,
    bg=DEEP_NAVY
).pack(anchor="w")

make_label(
    brand,
    "ROYAL EDITION  •  Mathematics made elegant",
    size=subtitle_size,
    fg=MUTED,
    bg=DEEP_NAVY
).pack(anchor="w", pady=(2, 0))

# Decorative gold line
tk.Frame(header, bg=GOLD, height=3).pack(
    side=tk.BOTTOM,
    fill=tk.X
)


# ==================================================
# NAVIGATION
# ==================================================

nav_frame = tk.Frame(root, bg=ROYAL_NAVY)
nav_frame.pack(fill=tk.X, padx=22, pady=(14, 8))

nav_inner = tk.Frame(
    nav_frame,
    bg=CARD,
    highlightthickness=1,
    highlightbackground="#455681"
)
nav_inner.pack(fill=tk.X)

nav_buttons = []


# ==================================================
# MAIN CONTENT
# ==================================================

content = tk.Frame(root, bg=ROYAL_NAVY)
content.pack(fill=tk.BOTH, expand=True, padx=22, pady=8)

# Result panel
result_card = tk.Frame(
    content,
    bg=DEEP_NAVY,
    highlightthickness=2,
    highlightbackground=GOLD
)
result_card.pack(side=tk.RIGHT, fill=tk.Y, padx=(12, 0))
result_card.configure(width=245)
result_card.pack_propagate(False)

make_label(
    result_card,
    "ROYAL DISPLAY",
    size=subtitle_size,
    bold=True,
    fg=GOLD,
    bg=DEEP_NAVY
).pack(pady=(28, 8))

result_value = tk.Label(
    result_card,
    text="Ready",
    font=("Segoe UI", max(18, title_size - 3), "bold"),
    fg=WHITE,
    bg=DEEP_NAVY,
    wraplength=210,
    justify="center"
)
result_value.pack(fill=tk.X, padx=14, pady=12)

tk.Frame(
    result_card,
    bg="#405080",
    height=1
).pack(fill=tk.X, padx=24, pady=12)

result_status = tk.Label(
    result_card,
    text="Choose a tool to begin",
    font=("Segoe UI", subtitle_size),
    fg=MUTED,
    bg=DEEP_NAVY,
    wraplength=190,
    justify="center"
)
result_status.pack(padx=18, pady=6)

clear_button = make_button(
    result_card,
    "↺  Clear Display",
    clear_result,
    bg=DANGER,
    font_size=normal_size
)
clear_button.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=24)

# Work area
work_outer = tk.Frame(
    content,
    bg=ROYAL_NAVY
)
work_outer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

work_frame = tk.Frame(
    work_outer,
    bg=ROYAL_NAVY
)
work_frame.pack(fill=tk.BOTH, expand=True)


# ==================================================
# DMAS CALCULATOR
# ==================================================

def open_dmas():
    clear_work_area()
    page_title(
        "DMAS Calculator",
        "Enter two values and choose an operation."
    )

    card = make_card(work_frame)
    card.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 18))

    form = tk.Frame(card, bg=CARD)
    form.pack(expand=True, pady=22)

    make_label(form, "FIRST NUMBER", bold=True, fg=GOLD).pack(anchor="w")
    number_1_entry = make_entry(form)
    number_1_entry.pack(pady=(4, 14))

    make_label(
        form,
        "OPERATION   +   −   ×   ÷",
        bold=True,
        fg=GOLD
    ).pack(anchor="w")

    operator_entry = make_entry(form, width=12)
    operator_entry.pack(pady=(4, 14))

    make_label(form, "SECOND NUMBER", bold=True, fg=GOLD).pack(anchor="w")
    number_2_entry = make_entry(form)
    number_2_entry.pack(pady=(4, 18))

    def calculate():
        try:
            number_1 = float(number_1_entry.get())
            number_2 = float(number_2_entry.get())
            operator = operator_entry.get().strip()

            if operator == "+":
                answer = number_1 + number_2
            elif operator == "-":
                answer = number_1 - number_2
            elif operator in ("*", "×", "x", "X"):
                answer = number_1 * number_2
            elif operator in ("/", "÷"):
                if number_2 == 0:
                    messagebox.showerror(
                        "Math Error",
                        "Division by zero is undefined."
                    )
                    return
                answer = number_1 / number_2
            else:
                messagebox.showerror(
                    "Invalid Operator",
                    "Use +, -, *, or /."
                )
                return

            show_result(answer)

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid numbers."
            )

    make_button(
        form,
        "♛  CALCULATE",
        calculate,
        bg=ROYAL_PURPLE,
        font_size=max(12, button_size + 1),
        width=20
    ).pack(pady=4)

    number_1_entry.focus_set()


# ==================================================
# ELECTRICITY BILL CALCULATOR
# ==================================================

def open_bills():
    clear_work_area()
    page_title(
        "Electricity Bill Calculator",
        "Estimate your bill using the progressive slab system."
    )

    card = make_card(work_frame)
    card.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 18))

    form = tk.Frame(card, bg=CARD)
    form.pack(expand=True)

    make_label(
        form,
        "ENTER UNITS USED",
        bold=True,
        fg=GOLD
    ).pack(pady=(25, 5))

    units_entry = make_entry(form)
    units_entry.pack(pady=(0, 8))

    make_label(
        form,
        "Fixed charge: Rs. 1,200",
        size=subtitle_size,
        fg=MUTED
    ).pack(pady=(0, 18))

    def calculate_bill():
        try:
            units = float(units_entry.get())

            if units < 0:
                messagebox.showerror(
                    "Input Error",
                    "Units cannot be negative."
                )
                return

            bill = 1200

            if units <= 100:
                bill += units * 12.5
            elif units <= 200:
                bill += 100 * 12.5 + (units - 100) * 26.5
            elif units <= 300:
                bill += (
                    100 * 12.5
                    + 100 * 26.5
                    + (units - 200) * 38
                )
            else:
                bill += (
                    100 * 12.5
                    + 100 * 26.5
                    + 100 * 38
                    + (units - 300) * 65
                )

            show_result(f"Rs. {bill:,.2f}")

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter a valid number."
            )

    make_button(
        form,
        "⚡  CALCULATE BILL",
        calculate_bill,
        bg=ROYAL_PURPLE,
        width=21
    ).pack(pady=8)

    units_entry.focus_set()


# ==================================================
# ROOTS AND POWERS
# ==================================================

def open_roots():
    clear_work_area()
    page_title(
        "Roots & Powers",
        "Explore squares, cubes, and their roots."
    )

    card = make_card(work_frame)
    card.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 18))

    form = tk.Frame(card, bg=CARD)
    form.pack(expand=True, fill=tk.X, padx=45)

    make_label(
        form,
        "ENTER A NUMBER",
        bold=True,
        fg=GOLD
    ).pack(pady=(22, 5))

    number_entry = make_entry(form)
    number_entry.pack(pady=(0, 16))

    def calculate(operation):
        try:
            number = float(number_entry.get())

            if operation == "square_root":
                if number < 0:
                    messagebox.showerror(
                        "Math Error",
                        "A negative number has no real square root."
                    )
                    return
                answer = math.sqrt(number)

            elif operation == "square":
                answer = number ** 2

            elif operation == "cube_root":
                answer = math.copysign(
                    abs(number) ** (1 / 3),
                    number
                )

            elif operation == "cube":
                answer = number ** 3

            show_result(f"{answer:.4f}")

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter a valid number."
            )

    button_frame = tk.Frame(form, bg=CARD)
    button_frame.pack(fill=tk.X, pady=(4, 22))

    buttons = [
        ("√  Square Root", "square_root"),
        ("x²  Square", "square"),
        ("∛  Cube Root", "cube_root"),
        ("x³  Cube", "cube")
    ]

    for index, (text, operation) in enumerate(buttons):
        button = make_button(
            button_frame,
            text,
            lambda op=operation: calculate(op),
            bg=ROYAL_BLUE,
            font_size=normal_size
        )
        button.grid(
            row=index // 2,
            column=index % 2,
            padx=5,
            pady=5,
            sticky="ew"
        )

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    number_entry.focus_set()


# ==================================================
# GEOMETRY CALCULATOR
# ==================================================

def open_geometry():
    clear_work_area()
    page_title(
        "Geometry Calculator",
        "Calculate areas and volumes with guided inputs."
    )

    card = make_card(work_frame)
    card.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 18))

    controls = tk.Frame(card, bg=CARD)
    controls.pack(fill=tk.X, padx=25, pady=(18, 4))

    mode_var = tk.StringVar(value="Area")
    shape_var = tk.StringVar(value="Circle")

    make_label(
        controls,
        "MODE",
        bold=True,
        fg=GOLD
    ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

    for col, (text, value) in enumerate(
        [("Area", "Area"), ("Volume", "Volume")],
        start=1
    ):
        tk.Radiobutton(
            controls,
            text=text,
            variable=mode_var,
            value=value,
            font=("Segoe UI", normal_size),
            bg=CARD,
            fg=WHITE,
            activebackground=CARD,
            activeforeground=LIGHT_GOLD,
            selectcolor=ROYAL_PURPLE,
            highlightthickness=0
        ).grid(row=0, column=col, padx=7, pady=6)

    make_label(
        controls,
        "SHAPE",
        bold=True,
        fg=GOLD
    ).grid(row=1, column=0, padx=8, pady=8, sticky="w")

    shape_menu = tk.OptionMenu(
        controls,
        shape_var,
        "Circle",
        "Square",
        "Rectangle",
        "Triangle",
        "Sphere",
        "Cube",
        "Cuboid",
        "Cone"
    )

    shape_menu.config(
        font=("Segoe UI", normal_size, "bold"),
        bg=ROYAL_BLUE,
        fg=WHITE,
        activebackground=GOLD,
        activeforeground=ROYAL_NAVY,
        relief="flat",
        width=15,
        highlightthickness=0
    )
    shape_menu["menu"].config(
        font=("Segoe UI", normal_size),
        bg=ENTRY_BG,
        fg=ROYAL_NAVY
    )
    shape_menu.grid(
        row=1,
        column=1,
        columnspan=2,
        padx=7,
        pady=8,
        sticky="w"
    )

    input_frame = tk.Frame(card, bg=CARD_2)
    input_frame.pack(
        fill=tk.BOTH,
        expand=True,
        padx=25,
        pady=10
    )

    input_entries = []

    def set_inputs():
        for widget in input_frame.winfo_children():
            widget.destroy()

        input_entries.clear()
        shape = shape_var.get()

        if shape in ("Circle", "Sphere", "Cube"):
            labels = ["Radius / Side:"]
        elif shape == "Square":
            labels = ["Side:"]
        elif shape == "Rectangle":
            labels = ["Length:", "Width:"]
        elif shape == "Triangle":
            labels = ["Base:", "Height:"]
        elif shape == "Cuboid":
            labels = ["Length:", "Width:", "Height:"]
        elif shape == "Cone":
            labels = ["Radius:", "Height:"]
        else:
            labels = []

        for label_text in labels:
            make_label(
                input_frame,
                label_text,
                bold=True,
                fg=LIGHT_GOLD,
                bg=CARD_2
            ).pack(pady=(8, 2))

            entry = make_entry(input_frame, width=20)
            entry.pack(pady=(0, 4))
            input_entries.append(entry)

        if input_entries:
            input_entries[0].focus_set()

    def calculate_geometry():
        try:
            shape = shape_var.get()
            values = []

            for entry in input_entries:
                value = float(entry.get())

                if value < 0:
                    raise ValueError

                values.append(value)

            if shape == "Circle":
                answer = area_circle(values[0])
                unit = "square units"

            elif shape == "Square":
                answer = area_square(values[0])
                unit = "square units"

            elif shape == "Rectangle":
                answer = area_rectangle(values[0], values[1])
                unit = "square units"

            elif shape == "Triangle":
                answer = area_triangle(values[0], values[1])
                unit = "square units"

            elif shape == "Sphere":
                answer = volume_sphere(values[0])
                unit = "cubic units"

            elif shape == "Cube":
                answer = volume_cube(values[0])
                unit = "cubic units"

            elif shape == "Cuboid":
                answer = volume_cuboid(
                    values[0],
                    values[1],
                    values[2]
                )
                unit = "cubic units"

            elif shape == "Cone":
                answer = volume_cone(values[0], values[1])
                unit = "cubic units"

            show_result(f"{answer:.4f} {unit}")

        except (ValueError, IndexError):
            messagebox.showerror(
                "Input Error",
                "Enter valid positive measurements and press Set Inputs."
            )

    action_frame = tk.Frame(card, bg=CARD)
    action_frame.pack(fill=tk.X, padx=25, pady=(0, 18))

    make_button(
        action_frame,
        "Set Inputs",
        set_inputs,
        bg=ROYAL_BLUE,
        font_size=normal_size
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

    make_button(
        action_frame,
        "♛  Calculate",
        calculate_geometry,
        bg=ROYAL_PURPLE,
        font_size=normal_size
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))

    set_inputs()


# ==================================================
# MAIN MENU BUTTONS
# ==================================================

def add_nav_button(text, command):
    button = make_button(
        nav_inner,
        text,
        command,
        bg=ROYAL_BLUE,
        font_size=normal_size
    )
    button.pack(
        side=tk.LEFT,
        expand=True,
        fill=tk.X,
        padx=3,
        pady=3
    )
    nav_buttons.append(button)
    return button


dmas_button = add_nav_button("DMAS", open_dmas)
bills_button = add_nav_button("Bills", open_bills)
roots_button = add_nav_button("Roots & Powers", open_roots)
geometry_button = add_nav_button("Geometry", open_geometry)


# ==================================================
# START APPLICATION
# ==================================================

open_dmas()
set_active(dmas_button)

root.mainloop()
