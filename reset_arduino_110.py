# -- coding: utf-8 --
import RPi.GPIO as GPIO
import time
pin=7
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=0)
print("Reley is On!")
time.sleep(1)                           # Пауза 1 секунда
GPIO.setup(pin, GPIO.OUT, initial=1)
GPIO.cleanup()                          # Возвращаем пины в исходное состояние
print("Reley is Off!")
