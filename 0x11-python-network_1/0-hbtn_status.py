#!/usr/bin/python3
"""Fetching data from a website on the internet"""
import urllib.request


if __name__ == "__main__":
    response = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(response) as get_response:
        data = get_response.read()
        utf_data = data.decode('utf-8')
        resourceType = type(data)
        print(f"Body response:\n\t- type: {resourceType}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {utf_data}")
