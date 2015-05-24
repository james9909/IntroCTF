#!/bin/bash

echo "What is the name of this problem?"
read name
echo "How many points is this problem worth?"
read points
PROBLEM_NAME=$name\_$points-INCOMPLETE
mkdir -p $PROBLEM_NAME/{release,admin}
touch $PROBLEM_NAME/Solution.txt
