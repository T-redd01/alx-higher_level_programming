#!/bin/bash
# get value of specific response header
curl -s -I -o /dev/null -w "%{http_code}" "$1"
