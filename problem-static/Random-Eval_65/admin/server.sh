#!/bin/bash

SCRIPT=./eval.py
PORT=54321
_UID=$(id -u randomeval)
_GID=$(id -g randomeval)

if [[ $_UID == "" || $_GID == "" ]]; then
    printf "Missing user. Attempting to add user....\n"
    sudo ./users.sh
    if [[ $? == 0 ]]; then
        printf "SUCCESS! RESTART THE SCRIPT TO DEPLOY\n"
        exit 0
    else
        printf "FAILURE :(\n"
        exit 1
    fi
fi

sudo tcpserver -g $_GID -u $_UID -H -R -c 500 0.0.0.0 $PORT $SCRIPT
