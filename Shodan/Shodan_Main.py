import os
import Exploit_Shod
import Normal_Shod
import API
import Host_Shod
import sys


def Shodan_Mode():
    os.system('cls')
    while True:
        print """
        #################################################
        #--------------------SHODAN---------------------#
        #                                               #
        #             .-=d88888888888b=-.               #
        #         .:d8888pr"|\|/-\|'rq8888b.            #
        #       ,:d8888P^//\-\/_\ /_\/^q88888b.         #
        #     ,;d88888/~-/ .-~  _~-. |/-q88888b,        #
        #    //8888887-\ _/    (#)   \-\/Y88888b\       #
        #    \8888888|// T      `    Y _/|888888 o      #
        #     \q88888|- \l           !\_/|88888p/       #
        #      'q8888l\-//\         / /\|!8888P'        #
        #        'q888\/-| "-,___.-^\/-\/888P'          #
        #          `=88\./-/|/ |-/!\/-!/88='            #
        #             ^^'-------------'^^               #
        #                                               #
        #################################################
                     \n\n"""
        print "[1] Exploit search."
        print "[2] Shodan search."
        print "[3] Host search."
        print "[4] Switch to Censys."
        print "[5] Exit.\n"
        try:
            choice = int(raw_input("($)> "))

            if choice == 1:
                os.system('cls')
                Exploit_Shod.Main_Exploits()
            elif choice == 2:
                os.system('cls')
                Normal_Shod.Shodan_Search_Main()
            elif choice == 3:
                os.system('cls')
                Host_Shod.Host_Main()
            elif choice == 4:
                break
            elif choice == 5:
                print "Goodbye!"
                sys.exit(1)
        except ValueError:
            print "[!] Enter a valid option please !"

