#!/bin/bash
# script must send a POST request with the contents
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
