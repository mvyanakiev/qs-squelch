from serial.tools import list_ports

correctPort = None

ports = list(list_ports.comports())
i = 0
for p in ports:

    if p.description == 'USB2.0-Serial':
        correctPort = p.device
    print('Port ' + str(i) + ' from total ' + str(len(ports)) + ' is ' + p.device)
    i += 1

print('Serial port is: ' + correctPort)
