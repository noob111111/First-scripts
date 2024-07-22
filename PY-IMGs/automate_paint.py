import pyautogui
import time
import keyboard

# Read the files
with open('coordinates.txt', 'r') as coord_file:
    coordinates = coord_file.readlines()

with open('paint.txt', 'r') as paint_file:
    paint_coords = paint_file.readlines()

with open('rgb_values.txt', 'r') as rgb_file:
    rgb_values = rgb_file.readlines()

# Parse the paint coordinates
paint_positions = []
for line in paint_coords:
    x, y = map(int, line.strip().split(','))
    paint_positions.append((x, y))

# Function to check for termination key
def check_termination():
    if keyboard.is_pressed('esc'):
        print("Terminating script...")
        exit()

# Loop through the coordinates and rgb_values
for i in range(len(coordinates)):
    # Check for termination key
    check_termination()

    # Get the current RGB values
    rgb = rgb_values[i].strip().strip('()').split(', ')
    r, g, b = rgb

    # Debugging output
    print(f"RGB values: {r}, {g}, {b}")

    # Input RGB values
    for j, (x, y) in enumerate(paint_positions):
        print(f"Moving to RGB input field at ({x}, {y})")
        pyautogui.moveTo(x, y)
        time.sleep(0.2)  # Small delay to ensure the move is completed
        pyautogui.click()
        time.sleep(0.2)  # Small delay before typing
        pyautogui.typewrite(rgb[j])
        time.sleep(0.2)  # Small delay after typing

    # Get the current coordinates
    x, y = map(int, coordinates[i].strip().split(','))
    
    # Debugging output
    print(f"Moving to paint coordinates at ({x}, {y})")
    pyautogui.moveTo(x, y)
    time.sleep(0.2)  # Small delay to ensure the move is completed
    pyautogui.click()
    time.sleep(0.2)  # Small delay after clicking

    # Add a small delay to prevent too fast execution
    time.sleep(0.2)
