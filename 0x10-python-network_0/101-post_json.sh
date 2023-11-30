#!/bin/bash
# pass json file as data with curl post request
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
