import time
import board
import usb_hid
import digitalio
import neopixel


from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

led_red = (10,0,0)
led_green = (0,10,0)
led_blue = (0,0,10)
led_white = (10,10,10)
led_cyan = (0,10,10)
led_yellow = (10,10,0)
led_magenta = (10,0,10)
led_off = (0,0,0)

def blinken():
	pixel.fill(led_green)
	time.sleep(0.5)
	pixel.fill(led_off)
	time.sleep(0.5)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.2
y =1 
while True:
	verz = 188			# Wiederholzeit in sekunden
	pixel.fill(led_red)
	mouse.move(0, y)
	time.sleep(0.1)
	y = y * -1
	mouse.move(0, y)
	pixel.fill(led_off)
	while(verz >>0):
		blinken()
		verz= verz-1

