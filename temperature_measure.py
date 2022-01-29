
import time

from gpiozero import CPUTemperature as CT

cpu = CT()

while True:
    print(cpu.temperature)
    time.sleep(5)

