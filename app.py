from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://Admin:Admin123@cluster1.jumillq.mongodb.net/?appName=Cluster1")

db = client["todoDB"]

collection = db["items"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api')
def api():

    with open('data.json') as file:
        data = json.load(file)

    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submit():

    itemName = request.form.get('itemName')

    itemDescription = request.form.get('itemDescription')

    data = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(data)

    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)