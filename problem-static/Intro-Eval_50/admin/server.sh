#!/bin/bash

SCRIPT=./eval.py
PORT=12345
_UID=$(id -u introeval)
_GID=$(id -g introeval)

sudo tcpserver -g $_GID -u $_UID -H -R -c 500 0.0.0.0 $PORT $SCRIPT
