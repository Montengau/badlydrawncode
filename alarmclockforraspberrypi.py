from gpiozero import LED
from time import sleep
from datetime import datetime, time

led = LED(16)
import time
import Adafruit_CharLCD as LCD
import sys

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

while True:
     t = datetime.now()

     hournow = str(t.hour)
     minnow = str(t.minute)
     secnow = str(t.second)


     #print(f'{hournow}:{minnow}:{secnow}')

     if len(hournow) == 1:
         hournow = hournow.zfill(2)
     if len(minnow)== 1:
         minnow = minnow.zfill(2)
     if len(secnow) == 1:
         secnow = secnow.zfill(2)

         #print(f'{hournow}:{minnow}:{secnow}')

     nowtime = (f'{hournow}:{minnow}:{secnow}')

     print(nowtime)

     alarm1hour = '09'
     alarm1minute = '20'
     alarm1second = '00'
     alarm1full = "{}:{}:{}".format(alarm1hour, alarm1minute, alarm1second)

     alarm2hour = '09'
     alarm2minute = '42'
     alarm2second = '45'
     alarm2full = "{}:{}:{}".format(alarm2hour, alarm2minute, alarm2second)

     alarm3hour = '13'
     alarm3minute = '00'
     alarm3second = '00'
     alarm3full = "{}:{}:{}".format(alarm3hour, alarm3minute, alarm3second)

     alarm4hour = '13'
     alarm4minute = '15'
     alarm4second = '45'
     alarm4full = "{}:{}:{}".format(alarm4hour, alarm4minute, alarm4second)

     alarm7hour = '15'
     alarm7minute = '30'
     alarm7second = '45'
     alarm7full = "{}:{}:{}".format(alarm7hour, alarm7minute, alarm7second)

     alarm8hour = '15'
     alarm8minute = '40'
     alarm8second = '45'
     alarm8full = "{}:{}:{}".format(alarm8hour, alarm8minute, alarm8second)

     alarm5hour = '18'
     alarm5minute = '25'
     alarm5second = '00'
     alarm5full = "{}:{}:{}".format(alarm5hour, alarm5minute, alarm5second)

     alarm6hour = '18'
     alarm6minute = '35'
     alarm6second = '45'
     alarm6full = "{}:{}:{}".format(alarm6hour, alarm6minute, alarm6second)

     alarmoffhour = '19'
     alarmoffminute = '12'
     alarmoffsecond = '00'
     alarmofffull = "{}:{}:{}".format(alarmoffhour, alarmoffminute, alarmoffsecond)

     text = "Good morning!!"
     text2 = "Go For a Walk!"
     text3 = "Stop Working!!"
     text4 = "Go For ANOTHER Walk!!"

     print(alarm1full)
     print(alarm2full)


     if nowtime > alarm1full and nowtime < alarm2full:
             led.on()
             sleep(1)
             led.off()
             sleep(1)
             lcd.message(text)

     elif nowtime > alarm3full and nowtime < alarm4full:
             led.on()
             sleep(1)
             led.off()
             sleep(1)
             lcd.message(text2)

     elif nowtime > alarm5full and nowtime < alarm6full:
             led.on()
             sleep(1)
             led.off()
             sleep(1)
             lcd.message(text3)

     elif nowtime > alarm7full and nowtime < alarm8full:
             led.on()
             sleep(1)
             led.off()
             sleep(1)
             lcd.message(text4)


     elif  nowtime == alarmofffull:
	     lcd.clear()
	     sys.exit()
     else:
         lcd_columns = 8
         lcd_rows = 1
         lcd.message(nowtime)

