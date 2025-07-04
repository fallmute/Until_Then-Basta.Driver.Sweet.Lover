import argparse
import threading
import time
import keyboard

parser = argparse.ArgumentParser(description="Скрипт для выполнения достижения Basta Driver, Sweet Lover")
parser.add_argument(
    "--interval",
    "-i",
    type=float,
    required=True,
    help="An interval in the form of a floating-point number, for example 1.0052"
)

args = parser.parse_args()
interval = args.interval

running = False

lock = threading.Lock()


def spam_space():
    global interval, press_count, running
    while True:

        time.sleep(0.01)

        with lock:
            if not running:
                continue
        
        keyboard.press_and_release('space')
        time.sleep(interval)


def toggle_running():
    global running
    with lock:
        running = not running
        state = "STARTED" if running else "STOPPED"
    print(f"[+] Autospammer {state}")


def main():
    worker = threading.Thread(target=spam_space, daemon=True)
    worker.start()

    keyboard.add_hotkey('space', toggle_running)
    print("Нажмите Space для старта/стопа автонажатия пробела.")
    print("Нажмите Ctrl+C в консоли для выхода.")

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n[!] Exit - Ctrl+C")
    finally:
        pass


if __name__ == '__main__':
    main()
     