import censys
from censys import certificates, data, ipv4, websites, query

def create_API():
	UID    = raw_input("Enter your UID    : ") 
	SECRET = raw_input("Enter your SECRET : ")
	IPv4   = ipv4.CensysIPv4(UID, SECRET)
	return IPv4

IPv4 = create_API()