import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))

while True:
    print("Measure", d.measure(), "Temp", d.temperature(), "Hum", d.humidity())
    time.sleep(5)