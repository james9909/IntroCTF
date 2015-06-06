#!/bin/bash

GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[m"
if [[ -x /usr/bin/tcpserver ]]; then
    printf "${YELLOW}tcpserver is installed!${RESET}\n"
else
    printf "${YELLOW}Installing tcpserver....${RESET}\n"
    sudo apt-get install ucspi-tcp
fi

printf "${GREEN}Starting netcat servers....${RESET}\n"

for tcpserver in `find . -name "server.sh"`
do
    directory=$(dirname $tcpserver)
    problem_name=${tcpserver%/*/*}
    problem_name=${problem_name/.\//}
    printf "${GREEN}Deploying $problem_name....${RESET}\n"
    bash -c "cd $directory && ./server.sh" &
done
