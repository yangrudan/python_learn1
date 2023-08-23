"""
Copyright (c) Zhejiang Lab. All right reserved.
"""
import json
from flask import Flask, render_template, request

from ..db.manipulate_db import SqliteTool
from cal_sum import *

app = Flask(__name__)

db = SqliteTool()


@app.route('/add_a_record', methods=['POST', 'GET'])
def add_a_record():
    if request.method == "POST":
        kind = request.form['type']
        desc = request.form['desc']
        date = request.form['date']
        money = request.form['money']
        a_record = ()
        a_record.append(kind, desc, date, money)
        try:
            db.operate_one("""INSERT INTO CONSUMPTION (TYPE, DESC, DATE, MONEY) VALUES (?, ?, ?, ?)""", a_record)
            return "0"
        except Exception as err:
            print(Exception + ": " + err)
            return "-1"


@app.route('/del_a_record', methods=['POST', 'GET'])
def del_a_record():
    if request.method == "POST":
        kind = request.form['type']
        desc = request.form['desc']
        date = request.form['date']
        money = request.form['money']
        place = ()
        place.append(kind, desc, date, money)
        try:
            del_sql = "DELETE FROM CONSUMPTION WHERE TYPE = ? AND DESC=? AND DATE=? AND MONEY=?"
            db.operate_one(del_sql, place)
            return "0"
        except Exception as err:
            print(Exception + ": " + err)
            return "-1"


@app.route('/get_record_by_month', methods=['POST', 'GET'])
def get_records_by_month():
    if request.method == "POST":
        date = request.form['date']
        data_early, date_later = get_early_later_month(date)
        select_sql = "SELECT * FROM CONSUMPTION WHERE DATE BETWEEN '{}' AND '{}'".format(data_early, date_later)
        try:
            r = db.query_many(select_sql)
            return json.dumps({"info": r, "sum": cal_sum(r)})
        except Exception as err:
            print(Exception + ": " + err)
            return "-1"








if __name__ == '__main__':
    app.run(port=8080,debug=True)