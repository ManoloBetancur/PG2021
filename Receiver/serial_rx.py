#!/usr/bin/python3
import time
import serial
import datetime
import pytz
#Funcion para guardar los datos recibidos en txt
def Guardar_txt(datos):
        with open('raw_data.txt', "a") as file_object:
        #Guarda los datos de posicion en un archivo txt
                newLine = '\n'
                file_object.write(datos+newLine)
#Check if it is "Pico y placa" time
def charge_time():
        timezone = pytz.timezone('America/Bogota')
        now = datetime.datetime.now(timezone).time()
        #Pico y placa time
        #First period
        start1 = datetime.time(6, 0, 0)
        end1 = datetime.time(8, 30, 0)
        #Second period
        start2 = datetime.time(15, 0, 0)
        end2 = datetime.time(19, 30, 0)
        if (start1 <= now <= end1):
                return True
        elif (start2 <= now <= end2):
                return True
        else:
                return False

#Lectura del puerto serial
def receive_time():
        ser = serial.Serial('/dev/serial0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
        time.sleep(2)
        try:
                while True:
                        if (charge_time()):
                                print("Recibiendo...")
                                if ser.inWaiting() > 0:
                                        print('Se recibio informacion')
                                        try:
                                                data = ser.readline().decode('utf-8')
                                        except UnicodeDecodeError:
                                                print('No se pudo decodificar')
                                                data = ser.readline()
                                        print(data)
                                        Guardar_txt(data)
                        else:
                                print("Fuera de Horario, no se reciven datos")
                                time.sleep(10)
        except KeyboardInterrupt:
                print("SALIENDO ,,,\n")
        finally:
                ser.close()
                pass

if __name__=='__main__':
        receive_time()