#!/bin/sh
cd ./homework2/
make clean
make test ARG='-k ./tests'
make test
make env
make cover
