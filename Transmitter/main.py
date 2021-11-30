import utime, time
from machine import UART
from machine import Pin
import ds1302
from micropyGPS import MicropyGPS



ds = ds1302.DS1302(Pin(9),Pin(18),Pin(19))
lora = UART(0,9600)
##########################################################
#GPS Module UART Connection
gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
##########################################################


##########################################################
TIMEZONE = 5
my_gps = MicropyGPS(TIMEZONE)
##########################################################
##########################################################
def convert(parts):
    if (parts[0] == 0):
        return None
        
    data = parts[0]+(parts[1]/60.0)
    # parts[2] contain 'E' or 'W' or 'N' or 'S'
    if (parts[2] == 'S'):
        data = -data
    if (parts[2] == 'W'):
        data = -data

    data = '{0:.6f}'.format(data) # to 6 decimal places
    return str(data)

def charge_time():
    pass

##########################################################


##########################################################
if __name__ == '__name__':
    while True:
        length = gps_module.any()
        if length>0:
            b = gps_module.read(length)
            for x in b:
                msg = my_gps.update(chr(x))
        #_________________________________________________
        latitude = convert(my_gps.latitude)
        longitude = convert(my_gps.longitude)
        
        hora = ds.hour()
        second = ds.second()
        minutes = ds.minute()
        hora_actual=f'{hora}:{minutes:02}:{second:02}'
        msg = f"{latitude},{longitude},MHX501,{hora_actual}"
        lora.write(msg)
        utime.sleep(10)
    