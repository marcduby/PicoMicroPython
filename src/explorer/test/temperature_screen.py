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

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temp_c = 27 - (reading - 0.706) / 0.001721
    temp_f = (temp_c * 9 / 5) + 32

    display.set_pen(DARK_BLUE)
    display.clear()
    display.set_pen(WHITE)
    display.text(
        f"Pico Temp:\n\n{temp_c:.1f} C\n\n{temp_f:.1f} F",
        20,
        50,
        scale=3,
    )
    display.update()

    time.sleep(60)
