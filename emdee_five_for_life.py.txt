import requests
import hashlib
import json

URL = "http://docker.hackthebox.eu:35405"

# Get PHPSESSID
def get_cookie():
   response = requests.get(URL)
   headers = dict(response.headers)
   return headers["Set-Cookie"]

# Get value from response string
def get_value(data):
   start = "<h3 align='center'>"
   end = "</h3>"
   return data[data.find(start)+len(start):data.rfind(end)]

# Get flag from response string
def get_flag(data):
   start = "<p align='center'>"
   end = "</p>"
   return data[data.find(start)+len(start):data.rfind(end)]

# Main function
def main():
   print "[*] Getting cookie..."
   cookie = get_cookie()

   print "[*] Asking for data to hash..."
   data = requests.get(URL, headers={'cookie': cookie}).text
   value = get_value(data)
   md5 = hashlib.md5(value).hexdigest()

   print "[*] Sending hash..."
   data = requests.post(URL, data={'hash': md5}, headers={'cookie': cookie}).text
   flag = get_flag(data)

   print "[*] Retreiving data..."
   print "Flag: " + flag

if __name__ == '__main__':
   main()
