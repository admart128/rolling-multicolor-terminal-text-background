import sys
import io
import time

def cycle_colors():
    colors = [
        93, 99, 105, 111, 117, 123, 122, 121, 120, 119, 118, 190, 226, 220, 214, 208, 202, 130, 131, 132, 138, 144, 150, 156, 120, 14, 108, 102, 96, 90, 91, 92
    ]
    return colors

def main():
    colors = cycle_colors()
    color_index = 0

    try:
        while True:
            sys.stdout.write(f'\033[48;5;{colors[color_index]}m')  # Set the background color
            sys.stdout.flush()
            color_index = (color_index + 1) % len(colors)
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.stdout.write('\033[0m')  # Reset the background color
        sys.stdout.flush()
        sys.exit()

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, write_through=True)  # Disable buffering
    main()