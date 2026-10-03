import tkinter as tk
import random

from color_converter import rgb_to_hsv, hsv_to_rgb


root = tk.Tk()
root.title("RGB-HSV Color Studio")
root.geometry("1180x800")
root.minsize(1050, 720)
root.resizable(True, True)

updating = False

SV_WIDTH = 360
SV_HEIGHT = 220


def get_current_hex():
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()

    return f"#{r:02X}{g:02X}{b:02X}"


def set_preview_color(r, g, b):
    color = f"#{r:02x}{g:02x}{b:02x}"

    preview.config(bg=color)

    hex_label.config(
        text=f"HEX: {color.upper()}"
    )

    copy_status_label.config(text="")


def copy_hex():
    color = get_current_hex()

    root.clipboard_clear()
    root.clipboard_append(color)
    root.update()

    copy_status_label.config(
        text="Copied!"
    )


def update_hue_indicator(h):
    hue_canvas.delete("hue_indicator")

    x = max(0, min(359, int(h)))

    hue_canvas.create_line(
        x,
        0,
        x,
        30,
        fill="white",
        width=3,
        tags="hue_indicator"
    )

    hue_canvas.create_line(
        x + 1,
        0,
        x + 1,
        30,
        fill="black",
        width=1,
        tags="hue_indicator"
    )


def update_sv_indicator(s, v):
    sv_canvas.delete("sv_indicator")

    x = (s / 100) * SV_WIDTH
    y = (1 - v / 100) * SV_HEIGHT

    radius = 6

    sv_canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        outline="white",
        width=2,
        tags="sv_indicator"
    )

    sv_canvas.create_oval(
        x - radius - 1,
        y - radius - 1,
        x + radius + 1,
        y + radius + 1,
        outline="black",
        width=1,
        tags="sv_indicator"
    )


def draw_hue_bar():
    hue_canvas.delete("all")

    for h in range(360):
        r, g, b = hsv_to_rgb(h, 100, 100)
        color = f"#{r:02x}{g:02x}{b:02x}"

        hue_canvas.create_line(
            h,
            0,
            h,
            30,
            fill=color
        )


def draw_sv_palette():
    sv_canvas.delete("all")

    h = hue_slider.get()
    step = 4

    for x in range(0, SV_WIDTH, step):
        s = (x / SV_WIDTH) * 100

        for y in range(0, SV_HEIGHT, step):
            v = (1 - y / SV_HEIGHT) * 100

            r, g, b = hsv_to_rgb(h, s, v)
            color = f"#{r:02x}{g:02x}{b:02x}"

            sv_canvas.create_rectangle(
                x,
                y,
                x + step,
                y + step,
                outline=color,
                fill=color
            )


def update_from_rgb(value=None):
    global updating

    if updating:
        return

    updating = True

    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()

    h, s, v = rgb_to_hsv(r, g, b)

    hue_slider.set(round(h))
    saturation_slider.set(round(s))
    value_slider.set(round(v))

    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h:.1f}°, {s:.1f}%, {v:.1f}%)"
    )

    set_preview_color(r, g, b)

    update_hue_indicator(h)

    draw_sv_palette()
    update_sv_indicator(s, v)

    updating = False


def update_from_hsv(value=None):
    global updating

    if updating:
        return

    updating = True

    h = hue_slider.get()
    s = saturation_slider.get()
    v = value_slider.get()

    r, g, b = hsv_to_rgb(h, s, v)

    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h}°, {s}%, {v}%)"
    )

    set_preview_color(r, g, b)

    update_hue_indicator(h)

    draw_sv_palette()
    update_sv_indicator(s, v)

    updating = False


def reset_color():
    global updating

    updating = True

    red_slider.set(0)
    green_slider.set(0)
    blue_slider.set(0)

    hue_slider.set(0)
    saturation_slider.set(0)
    value_slider.set(0)

    rgb_value_label.config(
        text="RGB: (0, 0, 0)"
    )

    hsv_value_label.config(
        text="HSV: (0°, 0%, 0%)"
    )

    set_preview_color(0, 0, 0)

    update_hue_indicator(0)

    draw_sv_palette()
    update_sv_indicator(0, 0)

    updating = False


