#!/usr/bin/env python
#- * -coding: utf - 8 - * -
'''
    Classe responsável por carregar os dados para um arquivo utilizando um formato especifico ou enviando para um bando de dados

    autor: Douglas T. S. Leite
    data: 25-05-2019
'''

import sys
import sqlite3
import datetime
import config

class Load:

    def __init__(self):
        self.db_name = config.config_values['db_name']

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except ValueError:
            e = sys.exc_info()[0]
            print("Error: %s" % e)

        return None

    def create_table(self):
        sql_create_table = '''
                    CREATE TABLE IF NOT EXISTS recent_changes(
                        id text DEFAULT NULL,
                        timestamp text DEFAULT NULL,
                        type text DEFAULT NULL,
                        title text DEFAULT NULL,
                        user text DEFAULT NULL,
                        wiki text DEFAULT NULL,
                        date_created TIMESTAMP not null
                    );
        '''

        conn = self.create_connection(self.db_name)
        cur = conn.cursor()
        try:
                cur.execute(sql_create_table)
        finally:
            cur.close()
            

    # grava os dados obtidos para um banco de dados SQL
    def write_database(self, data):
        conn = self.create_connection(self.db_name)
        self.create_table()
        cur = conn.cursor()
        try:
                cur.execute('insert into recent_changes values (?,?,?,?,?,?,?)', [str(data['id']),str(data['timestamp']),str(data['type']),str(data['title']),str(data['user']),str(data['wiki']),datetime.datetime.now()])
                conn.commit()
                print('Registro gravado :', [str(data['id']),str(data['timestamp']),str(data['type']),str(data['title']),str(data['user']),str(data['wiki'])])
                return cur.fetchone
        except KeyError:
            pass
        finally:
            cur.close()



    # grava os dados obtidos para um arquivo do tipo json
    def write_file(self, data):
        pass




    
