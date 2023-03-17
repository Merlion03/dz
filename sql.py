import pymysql.cursors


class MyDb:
    def __init__(self, config):
        self.config = config
        self.connection = pymysql.connect(**self.config, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self.table_users = 'users'
        self.table_customers = 'customers'
        self.table_orders = 'orders'
        self.raw_2_customers = 'customer_fio'
        self.raw_3_customers = 'customer_telephone'
        self.raw_4_customers = 'customer_email'
        self.raw_5_customers = 'customer_login'
        self.raw_2_orders = 'order_customer'
        self.raw_3_orders = 'order_data'
        self.raw_4_orders = 'order_price'
        self.raw_5_orders = 'order_service'
        self.raw_1 = 'id'
        self.raw_2 = 'user_login'
        self.raw_3 = 'user_password'
        self.raw_4 = 'user_fio'
        self.raw_5 = 'user_role'

    def add(self, login, telephone, email, FIO):
        if self.connection:
            if not self.validator(login, 2):
                sql = f"INSERT INTO {self.table_customers} ({self.raw_2_customers}, {self.raw_3_customers}, {self.raw_4_customers}, {self.raw_5_customers}) VALUES (%s, %s, %s, %s)"
                self.cursor.execute(sql, (FIO, telephone, email, login))
                self.connection.commit()
                print('True')
                return True
            else:
                print('False')
                return False
        else:
            print("SQL IS OFF")

    def validator(self, login, var):
        if var == 1:
            sql = f"SELECT {self.raw_1} FROM {self.table_users} WHERE {self.raw_2} = %s "
            self.cursor.execute(sql, (login,))
            result = self.cursor.fetchone()
            if result is None:
                return True
            else:
                return False
        if var == 2:
            sql = f"SELECT {self.raw_5_customers} FROM {self.table_customers} WHERE {self.raw_5_customers} = %s "
            self.cursor.execute(sql, (login,))
            result = self.cursor.fetchone()
            if result is None:
                return False
            else:
                return True
        else:
            pass

    def login(self, login, password):
        if not self.validator(login, 1):
            sql = f"SELECT {self.raw_2}, {self.raw_3}, {self.raw_5} FROM {self.table_users} WHERE {self.raw_2} = %s "
            self.cursor.execute(sql, (login,))
            result = self.cursor.fetchone()
            print(result['user_password'])
            if password == result['user_password']:
                return True, result[self.raw_5]
            else:
                return False
        else:
            return False

    def check_table(self):
        if self.connection:
            sql = f'SELECT * FROM {self.table_customers}'
            self.cursor.execute(sql)
            return self.cursor.fetchall()

    def delete(self, login):
        if not self.validator(login, 1):
            sql = f'DELETE FROM {self.table_users} WHERE {self.raw_2} = %s'
            self.cursor.execute(sql, login)
            self.connection.commit()
            return True
        else:
            return False

    def form_order(self, login, price):
        if self.validator(login, 2):
            sql = f"INSERT INTO {self.table_orders} ({self.raw_2_orders}, {self.raw_3_orders}, {self.raw_4_orders}, {self.raw_5_orders}) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (login, '2003-12-31', price, '83Hits'))
            self.connection.commit()
            return True
        else:
            return False


