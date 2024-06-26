import libuvk5
from serial.tools import list_ports

serial_port = None
all_ports = list(list_ports.comports())

for port in all_ports:
    if port.description == 'USB2.0-Serial':
        serial_port = port.device

# Connect and read
with libuvk5.uvk5(serial_port) as radio:
    if radio.connect():
        _ = radio.get_fw_version()

        # mandatory before reading mem
        # print radio.get_cfg_mem(0x1e00,10).hex() but in comma separated hex digits
        # for i in range(12):
        #     print(str(0x1e00+i*0x10) + ": ", end='')
        #     temp = radio.get_cfg_mem(0x1e00+i*0x10,10).hex()
        #     temp = ','.join([f'0x{temp[i:i+2]}' for i in range(0,len(temp),2)])
        #     print(temp)
        # sys.exit(0)

        print("UHF Squelch Open RSSI Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e00 + i, 1).hex(), 16) / 2 - 160))
        print("UHF Squelch Close RSSI Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e10 + i, 1).hex(), 16) / 2 - 160))
        print("UHF Squelch Open Noise Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e20 + i, 1).hex(), 16)))
        print("UHF Squelch Close Noise Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e30 + i, 1).hex(), 16)))
        print("UHF Squelch Close Glitch Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e40 + i, 1).hex(), 16)))
        print("UHF Squelch Open Glitch Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e50 + i, 1).hex(), 16)))
        print("VHF Squelch Open RSSI Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e60 + i, 1).hex(), 16) / 2 - 160))
        print("VHF Squelch Close RSSI Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e70 + i, 1).hex(), 16) / 2 - 160))
        print("VHF Squelch Open Noise Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e80 + i, 1).hex(), 16)))
        print("VHF Squelch Close Noise Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1e90 + i, 1).hex(), 16)))
        print("VHF Squelch Close Glitch Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1ea0 + i, 1).hex(), 16)))
        print("VHF Squelch Open Glitch Thresholds:")
        for i in range(10):
            print("SQL " + str(i) + ": " + str(int(radio.get_cfg_mem(0x1eb0 + i, 1).hex(), 16)))
