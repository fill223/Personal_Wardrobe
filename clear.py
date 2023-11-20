import pymysql


connection = pymysql.connect(host='host_ip',
                        user='username',
                        password='password',
                        database='database_name',
                        cursorclass=pymysql.cursors.DictCursor)



cursor=connection.cursor()



clearance="DELETE FROM queue"
cursor.execute(clearance)


customer="UPDATE cell set customer_id=0"
cursor.execute(customer)

customer="UPDATE cell set is_free=1"
cursor.execute(customer)

connection.commit()