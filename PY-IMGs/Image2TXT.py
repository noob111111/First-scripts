import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab, Image

def process_image():
    try:
        # Grab the latest image from clipboard
        img = ImageGrab.grabclipboard()
        if img is None:
            messagebox.showerror("Error", "No image found in clipboard.")
            return

        # Convert image to 51:39 ratio
        img = img.resize((51, 39), Image.LANCZOS)

        # Get RGB values for each pixel
        rgb_values = []
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                rgb_values.append(img.getpixel((x, y))[:3])  # Extract only RGB values, ignoring alpha channel

        # Write RGB values to a text file
        with open("rgb_values.txt", "w") as f:
            for rgb in rgb_values:
                f.write(f"{rgb}\n")

        messagebox.showinfo("Success", "RGB values extracted and saved to rgb_values.txt.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Image Processor")

button = tk.Button(root, text="Process Image", command=process_image)
button.pack(pady=20)

root.mainloop()
