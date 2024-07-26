import serial 
import datetime
import time

if __name__=='__main__':
    start_time = time.time()
    actual_time_str = datetime.datetime.utcnow().strftime('%d_%m_%Y_%H_%M')
    serial_obj = serial.Serial('/dev/ttyUSB0',baudrate=115200)
    with open(actual_time_str+'.csv','wb') as f:
        f.write(b' ')

    while True:
        with open(actual_time_str+'RESULTADOS.csv','a') as f:
            data = serial_obj.readline()
            print(data)
            f.write(f'{data.decode("UTF-8").strip()},{time.time()-start_time}\n')
