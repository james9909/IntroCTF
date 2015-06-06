#!/bin/bash

RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[m"

function close_port() {
    pid=$(netstat -lpn 2> /dev/null | grep "0.0.0.0:$1" | grep -o "[0-9]*/$2" | cut -d '/' -f 1)
    if [[ $pid != "" ]]; then
        printf "${YELLOW}Closing port $1.... ${RESET}\n"
        kill -9 $pid
    fi
}

close_port $1
