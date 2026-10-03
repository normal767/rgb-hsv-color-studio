import tkinter as tk


root = tk.Tk()

root.title("RGB-HSV Color Studio")
root.geometry("900x600")
def update_color(value=None):
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    color = f"#{red:02x}{green:02x}{blue:02x}"
    preview.config(bg=color)

preview = tk.Frame(
    root,
    width=400,
    height=200,
    bg="#808080"
)

preview.pack(pady=50)

red_slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient="horizontal",
    label="Red",
    length=400,
    command=update_color
)

red_slider.pack()

green_slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient="horizontal",
    label="Green",
    length=400,
    command=update_color
)

green_slider.pack()

blue_slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient="horizontal",
    label="Blue",
    length=400,
    command=update_color
)

blue_slider.pack()
root.mainloop()