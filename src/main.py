import tkinter as tk
from color_converter import rgb_to_hsv


root = tk.Tk()

root.title("RGB-HSV Color Studio")
root.geometry("900x700")


def update_color(value=None):
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    # Convert RGB values to HEX color
    color = f"#{red:02x}{green:02x}{blue:02x}"

    # Update preview color
    preview.config(bg=color)

    # Convert RGB to HSV
    h, s, v = rgb_to_hsv(red, green, blue)

    # Update HSV text
    hsv_label.config(
        text=f"HSV: {h:.1f}°, {s:.1f}%, {v:.1f}%"
    )


# Color preview area
preview = tk.Frame(
    root,
    width=500,
    height=250,
    bg="#808080"
)

preview.pack(pady=40)


# Red slider
red_slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient="horizontal",
    label="Red",
    length=500,
    command=update_color
)

red_slider.pack()


# Green slider
green_slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient="horizontal",
    label="Green",
    length=500,
    command=update_color
)

green_slider.pack()


# Blue slider
blue_slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient="horizontal",
    label="Blue",
    length=500,
    command=update_color
)

blue_slider.pack()


# HSV result text
hsv_label = tk.Label(
    root,
    text="HSV: 0.0°, 0.0%, 0.0%",
    font=("Arial", 14)
)

hsv_label.pack(pady=20)


root.mainloop()