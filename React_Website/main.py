from website import create_app
from flask import Flask
from flask_mongoengine import MongoEngine
import pymongo
from dotenv import load_dotenv
load_dotenv()
import os
uri = os.getenv('COSMO_DB_URL')

try:
    myclient = pymongo.MongoClient(uri)
    mydb=myclient["mydbazure"]
    myclient.server_info() #triggers exception
except Exception as e:
    print("Error , cannot connect to mongodb")
    print("reason = "+str(e))

app=create_app()
db=MongoEngine()
db.init_app(app)
if __name__=="__main__":
    app.run(debug=True)











# some random code, that you can use


# from  flask import Flask
# import pymongo
# from dotenv import load_dotenv
# load_dotenv()
# import os
# app = Flask(__name__)
# uri = os.getenv('COSMO_DB_URL')
# myclient = pymongo.MongoClient(uri)
# mydb=myclient["hrdb"]
# mycol=mydb["books"]
# book={
#     "id":"120",
#     "title":"M3y book"
# }

# mycol.insert_one(book)

# for b in mycol.find():
#     print(b)
 
# # @app.route("/")
# # def index():
# #     return "Welcome to the index page."

# # @app.route("/hi")
# # def who():
# #     return "Who are you?"

