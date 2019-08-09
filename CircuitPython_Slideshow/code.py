import board
from adafruit_slideshow import PlayBackOrder, SlideShow
import pulseio

# Create the slideshow object that plays through once alphabetically.
slideshow = SlideShow(board.DISPLAY,
					  folder="/images", loop=True,
					  order=PlayBackOrder.ALPHABETICAL, dwell=60)

while slideshow.update():
    pass