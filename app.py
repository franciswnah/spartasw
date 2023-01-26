from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://francis:francisSparta@cluster0.he73hna.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickname = request.form['nickname_give']
    comment = request.form['comment_give']

    doc = {
        'nickname': nickname,
        'comment': comment,
    }
    db.fanDB.insert_one(doc)
    return jsonify({'msg': '응원 저장 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    fanDB_list = list(db.fanDB.find({}, {'_id': False}))
    print(fanDB_list)
    return jsonify({'fanDB':fanDB_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)