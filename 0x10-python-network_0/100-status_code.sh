#!/bin/bash
# script that sends a JSON POST request to a URL passed as args
curl -sw '%{http_code}' -o /dev/null "$1"
