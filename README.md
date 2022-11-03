# Pico-Barcode-HAT
Barcode HAT for Pico is a robust and compact barcode scanner board that consists of DE2120 scanner module, buzzer, 1.14” LCD screen, micro-USB port. It is designed to scan 20 different barcode symbologies in the segment of both 1D and 2D symbology like barcodes and QR codes

<img src= https://github.com/sbcshop/Pico-Barcode-HAT/blob/main/images/img1.jpg />

## Setup Pico Barcode Hat
* First you need to change the mode of the Pico Barcode Hat.   
  * Mode is TTL/RS232 (serial communication interface) for this you need to scan below the barcode, Connect USB to pico barcode hat.

  <img src= https://github.com/sbcshop/Pico-Barcode-HAT/blob/main/images/TTL_RS232.JPG />
  
  *  Change the baud rate to (9600) for this you need to scan the below barcode by pressing the scan button on the Pico Barcode Hat
  
  <img src= https://github.com/sbcshop/Pico-Barcode-HAT/blob/main/images/img_baud_rate_9600.JPG />
  
## For setup the Board in thonny </b>
   * Now connect USB Cable on USB Port of Pico.
   * Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />
  
   
## code part
   * In the folder you see two files one is "st7789.py" and the other is "firmware.uf2"
      * Save the "st7789.py" file in the pico (this is the LCD library file)
      * For the second file "firmware.uf2" do this, Before raspberry pico connects to the laptop, press the boot button of the pico then connect to the laptop, you see the new device named "RPI-RP2". Drag and drop the "firmware.uf2" file to the RPI-RP2.
     
   * In the folder you see a file name "Barcode_Scanner_demo.py", run this file, this is demo code. From this code, you easily understand the working of this module. using this basic code you make many applications.
   
   * One of the applications we mention in that folder, the folder name is "smart attendance system". when you open this folder you see three file
     * employee.py (the file you need to enter the employee name and the barcode of that employee (it is like a database ))
     * main.py (the file you need to run (this is the main file ))
     * servo_control.py ( this file controls the servo motor )
     
   * Save the three files in the pico, "main.py" file is automatically run when you give power to pico

### <a href="https://learn.sb-components.co.uk/Pico-Barcode-HAT" > Pico Barcode HAT Wiki Portal </a>
