from machine import Pin
import time

clk = Pin(16, Pin.IN, Pin.PULL_UP)
dt = Pin(17, Pin.IN, Pin.PULL_UP)
sw = Pin(18, Pin.IN, Pin.PULL_UP)

previous_value = True
button_down = False

while True:
    #print("dir", dt.value(), "step", clk.value(), "button", sw.value())
    if previous_value != clk.value():
        if clk.value() == False:
            if dt.value() == False:
                print("turned left")
            else:
                print("turned right")
        previous_value = clk.value()   

    if button_pin.value() == False and not button_down:
        print("button pushed") 
        button_down = True
    if button_pin.value() == True and button_down:
        button_down = False

    if button_pin.value() == False:
        print("button pressed")