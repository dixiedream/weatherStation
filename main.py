import time
from machine import I2C, Pin

# PINS DEFINITIONS
CLOCK_SDA = 14
CLOCK_SCL = 15
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

## Clock
from ds3231_i2c import DS3231_I2C 
ds_i2c = I2C(1, sda=Pin(CLOCK_SDA), scl=Pin(CLOCK_SCL))
ds = DS3231_I2C(ds_i2c)

# current_time = b'\x00\x06\x11\x01\x01\x03\x22' # sec min hour week day mon year
# ds.set_time(current_time)

def printTemp():
    tSensor.measure()
    lcd.clear()
    lcd.move_to(0, 0)
    tempMsg = "Temp: {}C"
    lcd.putstr(tempMsg.format(tSensor.temperature()))
    lcd.move_to(0, 1)
    humMsg = "Humidity: {}%"
    lcd.putstr(humMsg.format(tSensor.humidity()))

def printTime():
    t = ds.read_time()
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Date: %02x/%02x/20%x" %(t[4],t[5],t[6]))
    lcd.move_to(0, 1)
    lcd.putstr("Time: %02x:%02x" %(t[2],t[1]))
    
while True:
    printTemp()
    time.sleep(5)
    printTime()
    time.sleep(5)