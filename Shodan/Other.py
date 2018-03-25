import API
import os
import sys

# Set the default encoding to UTF-8
reload(sys)
sys.setdefaultencoding("UTF-8")

# def Reverse_Lookup():
#
#
#
# def Dns_Lookup():
#     while True:
#         print "[1] Dns Revers lookup."
#         print "[2] Dns rezolve lookup."
#
#         choice = raw_input("What do you want to do? : "")
#
#         if choice == 1:
#             Reverse_Lookup()
#         elif choice == 2:
#             Rezolve_Lookup()

def Check_Honeypot():
    host = raw_input("Enter the ip address you want to check for: ")
    honeypot = APi.api.labs.honeyscore(host) # Get the honeypot score
    print "This host have a score of {} beeing a honeypot!\n".format(honeypot)

def Main():
    print """------Some Banner--------"""
    while True:
        print "[1] Dns lookup with Shodan."
        print "[2] Check for honeypot."
        print "[3] Check the HTTP headers you send."
        print "[4] Quit."

        choice = raw_input("What do you want to do? : ")

        if choice == 4:
            os.system('cls')
            break
        elif choice == 1:
            os.system('cls')
            Dns_Lookup()
        elif choice == 2:
            os.system('cls')
            Check_Honeypot()
        elif choice == 3:
            os.system('cls')
            Check_HTTP_Headers()
