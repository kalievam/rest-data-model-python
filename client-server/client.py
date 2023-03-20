import os
import sys
import http.client
import urllib.parse

HOST = "0.0.0.0"
PORT = 8000

path = os.path.abspath(sys.argv[1])      # get upload file from arguments and make full path, including the directory
content_type = "application/octet-stream"       # content type

# Open a connection to the server
conn = http.client.HTTPConnection(HOST, PORT)

# List the contents of the directory
conn.request("GET", f"test-env")
rslt = conn.getresponse()
if rslt.status == 200:    print(rslt.read().decode())
else:    print(f"Error {rslt.status}")


# Upload a file
with open(path, "rb") as f:
    conn.request("POST", f"/{path}", body=f.read(), headers={"Content-Type": content_type})
    rslt = conn.getresponse()
    if rslt.status == 200:        print("Upload successful")
    else:        print(f"Error {rslt.status}")
