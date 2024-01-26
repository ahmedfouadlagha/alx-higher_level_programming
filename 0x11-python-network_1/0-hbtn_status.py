#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print(f"\t- type: {}",type(response))
        print(f"\t- content: {}",response)
        print(f"\t- utf8 content: {}",response.decode('utf-8'))
