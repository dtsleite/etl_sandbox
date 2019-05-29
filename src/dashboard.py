#!/usr/bin/env python
#- * -coding: utf - 8 - * -
'''
    Classe responsável por disponibilizar os dados via http rest

    autor: Douglas T. S. Leite
    data: 25-05-2019
'''
from flask import Flask, jsonify, request, render_template
import sys
import os
import sqlite3
import config

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

def get_sqlite_data():
    try:
        conn = sqlite3.connect(config.config_values['db_name'])
        cur = conn.cursor()
        data = cur.execute('SELECT count(*), date_created FROM recent_changes')
        rows = cur.fetchall()
        return rows
    except ValueError:
        e = sys.exc_info()[0]
        print("Error: %s" % e)

@app.route('/', methods=['GET'])
def index():
    return render_template('dashboard.html')

@app.route('/get_totals', methods=['GET'])
def get_totals():
    total_records = get_sqlite_data()
    return jsonify(total_records), 200

if __name__ == '__main__':
    db_val = config.config_values['db_name']
    app.run(host='0.0.0.0', port=8080, debug=True)