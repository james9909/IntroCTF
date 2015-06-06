#!/bin/bash

RED="\033[1;31m"
YELLOW="\033[1;33m"
GREEN="\033[1;32m"
RESET="\033[m"

SCRIPT=./eval.py
PORT=12345
_UID=$(id -u introeval)
_GID=$(id -g introeval)

if [[ $_UID == "" || $_GID == "" ]]; then
    printf "Missing user. Attempting to add user....\n"
    sudo ./users.sh
    if [[ $? == 0 ]]; then
        printf "${GREEN}Success!${RESET}\n"
    else
        printf "${RED}Failed to add users....${RESET}\n"
        exit 1
    fi
fi

if sudo tcpserver -g $_GID -u $_UID -H -R -c 500 0.0.0.0 $PORT $SCRIPT 2>&1 | grep "unable to bind" > /dev/null; then
    printf "${RED}ERROR! Port ${PORT} is already in use!${RESET}\n"
else
    printf "${GREEN}Success!${RESET}\n"
fi