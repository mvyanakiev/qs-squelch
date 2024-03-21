from serial.tools import list_ports

correct_port = 'Not found'

ports = list(list_ports.comports())
i = 1
for p in ports:

    if p.description == 'USB2.0-Serial':
        correct_port = p.device
    print('Port ' + str(i) + ' from total ' + str(len(ports)) + ' is ' + p.device)
    i += 1

print('Serial port is: ' + correct_port)
