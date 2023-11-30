#!/bin/bash
# server options / methods / verbs
curl -s -I -X OPTIONS "$1" | grep -iF "allow" | cut -d ":" -f 2 | cut -d " " -f 2-
