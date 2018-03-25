import os
import sys
import CensysAPI
from Censys_Host import get_ports_and_proto

reload(sys)
sys.setdefaultencoding("UTF-8")

# DISPLAY PAGES FOR TARGETS TO CHOOSE FROM 
def search_for_hosts(query):
	print "[+] Searching for your query..."
	generator = CensysAPI.IPv4.search(query)
	while True:
		for i in range(10):
			target    = generator.next()
			ports_and_protocols = get_ports_and_proto(target['protocols'])
			print "[#]-----------[INFO]-----------[#]"
			try:
				print "[{}]\tLOCATION: {} \n#\tIP: {} \n#\tPORTS: {}\t".format(i + 1, target['location.country'], target['ip'], [port for port in ports_and_protocols])
			except KeyError:
				print "[{}]\tLOCATION: {} \n#\tIP: {} \n#\tPORTS: {}\t".format(i + 1, "None", target['ip'], [port for port in ports_and_protocols])
			print "[#]----------------------------[#]\n\n"
		choice = raw_input("\n\n[*] Show next 10 results? : ")
		if choice == 'Y' or choice == 'yes' or choice == 'y':
			os.system('cls')
			continue
		else:
			break


def Normal_Search_Main():
	print """\n\n
	  /$$$$$$  /$$$$$$$$ /$$   /$$  /$$$$$$  /$$     /$$ /$$$$$$         /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
	 /$$__  $$| $$_____/| $$$ | $$ /$$__  $$|  $$   /$$//$$__  $$       /$$__  $$| $$_____/ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$
	| $$  \__/| $$      | $$$$| $$| $$  \__/ \  $$ /$$/| $$  \__/      | $$  \__/| $$      | $$  \ $$| $$  \ $$| $$  \__/| $$  | $$
	| $$      | $$$$$   | $$ $$ $$|  $$$$$$   \  $$$$/ |  $$$$$$       |  $$$$$$ | $$$$$   | $$$$$$$$| $$$$$$$/| $$      | $$$$$$$$
	| $$      | $$__/   | $$  $$$$ \____  $$   \  $$/   \____  $$       \____  $$| $$__/   | $$__  $$| $$__  $$| $$      | $$__  $$
	| $$    $$| $$      | $$\  $$$ /$$  \ $$    | $$    /$$  \ $$       /$$  \ $$| $$      | $$  | $$| $$  \ $$| $$    $$| $$  | $$
	|  $$$$$$/| $$$$$$$$| $$ \  $$|  $$$$$$/    | $$   |  $$$$$$/      |  $$$$$$/| $$$$$$$$| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$
	 \______/ |________/|__/  \__/ \______/     |__/    \______/        \______/ |________/|__/  |__/|__/  |__/ \______/ |__/  |__/
 \n\n"""
	query = raw_input("[*] Query to search for: ")
	search_for_hosts(query)