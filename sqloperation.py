import mysql.connector as connection
from custom_logger import Custom_logger

class MysqlOperation:
    log = Custom_logger.log('mysql.log')

    def __init__(self,host,user,passwd):

        '''
        Initializing with Variable
        '''
        try:
            self.host = host
            self.user = user
            self.passwd = passwd
            self.conn = self.establish_db_connection()
            self.cursor = self.conn.cursor()
            self.log.info(f"Initialized all the variables : {host} , {user} , {passwd}")
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def establish_db_connection(self):

        '''
        Creating mysql databases connection
        '''
        try:
            self.log.info("Creating mysql database connection")
            mydb = connection.connect(host=self.host, user = self.user , passwd = self.passwd)
            return mydb
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def create_databases(self,db):
        '''
        Creating database
        '''
        try:
            query = "create database {}".format(db)
            self.cursor.execute(query)
            self.log.info(f"Executed Query : {query}")
            self.log.info(f"Database : {db} created successfully")
            return f"Database : {db} created"
        except Exception as e:
            self.log.info(str(e))
            print(e)

    def use_database(self,db):
        '''
        Use database
        '''
        try:
            query = "use {}".format(db)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            self.log.info((f"Database : {db} in use"))
            return f"Databse : {db} in use"
        except Exception as e:
            self.log.info(str(e))
            print(e)


    def select_data_table(self,tabl):
        '''
        Select data form table
        '''
        try:
            query = "select * from {}".format(tabl)
            self.cursor.execute(query)
            self.log.info(f"Executed Query : {query}")
            res = self.cursor.fetchall()
            self.log.info(f"Returning data form the table: {tabl}")
            return res
        except Exception as e:
            self.log.exception(str(e))
            print(e)


