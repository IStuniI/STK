import sys
from random import *
import os
import base64
import codecs
string = sys.argv[2]
crypt = sys.argv[1]
if os.path.isfile(string):
    string = open(string, "r").read()
def encrypt(string):
    string = base64.b64encode(string.encode('utf-8')).decode('utf-8')
    return string

def decrypt(string):
    string = base64.b64decode(string).decode('utf-8')
    return string


if crypt == "encrypt":
    print("INPUT: " + string)
    print("OUTPUT: " + encrypt(string))
elif crypt == "decrypt":
    try:
        print("INPUT: " + string)
        print("OUTPUT: " + decrypt(string))
    except Exception as e:
        print("OUTPUT: " + "Error: " + str(e))

os.system("pause")