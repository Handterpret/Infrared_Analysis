import serial
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument("--serial", default="COM7", help="Serial port to connect to for instance COM3 on windows or /dev/ttyUSB0 on Linux")
parser.add_argument("-b", "--baud", help="Baud rate for reading serial port", default="9600")
parser.add_argument("-o", "--output", help="Where to save output data", default=".")

args = parser.parse_args()

def GetIRData(serialport, baud):
    num = 0
    ser = serial.Serial(serialport, baud)
    t_end = time.time() + 1 # run for 1 sec
    while time.time() < t_end:
        bytesToRead = ser.inWaiting()
        data = ser.readline(bytesToRead)
        print(data)
        num+=1
    print(num)

if __name__ == "__main__":
    GetIRData(args.serial, args.baud)