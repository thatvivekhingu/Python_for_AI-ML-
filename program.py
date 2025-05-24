import pyautogui
import pyperclip
import time

# Wait for 3 seconds to allow user to switch to the desired screen
time.sleep(3)

# Step 1: Click on the icon at (983, 1054)
pyautogui.click(1312, 1051)
pyautogui.click(1416,920)
time.sleep(1)  # wait for UI to react

# Step 2: Drag from (672, 197) to (1893, 902) to select text
pyautogui.moveTo(756,226)
pyautogui.dragTo(804, 946, duration=1, button='left')

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # give time for clipboard to update

# Step 4: Get text from clipboard
copied_text = pyperclip.paste()

# Output the copied text
print("Copied Text:", copied_text)
