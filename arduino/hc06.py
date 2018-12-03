import serial

bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
def fire():
	while 1:
	    variable = (int)(bluetoothSerial.readline()
	    return variable
