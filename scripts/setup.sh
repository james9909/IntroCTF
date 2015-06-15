#!/bin/bash

GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[m"

printf "${YELLOW}Setting up users....${RESET}\n"
cd ..
mkdir accounts
cd accounts
touch login_list.txt teams.txt solved.txt scores.txt users.txt
chmod 707 *.txt
printf "${GREEN}Success!${RESET}"
