'''


import urllib.request as urllib

def main(url):
    print("Connection checking")

    response = urllib.urlopen(url)

    print("Connected to", url , "successfully...")
    print("The response code was ", response.getcode())

print("This is a site connecticity checker program")

input_url = input("Input the url of the site you want to check: ")
main(input_url) 
'''
#practice1

import urllib.request as urllib

def main(url):
    print("Connection checking...")

    response = urllib.urlopen(url)

    print("Connected to ", url , "successfully")
    print("The respnse code was ", response.getcode())

print("This is site connection checker programn...")

input_url = input("Enter thre the url which you want to see the connection status : ")

main(input_url)