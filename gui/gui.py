from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkextrafont import Font as eFont, load as load_fonts

# import pyglet

# Define paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


# Function to construct full asset paths
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Initialize the main window
window = Tk()
window.geometry("900x450")
window.configure(bg="#FFFFFF")

# Attempt to load the custom font
try:
    load_fonts(window)  # Initialize tkextrafont
    custom_font = eFont(file=relative_to_assets("TradeWinds-Regular.ttf"), family="Trade Winds")
except Exception as e:
    print(f"Failed to load custom font: {e}")
    custom_font = ("Arial", 24)  # Fallback to a default font

# Create and place the canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=450,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load and place the image
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(450.0, 300.0, image=image_image_1)

# Create text using the custom font
canvas.create_text(
    249.0,
    0.0,
    anchor="nw",
    text="Hourglass Calculator",
    fill="#1CF0BB",
    font=(custom_font, 24)
)

canvas.create_rectangle(
    232.0,
    64.0,
    665.0,
    67.0,
    fill="#19D8A7",
    outline=""
)

canvas.create_text(
    11.0,
    117.0,
    anchor="nw",
    text="Current Level:",
    fill="#1CF0BB",
    font=(custom_font, 20)
)

# Create entries for input
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(273.0, 137.5, image=entry_image_1)
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
    font=(custom_font, 20)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(273.0, 200.0, image=entry_image_2)
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
    font=(custom_font, 20)
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(273.0, 261.0, image=entry_image_3)
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
    font=(custom_font, 20)
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(273.0, 320.5, image=entry_image_4)
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

# Create rectangles for the design
canvas.create_rectangle(
    525.0,
    100.0,
    528.0,
    442.0,
    fill="#19D8A7",
    outline=""
)

canvas.create_rectangle(
    889.0,
    100.0,
    892.0,
    442.0,
    fill="#19D8A7",
    outline=""
)

canvas.create_rectangle(
    525.0,
    100.0,
    892.0,
    103.0,
    fill="#19D8A7",
    outline=""
)

canvas.create_rectangle(
    525.0,
    439.0,
    892.0,
    442.0,
    fill="#19D8A7",
    outline=""
)

# Add a button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=94.6,
    y=363.7,
    width=159.3,
    height=47.4
)

# Disable window resizing
window.resizable(False, False)

# Start the main event loop
window.mainloop()
