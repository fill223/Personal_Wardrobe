import serial
import pymysql
import datetime

def sql_check(data):

    connection = pymysql.connect(host='host_ip',
                        user='username',
                        password='password',
                        database='database_name',
                        cursorclass=pymysql.cursors.DictCursor)

    for i in range(1):
        today=datetime.datetime.today()
        dt_now=today.strftime("%Y/%m/%d %H:%M:%S")     

        cursor=connection.cursor()

        sql="INSERT INTO queue (card_data,is_in_work,log_date) VALUES (%s, '0', %s)"

        cursor.execute(sql,(str(data),str(dt_now)))


    connection.commit()
    connection.close()



serialPort = serial.Serial('/dev/ttyUSB0', 9600)


for i in range(10):
    card_data=0
    card_data=serialPort.readline()
    if card_data!=0:
        sql_check(card_data)
    i=1








# # import logging
# # import time



# def usb_read():
#     serialPort = serial.Serial(
#         # port="ttyUSB0", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
#         '/dev/ttyUSB0', 9600
#     )

#     while True:
#         data=serialPort.readline()
            

            
#1


# from serial.serialutil import SerialException
# class CardReader():
#     def __init__(self, usb_device):
#         self.usb_device = usb_device
#         self.connected = False
#         self.device = None

#     def device_path(self):
#         return self.usb_device

#     def connect(self):
#         try:
#             self.device = serial.Serial(self.usb_device)
#         except SerialException as e:
#             logging.error('Could not open port {}! Raw error:\n{}'.format(self.usb_device, e))
#         except Exception as e:
#             logging.error('Error while connecting! Text:\n{}'.format(e))
#         else:
#             logging.info('Successfully connected to {}!'.format(self.usb_device))
#             self.connected = True



#2
# with open('/dev/ttyUSB0','r', 'b') as с:
#     data = с.read()

# print(data)


#3
# import time

# i=100

# while i>0:
#     f=open('/dev/ttyUSB0', 'r+') #Reading data from Cardreader
#     data=f.read() #Записали данные в переменную data
#     print(data)
#     f.close() #MUST HAVE!!!!
    

#4
# serialString = ""  # Used to hold data coming over UART
# while 1:
#     # Wait until there is data waiting in the serial buffer
#     if serialPort.in_waiting > 0:

#         # Read data out of the buffer until a carraige return / new line is found
#         serialString = serialPort.readline()

#         # Print the contents of the serial data
#         try:
#             print(serialString)
#         except:
#             print('Some error')

