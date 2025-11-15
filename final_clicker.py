# transcript_clicker.py
# Minimal pyautogui clicker for your transcript workflow
# Abort any time by moving the mouse to the top-left corner.

import time
import sys

try:
    import pyautogui
except ImportError:
    print("Install dependencies: pip install pyautogui pillow")
    sys.exit(1)

pyautogui.FAILSAFE = True  # move mouse to top-left to abort

# Coordinates as (x, y). Update these to match your screen if needed.
CLICK_SEQUENCE = [
    (796, 485),   # 1
    (1005, 744),  # 2
    (854, 745),   # 3
    (875, 743),   # 4
    (877, 738),   # 5 paste here
    (1194, 73),   # 6
    (108, 194),   # 7
    (1194, 73),   # 8
    (1276, 193),  # 9
]

# Optional per-step sleeps in seconds
SLEEP_AFTER = {
    0: 0.5, 1: 0.5, 2: 0.5, 3: 0.7, 4: 1.0, 5: 0.7, 6: 0.7, 7: 0.7, 8: 0.7
}

# Steps where we paste with Ctrl+V (use zero-based indices)
PASTE_STEPS = {4}

# Steps that should scroll after clicking: index -> amount (negative scrolls down)
SCROLL_AFTER = {1: -300, 8: -800}

def main():
    print("Starting in 3 seconds. Move mouse to top-left to abort.")
    time.sleep(3)

    total = len(CLICK_SEQUENCE)
    for i, (x, y) in enumerate(CLICK_SEQUENCE):
        print(f"[{i+1}/{total}] Click at ({x}, {y})")
        pyautogui.click(x=x, y=y)

        if i in PASTE_STEPS:
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "v")
            print("  pasted")

        if i in SCROLL_AFTER:
            amt = SCROLL_AFTER[i]
            time.sleep(0.2)
            pyautogui.scroll(amt)
            print(f"  scrolled {amt}")

        time.sleep(SLEEP_AFTER.get(i, 0.5))

    print("Done.")

if __name__ == "__main__":
    main()
