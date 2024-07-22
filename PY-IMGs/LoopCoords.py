import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Current mouse position: ({x}, {y})")
        time.sleep(1)  # Adjust the sleep time if you want faster/slower updates
except KeyboardInterrupt:
    print("Script terminated by user.")
