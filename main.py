from flask import Flask , request , jsonify
from sqloperation import MysqlOperation
from mongo_operation import MyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/mysql1/getdata', methods = ['GET','POST'])
def get_mysql_data():
    if (request.method == 'POST'):
        db = request.json['database']
        table = request.json['table']
        conn_1 = MysqlOperation('localhost','root','pooja@2312')
        conn_1.use_database(db)
        result = conn_1.select_data_table(table)
        return jsonify(str(result))

@app.route('/mongodb1/getdata',methods = ['GET','POST'])
def get_mongodb_data():
    if (request.method == 'POST'):
        db = request.json['database']
        coll = request.json['collection']
        conn_2 = MyMongo(db,coll)
        result = conn_2.select_all_docs()
        return jsonify(str(result))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""    
''DB = 'Rahul'
collection = 'ineuron'

DB = 'pooja'
Table = 'glassdata'
"""