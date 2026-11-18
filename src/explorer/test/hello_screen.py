

from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
GREEN = display.create_pen(0, 255, 0)
WHITE = display.create_pen(255, 255, 255)

display.set_pen(GREEN)
display.clear()
display.set_pen(WHITE)
display.text("Explorer \n\nReady! \n\nDude", 20, 100, scale=3)
display.update()


