#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
        content = response.read()

        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content.decode('utf-8'))
        print("    - utf8 content:", content.decode('utf-8'))

