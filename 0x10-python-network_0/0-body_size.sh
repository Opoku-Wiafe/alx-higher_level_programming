#!/bin/bash
# Bash script that send url and displays the size of body
curl -s "$1" | wc -c
