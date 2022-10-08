import serial.tools.list_ports
import statistics as ss

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist = []
dict={'Temperature':[],'Soil Moisture(in Percentage) ':[]}

for onePort in ports:
    portlist.append(str(onePort))
    print(str(onePort))

val = input("Select port COM")

for x in range(0,len(portlist)):
    if portlist[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portlist[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

m=2
n=3

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        x=packet.decode('utf')
        data_list = x.split('\033')
        # print(data_list)
        for v in data_list:
            # print(v)
            if 'Temperature' in v:
                a = v.split("=")
                # print(a[1])
                if m>=0:
                    dict['Temperature'].append(float(a[1]))
                    m=m-1
                else:
                    break
            elif 'Soil Moisture(in Percentage) ' in v:
                b = v.split("=")
                # print(b[1])
                if n>=0:
                    dict['Soil Moisture(in Percentage) '].append(float(b[1]))
                    n=n-1
                else:
                    break

        
        if m<0 and n<0:
            break

    
dats = []
var1 = ss.mean(dict['Temperature'])
var2 = ss.mean(dict['Soil Moisture(in Percentage) '])
dats.append(var1)
dats.append(var2)
