#!/bin/bash

PATH="/"
name="$PATH/rsa.private"
openssl genrsa -3 -out name 1024

VAR=diff $name key.pem

echo $var