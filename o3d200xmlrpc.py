import socket
import struct
import time
import xmlrpc.client
import matplotlib.pyplot as plt
import numpy as np
import select
from matplotlib import cm

server_host = "192.168.0.69"
server_port = 8080
server_port_socket=50002
proxy = xmlrpc.client.ServerProxy(f"http://{server_host}:{server_port}")
time.sleep(1)
methods = proxy.system.listMethods()
print("\nMethods:\n", methods, "\n")
Conectare = proxy.MDAXMLConnectCP(server_host, server_port)
time.sleep(1)
if Conectare == [0, '4041', 'O3D200AD']:
    print('M-AM CONECTAT LA SERVER')
elif Conectare == [-120]:
    print("Sunt deja conectat la server")
workingmode=proxy.MDAXMLSetWorkingMode(1)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port_socket))                    #conectare la server-ul TCP/IP

#
ready = select.select([client_socket], [], [],  1)
print('Ready: ',ready)
time.sleep(5)


TOTAL_DATA=39528

command='xyz'

client_socket.send(command.encode())                    #comanda trimisa catre server.
time.sleep(0.1)
DATE_PRIMITE=b''
try:
    print("Am intrat in blocul try")
    while len(DATE_PRIMITE)<TOTAL_DATA:
        print("Am intrat in bucla while")
        data=client_socket.recv(1460)
        print('Lungimea datelor:',len(data))
        print('DATA IN HEX : ',data.hex())
        if not data:
            break
        DATE_PRIMITE = DATE_PRIMITE + data
except IOError as e:
    print('Complicata situatie')
    pass
DATE_PRIMITE_HEX=DATE_PRIMITE.hex()
print('TOTAL DATA BYTES: ',DATE_PRIMITE)
print('DATE_PRIMITE_HEX',DATE_PRIMITE_HEX)


HEADER_BYTES = DATE_PRIMITE[:376]#
print("PRIMUL HEADER: ",len(HEADER_BYTES))

DATA_BYTES = DATE_PRIMITE[376:13176]
print("DATA BYTES 0: ",len(DATA_BYTES))

HEADER_BYTES1=DATE_PRIMITE[13176:13552]
print("AL DOILEA HEADER: ",len(HEADER_BYTES1))

DATA_BYTES1=DATE_PRIMITE[13552:26352]
print("DATA BYTES 1: ",len(DATA_BYTES1))

HEADER_BYTES2=DATE_PRIMITE[26352:26728]
print("AL TREILEA HEADER: ",len(HEADER_BYTES2))

DATA_BYTES2=DATE_PRIMITE[26728:]
print("DATA BYTES 2 : ",len(DATA_BYTES2))

#FOR PENTRU IMPARTIREA OCTETILOR
# HEADER_LISTA=[]
# DATA_LISTA=[]
# C=376
# for i in range(3):
#     # HEADER_LISTA.append(DATE_PRIMITE[C:C+376])
#     # C=C+376
#     DATA_LISTA.append(DATE_PRIMITE[C:C+12800])
#     C=C+13176


#PRIMUL HEADER FLOAT SI DATA
HEADER_FLOAT=[]
#CONVERSIE IN FLOAT PENTRU HEADER
for i in range(0, len(HEADER_BYTES), 4):
    grup = HEADER_BYTES[i:i+4]
    valoare = struct.unpack('!f', grup)[0]
    HEADER_FLOAT.append(valoare)
print("HEADER FLOAT 0: ", HEADER_FLOAT)

DATA_FLOAT=[]
#CONVERSIE IN FLOAT PENTRU DATA
#DATA_LISTA[0]
for i in range(0, len(DATA_BYTES), 4):
    grup = DATA_BYTES[i:i+4]
    valoare = struct.unpack('!f', grup)[0]
    DATA_FLOAT.append(valoare)
print("DATA FLOAT 0: ", DATA_FLOAT)

#AL DOILEA HEADER FLOAT SI DATA

HEADER_FLOAT1=[]
#CONVERSIE IN FLOAT PENTRU HEADER
for i in range(0, len(HEADER_BYTES1), 4):
    grup = HEADER_BYTES1[i:i+4]
    valoare = struct.unpack('!f', grup)[0]
    HEADER_FLOAT1.append(valoare)
print("HEADER FLOAT 1: ", HEADER_FLOAT1)

DATA_FLOAT1=[]
#CONVERSIE IN FLOAT PENTRU DATA
#DATA_LISTA[1]
for i in range(0, len(DATA_BYTES1), 4):
    grup = DATA_BYTES1[i:i+4]
    valoare = struct.unpack('!f', grup)[0]
    DATA_FLOAT1.append(valoare)
print("DATA FLOAT 1: ", DATA_FLOAT1)

#AL TREILEA HEDER FLOAT SI DATA
HEADER_FLOAT2=[]
#CONVERSIE IN FLOAT PENTRU HEADER
for i in range(0, len(HEADER_BYTES2), 4):
    grup = HEADER_BYTES2[i:i+4]
    valoare = struct.unpack('!f', grup)[0]
    HEADER_FLOAT2.append(valoare)
