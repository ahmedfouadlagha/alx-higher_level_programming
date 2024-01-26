#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        Response = response.read()
        print("Body response:")
        print("\t- type: ",type(Response))
        print("\t- content: ",Response)
        print("\t- utf8 content: ",Response.decode('utf-8'))
