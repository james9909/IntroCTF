#!/bin/bash

SCRIPT=./overflow
PORT=13579

sudo tcpserver -H -R -c 500 0.0.0.0 $PORT $SCRIPT
