#!/bin/bash

SCRIPT=./vote
PORT=11111

sudo tcpserver -H -R -c 500 0.0.0.0 $PORT $SCRIPT