print("HEADER FLOAT 2: ", HEADER_FLOAT2)

DATA_FLOAT2=[]
#CONVERSIE IN FLOAT PENTRU DATA
#DATA_LISTA[2]
for i in range(0, len(DATA_BYTES2), 4):
    grup = DATA_BYTES2[i:i+4]
    valoare = struct.unpack('!f', grup)[0]
    DATA_FLOAT2.append(valoare)
print("DATA FLOAT 2: ", DATA_FLOAT2)



#MATRICE CU NUMPY!

# PRIMA MATRICE X

print(('Lungimea datelor pentru prima matrice :' ,len(DATA_FLOAT)))
MATRICE1X=np.array(DATA_FLOAT)
MATRICE2X=MATRICE1X.reshape(50,64)
MATRICE3X=MATRICE2X.transpose()
print("A TREIA MATRICCE X: ",MATRICE3X)

# #A DOUA MATRICE Y
print(('Lungimea datelor pentru a doua matrice :' ,len(DATA_FLOAT1)))
MATRICE1Y=np.array(DATA_FLOAT1)#
MATRICE2Y=MATRICE1Y.reshape(50,64)
MATRICE3Y=MATRICE2Y.transpose()
print("A DOUA MATRICE Y:",MATRICE3Y)

#
# #A TREIA MATRICE Z
print(('Lungimea datelor pentru a treia  matrice :' ,len(DATA_FLOAT2)))
MATRICE1Z=np.array(DATA_FLOAT2)
MATRICE2Z=MATRICE1Z.reshape(50,64)
MATRICE3Z=MATRICE2Z.transpose()
print("A TREIA MATRICE Z: ",MATRICE3Z)

#PENTRU 3D
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(MATRICE3X, MATRICE3Y, MATRICE3Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.colorbar(surf)
plt.show(block=True)

# PENTRU 2D
plt.imshow(MATRICE3X, cmap='viridis')
plt.colorbar()
plt.show(block=True)
plt.imshow(MATRICE3Y, cmap='viridis')
plt.colorbar()
plt.show(block=True)
plt.imshow(MATRICE3Z, cmap='viridis')
plt.colorbar()
plt.show(block=True)


# command='d'
# client_socket.send(command.encode())
# # client_socket.setblocking(0)
# #
# ready = select.select([client_socket], [], [],  1)
# print('Ready: ',ready)
# if ready[0]:
#      data = client_socket.recv(4096)
# #     print('cvd',data)

# print('socket')
# # command ='i'
# # client_socket.send(command.encode())
# # # client_socket.shutdown(socket.SHUT_WR)
# # response = client_socket.recv(1024).decode()
# # print(response)
# # Help1 = proxy.system.methodHelp('GetDisplayStatus')
# # print(type(Help1))
# # print(Help1)
# # result = proxy.MDAXMLGetSWVersion()
# # print(result)
# # Help2 = proxy.system.methodHelp('MDAXMLGetSWVersion')
# # print(Help2)
# # ceva=proxy.DisconnectMenue()
# Conectare = proxy.MDAXMLConnectCP(server_host, server_port)
# if Conectare == [0, '4041', 'O3D200AD']:
#     print('M-AM CONECTAT LA SERVER')
# elif Conectare == [-120]:
#     print("Sunt deja conectat la server")
# # result=proxy.MDAXMLGetSoftwareVersion()#4041
# # print(result)
# # tcpip=proxy.MDAXMLGetXmlPortCP()##port 8080
# # print(tcpip)MDAXMLSensorReset
# # temperature=proxy.MDAXMLGetTemperatures()
# # print(temperature)
# # workingmode=proxy.MDAXMLGetWorkingMode()
# # print(workingmode)
# # setworking=proxy.MDAXMLSetWorkingMode()
# # print(setworking)
# # meniu=proxy.ConnectMenue()
# # print(meniu)
# # mac=proxy.MDAXMLGetMacAddress()
# # print(mac)
# # status=proxy.GetDisplayStatus()
# # print(status)
# # filterstatus=proxy.MDAXMLGetAdaptiveMeanValueFilterStatus()
# # print(filterstatus)
# # exponentialfilterstatus=proxy.MDAXMLGetExponentialFilterStatus()
# # print(exponentialfilterstatus)
# # exponentialfiltervalue=proxy.MDAXMLGetExponentialFilterValue()
# # print(exponentialfiltervalue)
# # triggerimage=proxy.MDAXMLTriggerImage()
# # print(triggerimage)
# # unlocksensor=proxy.MDAXMLUnlockSensor()
# # print(unlocksensor)
# # multicall = xmlrpc.client.MultiCall(proxy)
# # # print(multicall)
# # Deconectare = proxy.MDAXMLDisconnectCP(server_host, server_port)
# # if Deconectare == [0]:
# #     print('M-AM DECONECTAT DE LA SERVER')
#
# # command='V?'
# # result=proxy.send_command(command)
# # print(result)
#


