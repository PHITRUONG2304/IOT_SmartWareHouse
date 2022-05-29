from time import sleep
import serial.tools.list_ports
import globals as g

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        splitPort = strPort.split(" ")
        commPort = (splitPort[0])
    return commPort

def readSerial():
    ser.write("GET#");
    bytesToRead = ser.inWaiting()
    while bytesToRead <= 0:
        bytesToRead = ser.inWaiting()
    mess = ser.read(bytesToRead).decode("UTF-8")
    start = mess.find("!")
    end = mess.find("#")
    g.data = mess[start:end+1]
    mess = ""

def writeSerial(message):
    ser.write(message)

if getPort() != "None":
    portName = getPort()
    ser = serial.Serial(portName, baudrate=9600)
    print("Connected with " + portName)
    print("Connect port successfully!")
    g.isComConnect = True
    