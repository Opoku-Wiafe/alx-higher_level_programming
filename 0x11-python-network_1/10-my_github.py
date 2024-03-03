#!/usr/bin/python3
"""GitHub credentials (username and password)"""
import requests
import sys

if __name__ == "__main__":
    userName = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    response = requests.get("https://api.github.com/userName", headers=headers)
    if (response.status_code >= 400):
        print("None")
        exit()
    print(response.json()["id"])
