import mysql.connector


class DbConnector:
    def __init__(self, port, host, user, password, database):
        self.port = port
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(port=port, host=host, user=user, password=password, database=database)

    def get_last_registered_user(self, parameter):
        parameter_dict = {'email': 'c.email', 'password': 'c.password'}
        cursor = self.connection.cursor()
        sql = f'SELECT {parameter_dict[parameter]} FROM `oc_customer` c order by c.date_added desc limit 1'
        try:
            cursor.execute(sql)
            for row in cursor.fetchall():
                result = row[0]
                return result
        finally:
            cursor.close()

    def destroy(self):
        cursor = self.connection.cursor()
        cursor.close()

    def get_last_product_name(self):
        cursor = self.connection.cursor()
        sql = f'SELECT pd.name FROM `oc_product_description` pd order by pd.product_id desc limit 1;'
        try:
            cursor.execute(sql)
            for row in cursor.fetchall():
                result = row[0]
            return result
        finally:
            cursor.close()
