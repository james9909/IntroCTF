#!/bin/bash

if [ $# -gt 0 ];
then
    PROBLEM_NAME=$1-INCOMPLETE

    mkdir -p $PROBLEM_NAME/{release,admin}
    touch $PROBLEM_NAME/Solution.txt
fi
