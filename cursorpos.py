import mouse
import keyboard
import time

def get_cursor_position():
    try:
        while True:
            x, y = mouse.get_position()
            print(f"Cursor Position: X={x}, Y={y}", end='\r')
            time.sleep(0.1)
            if keyboard.is_pressed('esc'):
                break
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

if __name__ == "__main__":
    get_cursor_position()
