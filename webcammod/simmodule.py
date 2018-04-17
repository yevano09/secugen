#simmod
import serial
import os, time

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
cmd = "AT"

port.write(cmd.encode('utf-8')+b'\r')

rcv = port.read(10)
print(" Sent " + cmd )
print( rcv )
