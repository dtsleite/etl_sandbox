#!/usr/bin/env bash

echo "Iniciando config aguarde ..."

echo "Verificando instalacao do Python 3"
if command -v python3 &>/dev/null; then
    echo "Python 3 esta instalado. SKip."
else
    echo "Instalando Python 3 ..."
    sudo apt-get install python3
fi

echo "Instalando pip"
sudo apt-get install python3-pip --yes

echo "Instalando virtualenv"
sudo pip3 install virtualenv

echo "Criando ambiente virtual sandbox"
virtualenv .

source $(pwd)/bin/activate
pip3 install flask
pip3 install aiohttp
pip3 install git+https://github.com/ebraminio/aiosseclient

echo "Iniciando servidor web da aplicação ..."
python3 src/main.py



