#!/bin/sh

bulkloader.py --filename=data/bancos-ascii.csv --config_file=data/banco_loader.py --kind=Banco --url=http://localhost:8080/remote_api --application=gitasoftweb  --auth_domain=localhost:8080 --email=foobar@nowhere.com

