#!/usr/bin/env bash
echo "Criando ambiente virtual sandbox"
virtualenv .

source $(pwd)/bin/activate

echo "Iniciando servidor web da aplicação ..."
python3 src/dashboard.py



