#!/bin/bash

RED="\033[1;31m"
YELLOW="\033[1;33m"
GREEN="\033[1;32m"
RESET="\033[m"

SCRIPT=./vote
PORT=11111

if sudo tcpserver -H -R -c 500 0.0.0.0 $PORT $SCRIPT 2>&1 | grep "unable to bind" > /dev/null; then
    printf "${RED}ERROR! Port ${PORT} is already in use!${RESET}\n" 
fi
