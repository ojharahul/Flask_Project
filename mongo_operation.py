import pymongo
from custom_logger import Custom_logger

class MyMongo:
    log = Custom_logger.log('mongo.log')

    def __init__(self,db_name, coll_name):

        '''
        This will initialize the connection
        '''
        try:
            self.client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.10qztuf.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.create_database(db_name)
            self.coll = self.create_collection(coll_name)
            self.log.info("Connection created with mongo db atlas")
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def show_databases(self):
        '''
        This method will show all the databases present
        '''
        try:
            self.log.info("Listing all the database ")
            db_list = self.client.list_database_names()
            self.log.info(f"Databases available are : {db_list}")
            return db_list
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def create_database(self,db_name):
        '''
        This method will create database
        '''
        try:
            self.log.info(f"Creating database : {db_name}")
            db = self.client[db_name]
            return db
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def create_collection(self,coll_name):
        '''
        This method will create collection
        '''
        try:
            self.log.info(f"Creating collection : {coll_name}")
            collection = self.db[coll_name]
            return collection
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def select_all_docs(self,query=None):
        '''
        This method will select & return all document from the collection
        '''
        try:
            self.log.info(f"selecting all the document form the collection: {self.coll} ")
            data_list = []
            if query:
                if isinstance(query, dict):
                    data_list = [i for i in self.coll.find(query)]
                else:
                    self.log.error("Raising exception since dictionary query is not passed in select_all_docs")
                    raise Exception(f"You have not entered a dictionary query: {query} in select_all_docs")
            else:
                data_list = [i for i in self.coll.find()]
            if data_list:
                return data_list
            else:
                return f"No document found with query: {query}"
        except Exception as e:
            self.log.exception(str(e))
            print(e)
