
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
GREEN = display.create_pen(0, 255, 0)
WHITE = display.create_pen(255, 255, 255)
DARK_BLUE = display.create_pen(20, 20, 40)

FACTOR = 361/240


# draw horizontal line
def horizontal(left, top, right):
    line = right - left + 1
    for i in range(line):
        display.pixel(left + i, top)
        display.pixel(left + i, top + 1)
        display.pixel(left + i, top + 2)

# background
display.set_pen(DARK_BLUE)
display.clear()

# display.set_pen(GREEN)
# display.clear()


# sine wave
# display.set_pen(80, 80, 80)
# display.set_pen(255, 255, 255)

display.set_pen(WHITE)
horizontal(left=0, top=60, right=239)
# for i in range(100):
#     display.pixel(0 + i, 100)
display.update()


# display.set_pen(WHITE)
# display.text("Explorer \n\nReady! \n\nDude", 20, 100, scale=3)
# display.update()


