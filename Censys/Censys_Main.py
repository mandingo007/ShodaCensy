import Censys_Host
import CensysAPI
import Censys_Search
import sys


def Censys_Mode():
	Censys_Host.os.system('cls')
	while True:
		print """
        #################################################
        #--------------------CENSYS---------------------#
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
		print "[1] Search for specific host."
		print "[2] Search for targets with the specified query."
		print "[3] Switch to Shodan."
		print "[4] Exit.\n"

		choice = int(raw_input("($)> "))

		if choice   == 4:
			sys.exit(1)

		elif choice == 3:
			break

		elif choice == 1:
			Censys_Host.Host_Main()

		elif choice == 2:
			Censys_Host.os.system('cls')
			Censys_Search.Normal_Search_Main()

		else:
			print "[!] Invalid option, please enter a valid one !"
