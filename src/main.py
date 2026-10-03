import tkinter as tk
import random

from color_converter import rgb_to_hsv, hsv_to_rgb


# -----------------------------
# Main window
# -----------------------------

root = tk.Tk()
root.title("RGB-HSV Color Studio")
root.geometry("1000x840")
root.resizable(False, False)


# Prevent RGB and HSV callbacks from triggering each other endlessly
updating = False


# -----------------------------
# Helper functions
# -----------------------------

def set_preview_color(r, g, b):
    color = f"#{r:02x}{g:02x}{b:02x}"

    preview.config(bg=color)

    hex_label.config(
        text=f"HEX: {color.upper()}"
    )


def update_from_rgb(value=None):
    global updating

    if updating:
        return

    updating = True

    # Read RGB values
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()

    # RGB -> HSV
    h, s, v = rgb_to_hsv(r, g, b)

    # Synchronize HSV sliders
    hue_slider.set(round(h))
    saturation_slider.set(round(s))
    value_slider.set(round(v))

    # Update labels
    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h:.1f}°, {s:.1f}%, {v:.1f}%)"
    )

    # Update preview and HEX
    set_preview_color(r, g, b)

    updating = False


def update_from_hsv(value=None):
    global updating

    if updating:
        return

    updating = True

    # Read HSV values
    h = hue_slider.get()
    s = saturation_slider.get()
    v = value_slider.get()

    # HSV -> RGB
    r, g, b = hsv_to_rgb(h, s, v)

    # Synchronize RGB sliders
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

    # Update labels
    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h}°, {s}%, {v}%)"
    )

    # Update preview and HEX
    set_preview_color(r, g, b)

    updating = False


def reset_color():
    global updating

    updating = True

    # Reset RGB
    red_slider.set(0)
    green_slider.set(0)
    blue_slider.set(0)

    # Reset HSV
    hue_slider.set(0)
    saturation_slider.set(0)
    value_slider.set(0)

    # Reset labels
    rgb_value_label.config(
        text="RGB: (0, 0, 0)"
    )

    hsv_value_label.config(
        text="HSV: (0°, 0%, 0%)"
    )

    # Reset preview and HEX
    set_preview_color(0, 0, 0)

    updating = False


def random_color():
    global updating

    updating = True

    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Update RGB sliders
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

    # Convert RGB to HSV
    h, s, v = rgb_to_hsv(r, g, b)

    # Update HSV sliders
    hue_slider.set(round(h))
    saturation_slider.set(round(s))
    value_slider.set(round(v))

    # Update labels
    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h:.1f}°, {s:.1f}%, {v:.1f}%)"
    )

    # Update preview and HEX
    set_preview_color(r, g, b)

    updating = False


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="RGB ↔ HSV Color Studio",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


# -----------------------------
# Color preview
# -----------------------------

preview = tk.Frame(
    root,
    width=500,
    height=220,
    bg="#000000",
    relief="solid",
    borderwidth=1
)

preview.pack(pady=15)


hex_label = tk.Label(
    root,
    text="HEX: #000000",
    font=("Arial", 13)
)

hex_label.pack(pady=5)


# -----------------------------
# Main controls container
# -----------------------------

controls_frame = tk.Frame(root)

controls_frame.pack(pady=20)


# =================================================
# RGB CONTROLS
# =================================================

rgb_frame = tk.LabelFrame(
    controls_frame,
    text="RGB",
    font=("Arial", 13, "bold"),
    padx=20,
    pady=15
)

rgb_frame.grid(
    row=0,
    column=0,
    padx=25
)


red_slider = tk.Scale(
    rgb_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="Red",
    length=350,
    command=update_from_rgb
)

red_slider.pack()


green_slider = tk.Scale(
    rgb_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="Green",
    length=350,
    command=update_from_rgb
)

green_slider.pack()


blue_slider = tk.Scale(
    rgb_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="Blue",
    length=350,
    command=update_from_rgb
)

blue_slider.pack()


rgb_value_label = tk.Label(
    rgb_frame,
    text="RGB: (0, 0, 0)",
    font=("Arial", 11)
)

rgb_value_label.pack(pady=10)


# =================================================
# HSV CONTROLS
# =================================================

hsv_frame = tk.LabelFrame(
    controls_frame,
    text="HSV",
    font=("Arial", 13, "bold"),
    padx=20,
    pady=15
)

hsv_frame.grid(
    row=0,
    column=1,
    padx=25
)


hue_slider = tk.Scale(
    hsv_frame,
    from_=0,
    to=359,
    orient="horizontal",
    label="Hue",
    length=350,
    command=update_from_hsv
)

hue_slider.pack()


saturation_slider = tk.Scale(
    hsv_frame,
    from_=0,
    to=100,
    orient="horizontal",
    label="Saturation",
    length=350,
    command=update_from_hsv
)

saturation_slider.pack()


value_slider = tk.Scale(
    hsv_frame,
    from_=0,
    to=100,
    orient="horizontal",
    label="Value",
    length=350,
    command=update_from_hsv
)

value_slider.pack()


hsv_value_label = tk.Label(
    hsv_frame,
    text="HSV: (0°, 0%, 0%)",
    font=("Arial", 11)
)

hsv_value_label.pack(pady=10)


# -----------------------------
# Buttons
# -----------------------------

buttons_frame = tk.Frame(root)

buttons_frame.pack(pady=10)


reset_button = tk.Button(
    buttons_frame,
    text="Reset",
    font=("Arial", 11),
    width=12,
    command=reset_color
)

reset_button.pack(
    side="left",
    padx=10
)


random_button = tk.Button(
    buttons_frame,
    text="Random Color",
    font=("Arial", 11),
    width=12,
    command=random_color
)

random_button.pack(
    side="left",
    padx=10
)


# -----------------------------
# Initial state
# -----------------------------

update_from_rgb()


# -----------------------------
# Start GUI event loop
# -----------------------------

root.mainloop()