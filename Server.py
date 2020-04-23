from flask import Flask, jsonify, g, request
from flask_cors import CORS
import sqlite3
app = Flask("__main__")
CORS(app)


@app.route("/<string:tag>",methods=["GET"])
def my_index(tag):
    database = "SuperMarket.db"
    try:
        conn = sqlite3.connect(database)
        cur=conn.cursor()
    except Error as e:
        print(e)
    cur.execute("SELECT * FROM {v}".format(v=tag))
    ans=cur.fetchall()
    #print(ans)
    return jsonify({'data':ans})

app.run()
