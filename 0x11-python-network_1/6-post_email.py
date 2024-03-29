#!/usr/bin/python3
""" Python script that takes in a URL and an email address, sends a POST"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    parameters = {"email": email}
    res = requests.post(url, data=parameters)
    print(res.text)
