import time
from machine import I2C, Pin

# PINS DEFINITIONS
LCD_SDA = 0
LCD_SCL = 1
TEMP_OUT = 4
ROTARY_SW = 18
ROTARY_DT = 17
ROTARY_CLK = 16

## LCD
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=Pin(LCD_SDA), scl=Pin(LCD_SCL), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

## Temp sensor
import dht

tSensor = dht.DHT11(Pin(TEMP_OUT))

def printTemp():
    lcd.clear()
    lcd.move_to(0, 0)
    tempMsg = "Temp: {}C"
    print(tSensor.temperature())
    lcd.putstr(tempMsg.format(tSensor.temperature()))
    lcd.move_to(0, 1)
    humMsg = "Humidity: {}%"
    print(tSensor.humidity())
    lcd.putstr(humMsg.format(tSensor.humidity()))
    
# while True:
    lcd.clear()
    # printTemp()
    # time.sleep(5)