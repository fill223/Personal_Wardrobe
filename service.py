import pymysql
from gpio_contrlol import cell_open
from client import client
import time
import paramiko

connection = pymysql.connect(host='host_ip',
                        user='username',
                        password='password',
                        database='database_name',
                        cursorclass=pymysql.cursors.DictCursor)



tik_host = 'mikrotik_ip
tik_port = 22
tik_username = 'mikrotik_username'
tik_password = 'mikrotik_password'

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure, see note below)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the MikroTik device
ssh.connect(tik_host, tik_port, tik_username, tik_password)

# Execute your command
command = 'system routerboard usb power-reset duration=4s'



while True:

    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(5)
    data=None
    occupancy=None

    cursor=connection.cursor()

    #Checking queue
    sql="SELECT card_data FROM queue WHERE is_in_work=0"
    cursor.execute(sql)
    data=str(cursor.fetchone())
    data=data.strip("{'card_data': '}")


    #Checking card_data=cell occupancy
    if data != "None":

        #Updating is_in_work
        in_work="UPDATE queue SET is_in_work=1 WHERE is_in_work=0"
        cursor.execute(in_work)


        #Checking this client occupancy
        occupancy="SELECT cell_id FROM cell WHERE customer_id=(%s)"
        cursor.execute(occupancy,(data))
        occupancy=str(cursor.fetchone())
        occupancy=occupancy.strip("{'cell_id':'}") 
        #Found cell_id of occupanced cell

        print("Occupancyed's cell id = "+occupancy)

        if occupancy=="Non": #if its not occupyied
            #Choosing cell
            choise="SELECT cell_id FROM cell WHERE is_free=1 ORDER BY cell_id" #Choisen cell
            cursor.execute(choise)
            choise=str(cursor.fetchone())
            choise=choise.strip("{'cell_id':'}") #Choise = cell_id
            
            print("Choisen's cell_id = " + choise)

            #Finding out choosen cell ipaddr
            ipaddr="SELECT rasp_id FROM cell WHERE is_free=1 ORDER BY cell_id"
            cursor.execute(ipaddr)
            ipaddr=str(cursor.fetchone())
            ipaddr=ipaddr.strip("{'rasp_id':'}") #ipaddr = rasp_id
            ipaddr=ipaddr.strip()
            print("Ipaddr = " + ipaddr)

            #Finding out choosen cell's gpio_pin
            gpio_pin="SELECT gpio_pin FROM cell WHERE is_free=1 ORDER BY cell_id"
            cursor.execute(gpio_pin)
            gpio_pin=str(cursor.fetchone())
            gpio_pin=gpio_pin.strip("{'gpio_pin':'}") 


            if ipaddr=="10":
                cell_open(gpio_pin,5)
            else: 
                client(gpio_pin,ipaddr) #Send call on rasp to open cell

            reserv="UPDATE cell SET customer_id=(%s) WHERE cell_id=(%s)"
            cursor.execute(reserv,(data, choise))
            
            free="UPDATE cell SET is_free=0 WHERE cell_id=(%s)"
            cursor.execute(free,( choise))

        else:

            #Finding out occypied cell's ipaddr
            ipaddr="SELECT rasp_id FROM cell WHERE customer_id=(%s)"
            cursor.execute(ipaddr,(data))
            ipaddr=str(cursor.fetchone())
            ipaddr=ipaddr.strip("{'rasp_id':'}") #ipaddr = rasp_id
            ipaddr=ipaddr.strip()
            print("Ipaddr = " + ipaddr)

            #Finding out choosen cell's gpio_pin
            gpio_pin="SELECT gpio_pin FROM cell WHERE customer_id=(%s)"
            cursor.execute(gpio_pin,(data))
            gpio_pin=str(cursor.fetchone())
            gpio_pin=gpio_pin.strip("{'gpio_pin':'}") 

            if ipaddr=="10":
                cell_open(gpio_pin,5)
            else:  
                client(gpio_pin,ipaddr) #Send call on rasp to open cell
    connection.commit()
    
    



            





    
    


    #Working with DB 
    # sql="UPDATE cell \
    # SET customer_id=0 \
    # ORDER BY cell_id "
    # cursor.execute(sql)

    # sql="UPDATE cell \
    # SET customer_id=(%s)\
    # WHERE is_free=1 \
    # ORDER BY cell_id"
    # cursor.execute(sql,(data))





# connection.commit()
# connection.close()



# def sql_check(data):

#     connection = pymysql.connect(host='172.16.1.10',
#                                 user='root',
#                                 password='njhufib',
#                                 database='new_shkaf',
#                                 cursorclass=pymysql.cursors.DictCursor)

#     for i in range(1):
#         today=datetime.datetime.today()
#         dt_now=today.strftime("%Y/%m/%d %H:%M:%S")     

#         cursor=connection.cursor()

#         sql="INSERT INTO queue (card_data,is_in_work,log_date) VALUES (%s, '0', %s)"

#         cursor.execute(sql,(str(data),str(dt_now)))


#     connection.commit()
#     connection.close()