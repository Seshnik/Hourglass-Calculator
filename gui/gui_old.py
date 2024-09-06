from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.font as tkfont
import pyglet


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x450")
window.configure(bg = "#FFFFFF")

# Load custom font
pyglet.font.add_file(str(relative_to_assets("TradeWinds.ttf")))

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_text(
    249.0,
    0.0,
    anchor="nw",
    text="Hourglass Calculator",
    fill="#1CF0BB",
    font=("TradeWinds", 24 * -1)
)

canvas.create_rectangle(
    232.0,
    64.0,
    665.0,
    67.0,
    fill="#19D8A7",
    outline="")

canvas.create_text(
    11.0,
    117.0,
    anchor="nw",
    text="Current Level:",
    fill="#1CF0BB",
    font=("TradeWinds", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    273.0,
    137.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#22192E",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=231.5,
    y=125.0,
    width=83.0,
    height=23.0
)

canvas.create_text(
    11.0,
    181.0,
    anchor="nw",
    text="Target Level:",
    fill="#1CF0BB",
    font=("TradeWinds", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    273.0,
    200.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#22192E",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=230.0,
    y=189.0,
    width=86.0,
    height=20.0
)

canvas.create_text(
    11.0,
    242.0,
    anchor="nw",
    text="Win-rate %:",
    fill="#1CF0BB",
    font=("TradeWinds", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    273.0,
    261.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#22192E",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=230.0,
    y=250.0,
    width=86.0,
    height=20.0
)

canvas.create_text(
    11.0,
    303.0,
    anchor="nw",
    text="EXP Boost:",
    fill="#1CF0BB",
    font=("TradeWinds", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    273.0,
    320.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#22192E",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=231.5,
    y=308.0,
    width=83.0,
    height=23.0
)

canvas.create_rectangle(
    524.9999851818393,
    100.0,
    528.0,
    442.0,
    fill="#19D8A7",
    outline="")

canvas.create_rectangle(
    888.9999851818393,
    100.0,
    892.0,
    442.0,
    fill="#19D8A7",
    outline="")

canvas.create_rectangle(
    525.0,
    99.99999999999989,
    892.0,
    103.0,
    fill="#19D8A7",
    outline="")

canvas.create_rectangle(
    525.0,
    438.9999999999999,
    892.0,
    442.0,
    fill="#19D8A7",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=94.626708984375,
    y=363.65966796875,
    width=159.33058166503906,
    height=47.35658264160156
)
window.resizable(False, False)
window.mainloop()