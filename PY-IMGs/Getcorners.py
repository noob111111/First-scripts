import pyautogui
import time

def get_click_position(prompt):
    print(prompt)
    time.sleep(2)  # Give you time to move the mouse to the desired location
    x, y = pyautogui.position()
    print(f"Position captured: ({x}, {y})")
    return x, y

def calculate_coordinates(top_left, top_right, bottom_left, bottom_right, rows, columns):
    coordinates = []
    width = top_right[0] - top_left[0]
    height = bottom_left[1] - top_left[1]

    block_width = width / (columns - 1)
    block_height = height / (rows - 1)

    for row in range(rows):
        for col in range(columns):
            x = top_left[0] + col * block_width
            y = top_left[1] + row * block_height
            coordinates.append((int(x), int(y)))

    return coordinates

def save_coordinates_to_file(coordinates, filename="coordinates.txt"):
    with open(filename, "w") as f:
        for coord in coordinates:
            f.write(f"{coord[0]},{coord[1]}\n")

def main():
    rows, columns = 51, 39

    print("Move your mouse to the top-left corner and wait...")
    top_left = get_click_position("Top-left corner captured.")
    
    print("Move your mouse to the top-right corner and wait...")
    top_right = get_click_position("Top-right corner captured.")
    
    print("Move your mouse to the bottom-left corner and wait...")
    bottom_left = get_click_position("Bottom-left corner captured.")
    
    print("Move your mouse to the bottom-right corner and wait...")
    bottom_right = get_click_position("Bottom-right corner captured.")
    
    coordinates = calculate_coordinates(top_left, top_right, bottom_left, bottom_right, rows, columns)
    save_coordinates_to_file(coordinates)

    print(f"Coordinates saved to coordinates.txt")

if __name__ == "__main__":
    main()
