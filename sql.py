import pymysql

def sql_check(rasp_id):

    connection = pymysql.connect(host='host_ip',
                            user='username',
                            password='password',
                            database='database_name',
                            cursorclass=pymysql.cursors.DictCursor)

    for i in range(1):
        cursor=connection.cursor()

        rasp_id=1
        sql="SELECT cell_id FROM cell where customer_id= NULL & rasp_id= %s (rasp_id) order by cell_id"

        cursor.execute(sql, rasp_id)


    connection.commit()
    connection.close()