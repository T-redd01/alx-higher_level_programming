#!/bin/bash
# send POST request with parameters
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
