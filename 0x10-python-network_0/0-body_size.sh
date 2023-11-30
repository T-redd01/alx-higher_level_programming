#!/bin/bash
# capture length of http response
curl -s -I "$1" | grep -iF "content-length" | cut -d ":" -f 2 | tr -d " "
