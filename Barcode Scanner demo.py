 # Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, UART,SPI
import utime
import st7789
import vga1_bold_16x32 as font

uart = UART(0, baudrate=9600,
                    bits=8, parity=None, stop=1)

print(uart)
utime.sleep(1)
scan= b"^_^SCAN."
#scan = b'\x5E\x5F\x5E\x53\x43\x41\x4E\x2E'

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(13, Pin.OUT),
        rotation=3)
def wait_resp_info(timeout=2000):
    prvmills = utime.ticks_ms()
    info = b""
    while (utime.ticks_ms()-prvmills) < timeout:
        if uart.any():
            info = b"".join([info, uart.read(1)])
    print(info.decode())
    return info
def main():
    

    tft.init()
    utime.sleep(0.5)
   
    tft.text(font,"Barcode HAT", 0,0)
    #tft.rect(100, 100, 100, 10, st7789.RED)
    tft.fill_rect(0, 40, 240,10, st7789.RED)
    #utime.sleep(4)
    tft.text(font,"Scan Barcode", 0,0)
    #tft.rect(100, 100, 100, 10, st7789.RED)
    tft.fill_rect(0, 40, 240,10, st7789.RED)
    
    


utime.sleep(2)
main()
while 1:
  #  uart.write(scan)
    data=uart.read(14)
    
    if data:
        print(data)
        if '\r' in data:
            tft.text(font,data, 0,60)
            tft.fill_rect(0, 100, 240,10, st7789.BLUE)
             
            utime.sleep(4)
            for x in range(241):
                tft.text(font,' ', x,60)
            data ='\0'
        
           
        
        
    
