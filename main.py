import os
import random
import string
import tkinter as tk
from tkinter import filedialog

def generate_name():
    """Generate a recognizable name for a file."""
    prefix_list = [
        "Ball", "Keyboard", "Computer", "Mouse", "Eagle", "Cobra", "Horse", "Jupiter", "Saturn", "Mars",
        "Venus", "Banana", "Strawberry", "Car", "Bus", "Train", "Plane", "Boat", "Helicopter", "Guitar",
        "Piano", "Trumpet", "Flute", "Violin", "Camera", "Phone", "Watch", "Sunglasses", "Hat", "Jacket",
        "Shirt", "Dress", "Shoes", "Boots", "Socks", "Book", "Magazine", "Newspaper", "Map", "Globe",
        "Telescope", "Microscope", "Compass", "Calculator", "Ruler", "Pen", "Pencil", "Marker", "Eraser",
        "Stapler", "Scissors", "Tape", "Glue", "Paintbrush", "Canvas", "Easel", "Sculpture", "Pottery",
        "Candles", "Incense", "Perfume", "Soap", "Shampoo", "Toothbrush", "Toothpaste", "Floss", "Mouthwash",
        "Deodorant", "Razor", "Shaving cream", "Tissue", "Towel", "Bed", "Pillow", "Blanket", "Lamp",
        "Desk", "Chair", "Sofa", "Table", "Plant", "Vase", "Picture frame", "Clock", "Candlestick", "Bowl",
        "Plate", "Cup", "Glass", "Fork", "Spoon", "Knife", "Cutting board", "Oven", "Refrigerator",
        "Microwave", "Blender", "Coffee maker", "Toaster", "Dishwasher"
    ]

    suffix = "".join(random.choices(string.digits, k=1))
    prefix = random.choice(prefix_list)
    return prefix + "_" + suffix + ".jpg"

def rename_files(file_list):
    """Rename selected files with recognizable names."""
    for file_path in file_list:
        directory, filename = os.path.split(file_path)
        if filename.endswith(".jpg"):
            new_filename = generate_name()
            os.rename(file_path, os.path.join(directory, new_filename))

def select_files():
    """Open a file dialog to select files to rename."""
    filetypes = (("JPEG files", "*.jpg"), ("All files", "*.*"))
    file_list = filedialog.askopenfilenames(title="Select files to rename", filetypes=filetypes)
    rename_files(file_list)

# Create GUI
root = tk.Tk()
root.title("Rename Files")
root.geometry("300x100")

# Add file select button
select_button = tk.Button(root, text="Select Files", command=select_files)
select_button.pack(pady=10)

# Start GUI event loop
root.mainloop()
