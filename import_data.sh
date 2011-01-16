#!/bin/sh

bulkloader.py --filename=data/bancos.csv --config_file=data/banco_loader.py --kind=Banco --url=http://localhost:8080/import --application=gitasoftweb

