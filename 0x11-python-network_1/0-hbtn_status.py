#!/usr/bin/python3
"""Fetching data from a website on the internet"""
import urllib.request


if __name__ == "__main__":
    response = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(response) as get_response:
        utf_data = get_response.read().decode('utf-8')
        resourceType = type(get_response.read())
        print(f"Body response:\n\t- type: {resourceType}")
        print(f"\t- content: {get_response.read()}")
        print(f"\t- utf8 content: {utf_data}")

