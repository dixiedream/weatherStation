import time

from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.clear()
countdown = "{}"
for i in reversed(range(1, 6)):
    lcd.move_to(8, 0)
    lcd.putstr(countdown.format(i))
    time.sleep(1)
    lcd.clear()

lcd.move_to(1,0)
lcd.putstr("Programma...")
time.sleep(5)
lcd.clear()

lcd.move_to(1,0)
lcd.putstr("Fanahaaaaaa")
lcd.move_to(1, 1)
lcd.putstr("Nahaaaaaa")
time.sleep(5)
lcd.clear()


time.sleep(2)