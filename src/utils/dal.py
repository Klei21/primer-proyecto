import mysql.connector

class DAL:
    #constrictor - create connection - database access layer 
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",password="123456")

    def log_in(self,sql):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            logged = cursor.fetchone()
        return logged

    def get_table(self, sql):    
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            table = cursor.fetchall() 
            if table == None:
                raise FileNotFoundError("There's no parameter to return!")
            return table 

    def get_one(self, sql):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            one = cursor.fetchall()
            return one

    def new_param(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit() 
            last_row_id = cursor.lastrowid
            return last_row_id

    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count

    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count

    def log_out(self):
        self.connection.close() 
