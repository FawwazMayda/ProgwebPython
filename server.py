from flask import Flask,request,jsonify
import pymongo
import json
from flask_cors import CORS
client = pymongo.MongoClient("mongodb://m001-student:abangbola@sandbox-shard-00-00-wtclz.mongodb.net:27017,sandbox-shard-00-01-wtclz.mongodb.net:27017,sandbox-shard-00-02-wtclz.mongodb.net:27017/test?ssl=true&replicaSet=Sandbox-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['vie']
collections = db['education']

app = Flask(__name__)
CORS(app)
@app.route("/api",methods=["GET"])
def apiInfo():
    msg = "berikut adalah contoh endpoint yang tersedia [GET]/api/<year> [GET]/api/<year>/<kota> dan [POST]/api"
    return jsonify(msg)
@app.route("/api",methods=["POST"])
def apiPost():
    req = request.get_json()
    doc_id = collections.insert_one(req).inserted_id
    return jsonify(msg="Inserted with _id:{doc_id}".format(doc_id=doc_id))

@app.route("/api/<year>",methods=['GET'])
def api(year):
    print(year)
    res = collections.find({"tahun":int(year)})
    doc = []
    for x in res:
        x.pop('_id')
        doc.append(x)
    return jsonify(msg="OK",data=doc)

@app.route("/api/<year>/<kota>",methods=["GET"])
def api2(year,kota):
    res = collections.find({"tahun":int(year),"kota":kota})
    doc = []
    for x in res:
        x.pop("_id")
        doc.append(x)
    return jsonify(msg="OK",data=doc)
    
    


if __name__ == "__main__":
    app.run(port=80,host='0.0.0.0')