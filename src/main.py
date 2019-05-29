#!/usr/bin/env python
#- * -coding: utf - 8 - * -
'''
    Ponto de entrada principal para aplicação.
    autor: Douglas T. S. Leite
    data: 25-05-2019
'''
import json
import asyncio
import aiohttp
from aiosseclient import aiosseclient

from load import *

db_name = 'test_home.db'
table_name = 'recent_changes'


# EXTRACT
# extrai os dados necessários do servico
async def extract(url):
    async for event in aiosseclient(url):
        if event.event == 'message':
            transform(event)

# TRANSFORM
# realiza as transformações necessários se houver
def transform(event):
    try:
        change = json.loads(event.data)
        if(change['bot'] == False):
            print(json.dumps(change, indent = 4, sort_keys=True))
            load(change)

    except ValueError:
        pass
# LOAD
# carrega o conteudo desejado para um arquivo ou banco de dados
def load(data):
    load_op = Load()
    load_op.write_database(data)
    

def main():
    url = 'https://stream.wikimedia.org/v2/stream/recentchange'

    loop = asyncio.get_event_loop()
    loop.run_until_complete(extract(url))

if __name__ == "__main__":
    main()