def random_color():
    global updating

    updating = True

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

    h, s, v = rgb_to_hsv(r, g, b)

    hue_slider.set(round(h))
    saturation_slider.set(round(s))
    value_slider.set(round(v))

    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h:.1f}°, {s:.1f}%, {v:.1f}%)"
    )

    set_preview_color(r, g, b)

    update_hue_indicator(h)

    draw_sv_palette()
    update_sv_indicator(s, v)

    updating = False


def select_hue(event):
    global updating

    x = max(0, min(359, event.x))

    updating = True

    hue_slider.set(x)

    h = x
    s = saturation_slider.get()
    v = value_slider.get()

    r, g, b = hsv_to_rgb(h, s, v)

    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h}°, {s}%, {v}%)"
    )

    set_preview_color(r, g, b)

    update_hue_indicator(h)

    draw_sv_palette()
    update_sv_indicator(s, v)

    updating = False


def select_sv(event):
    global updating

    x = max(0, min(SV_WIDTH, event.x))
    y = max(0, min(SV_HEIGHT, event.y))

    s = (x / SV_WIDTH) * 100
    v = (1 - y / SV_HEIGHT) * 100

    h = hue_slider.get()

    updating = True

    saturation_slider.set(round(s))
    value_slider.set(round(v))

    r, g, b = hsv_to_rgb(h, s, v)

    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

    rgb_value_label.config(
        text=f"RGB: ({r}, {g}, {b})"
    )

    hsv_value_label.config(
        text=f"HSV: ({h}°, {s:.1f}%, {v:.1f}%)"
    )

    set_preview_color(r, g, b)

    update_sv_indicator(s, v)

    updating = False


# =================================================
# Main layout
# =================================================

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)


# -----------------------------
# Header
# -----------------------------

header_frame = tk.Frame(root)

header_frame.grid(
    row=0,
    column=0,
    pady=(15, 5)
)


title_label = tk.Label(
    header_frame,
    text="RGB ↔ HSV Color Studio",
    font=("Arial", 22, "bold")
)

title_label.pack()


subtitle_label = tk.Label(
    header_frame,
    text="Interactive RGB and HSV color model explorer",
    font=("Arial", 10)
)

subtitle_label.pack(pady=(3, 0))


# -----------------------------
# Top area
# -----------------------------

top_frame = tk.Frame(root)

top_frame.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=25
)

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)


# =================================================
# LEFT: Color Preview
# =================================================

preview_frame = tk.LabelFrame(
    top_frame,
    text="Current Color",
    font=("Arial", 13, "bold"),
    padx=20,
    pady=15
)

preview_frame.grid(
    row=0,
    column=0,
    padx=15,
    pady=10,
    sticky="nsew"
)


preview = tk.Frame(
    preview_frame,
    width=430,
    height=280,
    bg="#000000",
    relief="solid",
    borderwidth=1
)

preview.pack(
    pady=(10, 15)
)


hex_info_frame = tk.Frame(
    preview_frame
)

hex_info_frame.pack(
    pady=5
)


hex_label = tk.Label(
    hex_info_frame,
    text="HEX: #000000",
    font=("Arial", 14, "bold")
)

hex_label.pack(
    side="left",
    padx=(0, 10)
)


copy_hex_button = tk.Button(
    hex_info_frame,
    text="Copy HEX",
    width=10,
    command=copy_hex
)

copy_hex_button.pack(
    side="left"
)


copy_status_label = tk.Label(
    preview_frame,
    text="",
    font=("Arial", 9)
)

copy_status_label.pack()


# =================================================
# RIGHT: HSV Picker
# =================================================

picker_frame = tk.LabelFrame(
    top_frame,
    text="Interactive HSV Picker",
    font=("Arial", 13, "bold"),
    padx=20,
    pady=15
)

picker_frame.grid(
    row=0,
    column=1,
    padx=15,
    pady=10,
    sticky="nsew"
)


hue_bar_label = tk.Label(
    picker_frame,
    text="Hue Spectrum",
    font=("Arial", 11, "bold")
)

hue_bar_label.pack(
    pady=(5, 4)
)


hue_canvas = tk.Canvas(
    picker_frame,
    width=360,
    height=30,
    highlightthickness=1,
    highlightbackground="#999999"
)

