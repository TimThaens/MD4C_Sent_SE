#!/bin/bash



curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list

sudo apt-get update





sudo apt install freerdp2-x11 hydra tor torsocks python3-pip python3-venv unixodbc unixodbc-dev msodbcsql18 -y

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

python3 -m venv venv

source venv/bin/activate

pip install pyodbc


