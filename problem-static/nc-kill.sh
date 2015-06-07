#!/bin/bash

RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[m"

declare -a ports=("11111" "12345" "13579" "54321" "33333" "22222")

function close_port() {
    for PORT in "${ports[@]}"; do
    	pid=$(sudo netstat -lpn 2> /dev/null | grep "0.0.0.0:$PORT" | grep -o "[0-9]*/tcpserver" | cut -d '/' -f 1)
    	if [[ $pid != "" ]]; then
    	    printf "${YELLOW}Killing netcat server on port $PORT.... ${RESET}\n"
    	    sudo kill -9 $pid
    	else
    	    printf "${RED}Process using port $PORT not found.... ${RESET}\n"
    	fi
    done
}

close_port $1 
