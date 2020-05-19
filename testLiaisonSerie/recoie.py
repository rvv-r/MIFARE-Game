import serial

nbSerialPort = str(input("Rentrez le numéro du port série : "))
serialPort = 'COM'+nbSerialPort

ser = 0
var = True

def init_serial(numeroPort):
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM'+numeroPort
    ser.timeout = 3
    ser.open()

    if ser.isOpen():
        print('Open : ' + ser.portstr)
    

init_serial(nbSerialPort)

while var == True:
    data = str(ser.readline())
    data = data[2:-1]
    print("reçu : " + data)
    if data == "quit":
        print("connection fermé")
        var = False