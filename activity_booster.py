import pyautogui
import pywinctl as pw
import time
import random
import string
import argparse
from datetime import datetime, timezone

# Failsafe: move mouse to top-left corner to abort
pyautogui.FAILSAFE = True

# List of keys to randomly press
KEYS = list(string.ascii_lowercase) + ["space"]

def random_mouse_movement(max_delta=50, steps=5):
    """Move the mouse randomly and return to original position."""
    x, y = pyautogui.position()
    for _ in range(steps):
        dx = random.randint(-max_delta, max_delta)
        dy = random.randint(-max_delta, max_delta)
        pyautogui.moveTo(x + dx, y + dy, duration=0.1)
    pyautogui.moveTo(x, y, duration=0.1)

def random_key_press():
    """Press a random key from A-Z or space."""
    key = random.choice(KEYS)
    pyautogui.press(key)

def get_active_window_title():
    try:
        win = pw.getActiveWindow()
        if not win:
            return "<no-active-window>"
        return win.title or "<untitled-window>"
    except Exception:
        return "<error-getting-window>"

def run_agent(duration_minutes=1, interval_seconds=0.5):
    end_time = time.time() + duration_minutes * 60
    iteration = 0
    print(f"Running agent for {duration_minutes} minute(s). Ctrl+C or move mouse to top-left to stop.")
    while time.time() < end_time:
        iteration += 1
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        window_title = "get_active_window_title()"
        # print(f"[{timestamp}] Iteration {iteration} | Active window: {window_title}")
        
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        print(f" {minutes} min {seconds} sec")

        # Simulate random mouse movement
        random_mouse_movement()

        # Simulate random key press
        random_key_press()

        # Wait before necgibysxt action
        time.sleep(interval_seconds)
 
if __name__ == "__main__":
    minutes = 120
    interval = 0.5
    run_agent(minutes, interval)

