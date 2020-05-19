import serial

nbSerialPort = str(input("Rentrez le numéro du port série : "))

ser = 0
var = True

def init_serial(numeroPort):
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM'+numeroPort
    ser.timeout = 10
    ser.open()

    if ser.isOpen():
        print('Open : ' + ser.portstr)

init_serial(nbSerialPort)

while var == True :
    line = str(input("Envoyer : "))
    lineb = str.encode(line)
    ser.write(lineb)
    if line == "quit":
        print("connection fermé")
        var = False