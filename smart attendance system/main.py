
# attendence system using raspberry pi pico and pico barcode hat and security system using barcode
from machine import Pin, UART,SPI
import time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font
import employee
import servo_control

# this create the data.txt file inside the raspberry pi pico
file=open('data.txt',"a+")
file.write("Today Present Student are :")
file.write("\r")
file.close()

uart = UART(0, baudrate=9600,bits=8, parity=None, stop=1)# UART interface for barcode scanner 

print(uart)
time.sleep(1)

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=3)#SPI interface for tft screen

def main():
    tft.init()
    time.sleep(0.5)#time delay
   
    tft.text(font,"Barcode HAT", 0,0)# print on tft screen
    tft.fill_rect(0, 40, 240,10, st7789.RED)#display red line on tft screen
    time.sleep(2)
    tft.text(font,"Scan barcode --", 0,0)
    tft.fill_rect(0, 40, 240,10, st7789.RED)
    
    
time.sleep(1)
main()
while 1:
  #  uart.write(scan)# uncomment this line and 19 line for continously scan 
    data=uart.read(15)#read data from barcode via uart
    
    if data:
        if '\r' in data:
            dec_1 = data.decode("utf-8")#  convert data to string
            dec = dec_1.replace('\r', '')# replace this \r by ' ' 
            print(dec)
            
            tft.fill_rect(0, 100, 240,10, st7789.BLUE)
            feedback = employee.search(dec)# call the search from employee file
            if feedback == False:
                print("unauthorised access")
                tft.text(font,"unauthorised", 0,60)
                servo_control.off_servo()#call the off_servo from motor_barcode file
            else:
                print("successful enter")
                tft.text(font,feedback, 0,60)
                servo_control.on_servo()#call the on_servo from motor_barcode file
                time.sleep(2)
                servo_control.off_servo()
                print(dec)
            time.sleep(2)
            tft.text(font,'                 ', 0,60)#remove the text from the display after 2 sec
        
