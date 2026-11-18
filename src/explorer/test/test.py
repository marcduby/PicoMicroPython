import time
from machine import RTC
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

# Initialize the 240x240 IPS LCD on the Pico Explorer Base
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
WIDTH, HEIGHT = display.get_bounds()

# Define Pens (RGB)
BG_PEN = display.create_pen(20, 20, 40)       # Dark blue background
TEXT_PEN = display.create_pen(255, 255, 255)  # White text for time
DATE_PEN = display.create_pen(160, 200, 255)  # Light blue text for date
ACCENT_PEN = display.create_pen(0, 200, 140)  # Teal accent line

display.set_font("bitmap8")

rtc = RTC()

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def draw_centered_text(text, y, scale, pen):
    display.set_pen(pen)
    text_width = display.measure_text(text, scale)
    x = max(0, (WIDTH - text_width) // 2)
    display.text(text, x, y, WIDTH, scale)


while True:
    # RTC().datetime() returns (year, month, day, weekday, hours, minutes, seconds, subseconds)
    year, month, day, weekday, hour, minute, second, _ = rtc.datetime()

    date_str = f"{DAYS[weekday % 7]} {year:04d}-{month:02d}-{day:02d}"
    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"

    # Clear screen
    display.set_pen(BG_PEN)
    display.clear()

    # Draw header & divider
    draw_centered_text("PICO EXPLORER", 35, 2, ACCENT_PEN)
    display.line(20, 65, WIDTH - 20, 65)

    # Draw time and date
    draw_centered_text(time_str, 105, 4, TEXT_PEN)
    draw_centered_text(date_str, 165, 2, DATE_PEN)

    # Push buffer to the LCD screen
    display.update()

    time.sleep(0.2)
