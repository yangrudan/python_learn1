"""
Copyright (c) Zhejiang Lab. All right reserved.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/add_a_record', methods=['POST', 'GET'])
def add_a_record():
    if request.method == "POST":
        kind = request.form['type']
        desc = request.form['desc']
        date = request.form['date']
        money = request.form['money']
        pass


@app.route('/del_a_record', methods=['POST', 'GET'])
def del_a_record():
    if request.method == "POST":
        kind = request.form['type']
        desc = request.form['desc']
        date = request.form['date']
        money = request.form['money']
        pass


@app.route('/get_record_by_month', methods=['POST', 'GET'])
def get_records_by_month():
    if request.method == "POST":
        date = request.form['date']
        pass


@app.route('/cal_sum', methods=['POST', 'GET'])
def cal_sum():
    if request.method == "POST":
        date = request.form['date']
        pass





if __name__ == '__main__':
    app.run(port=8080,debug=True)