hue_canvas.pack(
    pady=(0, 15)
)

hue_canvas.bind(
    "<Button-1>",
    select_hue
)

hue_canvas.bind(
    "<B1-Motion>",
    select_hue
)


sv_label = tk.Label(
    picker_frame,
    text="Saturation × Value",
    font=("Arial", 11, "bold")
)

sv_label.pack(
    pady=(0, 4)
)


sv_canvas = tk.Canvas(
    picker_frame,
    width=SV_WIDTH,
    height=SV_HEIGHT,
    highlightthickness=1,
    highlightbackground="#999999"
)

sv_canvas.pack(
    pady=(0, 5)
)

sv_canvas.bind(
    "<Button-1>",
    select_sv
)

sv_canvas.bind(
    "<B1-Motion>",
    select_sv
)


# =================================================
# RGB / HSV controls
# =================================================

controls_frame = tk.Frame(root)

controls_frame.grid(
    row=2,
    column=0,
    padx=25,
    pady=10,
    sticky="nsew"
)

controls_frame.columnconfigure(
    0,
    weight=1
)

controls_frame.columnconfigure(
    1,
    weight=1
)


# -----------------------------
# RGB
# -----------------------------

rgb_frame = tk.LabelFrame(
    controls_frame,
    text="RGB Channels",
    font=("Arial", 13, "bold"),
    padx=15,
    pady=10
)

rgb_frame.grid(
    row=0,
    column=0,
    padx=15,
    sticky="ew"
)


red_slider = tk.Scale(
    rgb_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="Red",
    length=400,
    command=update_from_rgb
)

red_slider.pack(
    fill="x"
)


green_slider = tk.Scale(
    rgb_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="Green",
    length=400,
    command=update_from_rgb
)

green_slider.pack(
    fill="x"
)


blue_slider = tk.Scale(
    rgb_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="Blue",
    length=400,
    command=update_from_rgb
)

blue_slider.pack(
    fill="x"
)


rgb_value_label = tk.Label(
    rgb_frame,
    text="RGB: (0, 0, 0)",
    font=("Arial", 11, "bold")
)

rgb_value_label.pack(
    pady=5
)


# -----------------------------
# HSV
# -----------------------------

hsv_frame = tk.LabelFrame(
    controls_frame,
    text="HSV Model",
    font=("Arial", 13, "bold"),
    padx=15,
    pady=10
)

hsv_frame.grid(
    row=0,
    column=1,
    padx=15,
    sticky="ew"
)


hue_slider = tk.Scale(
    hsv_frame,
    from_=0,
    to=359,
    orient="horizontal",
    label="Hue",
    length=400,
    command=update_from_hsv
)

hue_slider.pack(
    fill="x"
)


saturation_slider = tk.Scale(
    hsv_frame,
    from_=0,
    to=100,
    orient="horizontal",
    label="Saturation",
    length=400,
    command=update_from_hsv
)

saturation_slider.pack(
    fill="x"
)


value_slider = tk.Scale(
    hsv_frame,
    from_=0,
    to=100,
    orient="horizontal",
    label="Value",
    length=400,
    command=update_from_hsv
)

value_slider.pack(
    fill="x"
)


hsv_value_label = tk.Label(
    hsv_frame,
    text="HSV: (0°, 0%, 0%)",
    font=("Arial", 11, "bold")
)

hsv_value_label.pack(
    pady=5
)


# =================================================
# Buttons
# =================================================

buttons_frame = tk.Frame(root)

buttons_frame.grid(
    row=3,
    column=0,
    pady=(5, 15)
)


random_button = tk.Button(
    buttons_frame,
    text="Random Color",
    font=("Arial", 11),
    width=14,
    command=random_color
)

random_button.pack(
    side="left",
    padx=10
)


reset_button = tk.Button(
    buttons_frame,
    text="Reset",
    font=("Arial", 11),
    width=14,
    command=reset_color
)

reset_button.pack(
    side="left",
    padx=10
)


# =================================================
# Initial state
# =================================================

draw_hue_bar()

update_hue_indicator(0)

draw_sv_palette()

update_sv_indicator(0, 0)

update_from_rgb()


root.mainloop()