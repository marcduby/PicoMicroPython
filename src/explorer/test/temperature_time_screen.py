import time
import machine
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
GREEN = display.create_pen(0, 255, 0)
WHITE = display.create_pen(255, 255, 255)
DARK_BLUE = display.create_pen(20, 20, 40)

# Internal temperature sensor on ADC channel 4 (CORE_TEMP)
sensor_temp = machine.ADC(getattr(machine.ADC, "CORE_TEMP", 4))
conversion_factor = 3.3 / 65535

rtc = machine.RTC()
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

SCALE = 3

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temp_c = 27 - (reading - 0.706) / 0.001721
    temp_f = (temp_c * 9 / 5) + 32

    year, month, day, weekday, hour, minute, second, _ = rtc.datetime()
    date_str = year
    # date_str = f"{DAYS[weekday % 7]} {year:04d}-{month:02d}-{day:02d}"
    # time_str = f"{hour:02d}:{minute:02d}:{second:02d}"

    display.set_pen(DARK_BLUE)
    display.clear()
    display.set_pen(WHITE)
    # display.text(
    #     f"Pico Temp:\n\n{temp_c:.1f} C\n\n{temp_f:.1f} F \n\n {date_str}",
    #     20,
    #     50,
    #     scale=3,
    # )

    display.text("Pico Temp:", 10, 10, scale=SCALE)
    display.text(f"{temp_c:.1f} C", 10, 45, scale=SCALE)
    display.text(f"{temp_f:.1f} F", 10, 85, scale=SCALE)
    # display.text(date_str, 10, 130, scale=SCALE)
    display.text(f"{DAYS[weekday % 7]} {year:04d}-{month:02d}-{day:02d}", 10, 130, scale=SCALE)

    display.update()

    time.sleep(60)
