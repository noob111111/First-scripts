from PIL import Image, ImageTk
import tkinter as tk

def load_rgb_values(file_path):
    rgb_values = []
    with open(file_path, 'r') as f:
        for line in f:
            # Parse each line and convert string representation of RGB tuple to tuple
            rgb_values.append(tuple(map(int, line.strip()[1:-1].split(', '))))
    return rgb_values

def create_image(rgb_values):
    # Create a new image with the given RGB values
    img = Image.new('RGB', (51, 39))
    pixels = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # Set RGB values for each pixel
            pixels[x, y] = rgb_values[y * img.size[0] + x]
    return img

def display_image(rgb_values):
    img = create_image(rgb_values)

    # Display the image using Tkinter
    root = tk.Tk()
    root.title("RGB Image Viewer")

    # Convert the image to a format compatible with Tkinter
    tk_img = ImageTk.PhotoImage(img)

    # Create a label to display the image
    label = tk.Label(root, image=tk_img)
    label.pack()

    # Keep the window open
    root.mainloop()

if __name__ == "__main__":
    rgb_values = load_rgb_values("rgb_values.txt")
    display_image(rgb_values)
 