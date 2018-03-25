import json
import os
import CensysAPI
import sys


reload(sys)
sys.setdefaultencoding("UTF-8")

# QUERY THE TARGET
def get_result(host):
	target = CensysAPI.IPv4.view(host)
	return target

# WRITE DATA TO FILE (JSON FORMAT)
def write_info_to_file(host):
	# target = ipv4.view(host)
	os.system('cls')
	filename = raw_input("[+] Enter the filename you want to save to: ")
	with open(filename, "w") as f:
		 json.dump(host, f, indent=4, sort_keys=True)
	print "[+] Data has been written to {}.".format(filename)


# PREPARE PORTS AND PROTOCOLS
def get_ports_and_proto(array):
	port_and_protocols = {}
	for proto_port in array:
		pair = proto_port.split('/')
		port_and_protocols[pair[0]] = pair[1]
	return port_and_protocols


# DISPLAY TARGET DATA
def target_data(target):

	pairs = get_ports_and_proto(target['protocols'])

	for port, protocol in pairs.iteritems():

		# GO RIGHT INTO THE PORT AND PROTOCOL AND DISPLAY INFO ABOUT THEM
		for key, value in target[port][protocol].iteritems():
			print '\n\n[#]----------------------[PORT {} | PROTOCOL {}]---------------------[#]\n\n'.format(port, protocol)


	#		[#]---------------------------------------------------[HTTP]--------------------------------------------------------[#]
			# CHECK FOR GET KEY
			if key == 'get':


				# ITERATE OVER GET VALUES
				for getkey, getvalue in value.iteritems():


					# DISPLAY HEADERS
					if getkey == 'headers':
						print "\n\t[#]--------------------------[HEADERS]---------------------------[#]\n"
						for headerk, headerv in getvalue.iteritems():
							print "\t[*]{} : {}".format(headerk, headerv)
						print "\n\t[#]--------------------------------------------------------------[#]\n"


					# GET OVER THE HTML CODE
					elif getkey == 'body':
						continue


					# DISPLAY METADATA
					elif getkey == "metadata":
						print "\n\t[#]-------------------------[METADATA]---------------------------[#]\n"
						for metak, metav in getvalue.iteritems():
							print "\t[*]{} : {}".format(metak, metav)
						print "\n\t[#]--------------------------------------------------------------[#]\n"


					# DISPLAY OTHER DATA
					else:
						print "\t[*]{} : {}".format(getkey, getvalue)




			elif key == 'heartbleed':
				 for heartbleedk, heartbleedv in value.iteritems():
				 	print "\t[*]{} : {}".format(heartbleedk, heartbleedv)

			elif key == 'rsa-export':
				for rsa_exportk, rsa_exportv in value.iteritems():
					print "\t[*]{} : {}".format(rsa_exportk, rsa_exportv)

			elif key == 'tls':
				print "\n\t[#]-------------------------[TLS]---------------------------[#]\n"
				for tlskey, tlsvalue in value.iteritems():

					# DISPLAY CERTIFICATE DATA
					if tlskey == 'certificate':	
						print "\n\t\t[#]----------------------[CERTIFICATE]----------------------[#]\n"
						for certkey, certvalue in tlsvalue.iteritems():


							# GO INTO PARSED VALUE
							if certkey == 'parsed':
								for parsedk, parsedv in certvalue.iteritems():


									if parsedk == 'extensions':
										print "\n\t\t\t[#]-------[EXTENSIONS]------[#]\n"
										for extensionk, extensionv in parsedv.iteritems():
											print "\t\t\t[*]{} : {}".format(extensionk, extensionv)
										print "\n\t\t\t[#]-------------------------[#]\n"


									# DISPLAY ISSUER DATA
									elif parsedk   == 'issuer':
										print "\n\t\t\t[#]---------[ISSUER]--------[#]\n"
										for issuerkey, issuervalue in parsedv.iteritems():
											print "\t\t\t[*]{} : {}".format(issuerkey, issuervalue)
										print "\n\t\t\t[#]-------------------------[#]\n"


									# DISPLAY SIGNATURE DATA
									elif parsedk == 'signature':
										print "\n\t\t\t[#]-----[SIGNATURE]-----[#]\n"
										for signaturek, signaturev in parsedv.iteritems():
											print "\t\t\t[*]{} : {}".format(signaturek, signaturev)
										print "\n\t\t\t[#]-------------------------[#]\n"



									# DISPLAY SIGNATURE ALG DATA
									elif parsedk == 'signature_algorithm':
										print "\n\t\t\t[#]---[SIGNATURE-ALG]---[#]\n"
										for signalgk, signalgv in parsedv.iteritems():
											print "\t\t\t[*]{} : {}".format(signalgk, signalgv)
										print "\n\t\t\t[#]-------------------------[#]\n"


									# DISPLAY SUBJECT DATA
									elif parsedk == 'subject':
										print "\n\t\t\t[#]------[SUBJECT]------[#]\n"
										for subjectk, subjectv in parsedv.iteritems():
											print "\t\t\t[*]{} : {}".format(subjectk, subjectv)
										print "\n\t\t\t[#]---------------------[#]\n"


									# DISPLAY KEY-INFO DATA			
									elif parsedk == 'subject_key_info':
										print "\n\t\t\t[#]------[KEY-INFO]-----[#]\n"
										for keyinfok, keyinfov in parsedv.iteritems():
											print "\t\t\t[*]{} : {}".format(keyinfok, keyinfov)
										print "\n\t\t\t[#]---------------------[#]\n"


									# DISPLAY VALIDITY DATA
									elif parsedk == 'validity':
										print "\n\t\t\t[#]------[VALIDITY]-----[#]\n"
										for validkey, validvalue in parsedv.iteritems():					
											print "\t\t\t[*]{} : {}".format(validkey, validvalue)
										print "\n\t\t\t[#]---------------------[#]\n"

						print "\n\t\t[#]---------------------------------------------------------[#]\n"





	#		[#]---------------------------------------------------[SMB]--------------------------------------------------------[#]
			# CHECK FOR BANNER KEY
			elif key == 'banner':

				# DISPLAY BANNER DATA
				print "\n\t[#]-------------------------[BANNER]---------------------------[#]\n"
				for bannerk, bannerv in value.iteritems():
					print "\t[*]{} : {}".format(bannerk, bannerv)
				print "\n\t[#]------------------------------------------------------------[#]\n"





	#		[#]---------------------------------------------------[TLS]--------------------------------------------------------[#]		
			elif key == 'starttls':
				for starttlsk, starttlsv in value.iteritems():

					# DISPLAY TLS DATA
					if starttlsk == 'tls':
						print "\n\t[#]-------------------------[TLS]---------------------------[#]\n"
						for tlskey, tlsvalue in starttlsv.iteritems():



							# DISPLAY CERTIFICATE DATA
							if tlskey == 'certificate':	
								print "\n\t\t[#]----------------------[CERTIFICATE]----------------------[#]\n"
								for certkey, certvalue in tlsvalue.iteritems():


									# GO INTO PARSED VALUE
									if certkey == 'parsed':
										for parsedk, parsedv in certvalue.iteritems():


											# DISPLAY ISSUER DATA
											if parsedk   == 'issuer':
												print "\n\t\t\t[#]-------[ISSUER]------[#]\n"
												for issuerkey, issuervalue in parsedv.iteritems():
													print "\t\t\t[*]{} : {}".format(issuerkey, issuervalue)
												print "\n\t\t\t[#]-------------------------[#]\n"


											# DISPLAY SIGNATURE DATA
											elif parsedk == 'signature':
												print "\n\t\t\t[#]-----[SIGNATURE]-----[#]\n"
												for signaturek, signaturev in parsedv.iteritems():
													print "\t\t\t[*]{} : {}".format(signaturek, signaturev)
												print "\n\t\t\t[#]-------------------------[#]\n"



											# DISPLAY SIGNATURE ALG DATA
											elif parsedk == 'signature_algorithm':
												print "\n\t\t\t[#]---[SIGNATURE-ALG]---[#]\n"
												for signalgk, signalgv in parsedv.iteritems():
													print "\t\t\t[*]{} : {}".format(signalgk, signalgv)
												print "\n\t\t\t[#]-------------------------[#]\n"


											# DISPLAY SUBJECT DATA
											elif parsedk == 'subject':
												print "\n\t\t\t[#]------[SUBJECT]------[#]\n"
												for subjectk, subjectv in parsedv.iteritems():
													print "\t\t\t[*]{} : {}".format(subjectk, subjectv)
												print "\n\t\t\t[#]-------------------------[#]\n"


											# DISPLAY KEY-INFO DATA			
											elif parsedk == 'subject_key_info':
												print "\n\t\t\t[#]------[KEY-INFO]-----[#]\n"
												for keyinfok, keyinfov in parsedv.iteritems():
													print "\t\t\t[*]{} : {}".format(keyinfok, keyinfov)
												print "\n\t\t\t[#]-------------------------[#]\n"


											# DISPLAY VALIDITY DATA
											elif parsedk == 'validity':
												print "\n\t\t\t[#]------[VALIDITY]-----[#]\n"
												for validkey, validvalue in parsedv.iteritems():
													print "\t\t\t[*]{} : {}".format(validkey, validvalue)			
												print "\n\t\t\t[#]-------------------------[#]\n"
									
								print "\n\t\t[#]---------------------------------------------------------[#]\n"	

							# DISPLAY CIPHERS
							elif tlskey == 'cipher_suite':
								print "\n\t\t[#]----------------------[CIPHERS]--------------------------[#]\n"
								for cipherk, cipherv in tlsvalue.iteritems():
									print "\t\t[*]{} : {}".format(cipherk, cipherv)
								print "\n\t\t[#]---------------------------------------------------------[#]\n"


							# DISPLAY SV-KEY-EXCHANGE
							elif tlskey == 'server_key_exchange':
								print "\n\t\t[#]-----------------[SERVER-KEY-EXCHANGE]-------------------[#]\n"
								for serverkeyexk, serverkeyexv in tlsvalue.iteritems():
									print "\t\t[*]{} : {}".format(serverkeyexk, serverkeyexv)
								print "\n\t\t[#]---------------------------------------------------------[#]\n"


							# DISPLAY SIGNATURE
							elif tlskey == 'signature':
								print "\n\t\t[#]----------------------[SIGNATURE]------------------------[#]\n"
								for signaturek, signaturev in tlsvalue.iteritems():
									print "\t\t[*]{} : {}".format(signaturek, signaturev)
								print "\n\t\t[#]---------------------------------------------------------[#]\n"


							# DISPLAY VALIDATION
							elif tlskey == 'validation':
								print "\n\t\t[#]---------------------[VALIDATION]------------------------[#]\n"
								for validkey, validvalue in tlsvalue.iteritems():
									print "\t\t[*]{} : {}".format(validkey, validvalue)
								print "\n\t\t[#]---------------------------------------------------------[#]\n"

						print "\n\t[#]---------------------------------------------------------[#]\n"



	#		[#]---------------------------------------------------[DNS]--------------------------------------------------------[#]
			elif key == "lookup":
				for lookupkey, lookupvalue in value.iteritems():
					print "\t[*]{} : {}".format(lookupkey, lookupvalue)





	#		[#]---------------------------------------------------[SSH]--------------------------------------------------------[#]
			# CHECK FOR V2 KEY
			elif key == 'v2':

				# ITERATE OVER V2 VALUES
				for v2key, v2value in value.iteritems():


					# DISPLAY BANNER
					if v2key == 'banner':
						print "\n\t[#]-------------------------[BANNER]---------------------------[#]\n"
						for bannk, bannv in v2value.iteritems():
							print "\t[*]{} : {}".format(bannk, bannv)
						print "\n\t[#]------------------------------------------------------------[#]\n"


					# DISPLAY METADATA
					elif v2key == 'metadata':
						print "\n\t[#]-------------------------[METADATA]-------------------------[#]\n"
						for metak, metav in v2value.iteritems():
							print "\t[*]{} : {}".format(metak, metav)
						print "\n\t[#]------------------------------------------------------------[#]\n"


					# DISPLAY SELECTED DATA
					elif v2key == 'selected':

						print "\n\t[#]-------------------------[SELECTED]-------------------------[#]\n"
						# ITERATE OVER SELECTED VALUES
						for selectedk, selectedv in v2value.iteritems():
							print "\t\t[*]{} : {}".format(selectedk, selectedv)


							# DISPLAY CLIENT TO SERVER DATA
							if selectedk == "client_to_server":
								print "\n\t\t[#]---------------------[CLIENT-->SERVER]----------------------[#]\n"
								for cli_serverk, cli_serverv in selectedv.iteritems():
									print "\t\t[*]{} : {}".format(cli_serverk, cli_serverv)
								print "\n\t\t[#]------------------------------------------------------------[#]\n"


							# DISPLAY SERVER TO CLIENT DATA
							elif selectedk == "server_to_client":
								print "\n\t\t[#]---------------------[SERVER-->CLIENT]----------------------[#]\n"
								for sv_clientk, sv_clientv in selectedv.iteritems():
									print "\t\t[*]{} : {}".format(sv_clientk, sv_clientv)
								print "\n\t\t[#]------------------------------------------------------------[#]\n"

						print "\n\t[#]------------------------------------------------------------[#]\n"


					# DISPLAY SERVER-HOST-KEY VALUES
					elif v2key == 'server_host_key':


						# ITERATE OVER SERVER-HOST-KEY VALUES
						for server_h_key, server_h_value in v2value.iteritems():


							# DISPLAY ECDSA-PUB-KEY DATA
							if server_h_key == 'ecdsa_public_key':
								print "\n\t[#]---------------------[ECSDA-PUB-KEY]-----------------------[#]\n"
								for ecdsa_pub_key, ecdsa_pub_value in server_h_value.iteritems():
									print "\t[*]{} : {}".format(ecdsa_pub_key, ecdsa_pub_value)
								print "\n\t[#]-----------------------------------------------------------[#]\n"

							# DISPLAY WHAT IS LEFT OVER
							else:
								print "\t[*]{} : {}".format(server_h_key, server_h_value)


					# DISPLAY SUPPORT DATA
					elif v2key == 'support':


						# ITERATE OVER IT
						for suppkey, suppvalue in v2value.iteritems():
							
							# DISPLAY CLIENT-TO-SERVER DATA
							if suppkey == 'client_to_server':
								print "\n\t[#]--------------------[CLIENT-->SERVER]---------------------------[#]\n"
								for cli_to_serverk, cli_to_serverv in suppvalue.iteritems():


									# DISPLAY CIPHERS
									if cli_to_serverk   == 'ciphers':
										print "\n\t\t[#]----------------------[CIPHERS]-----------------------[#]\n"
										for cipher in cli_to_serverv:
											print "\t\t[*]{}".format(cipher)
										print "\n\t\t[#]------------------------------------------------------[#]\n"


									# DISPLAY COMPRESSIONS
									elif cli_to_serverk == 'compressions':
										print "\n\t\t[#]--------------------[COMPRESSIONS]--------------------[#]\n"
										for compression in cli_to_serverv:
											print "\t\t[*]{}".format(compression)
										print "\n\t\t[#]------------------------------------------------------[#]\n"


									# DISPLAY MACS
									elif cli_to_serverk == 'macs':
										print "\n\t\t[#]------------------------[MACS]------------------------[#]\n"
										for macs in cli_to_serverv:
											print "\t\t[*]{}".format(macs)
										print "\n\t\t[#]------------------------------------------------------[#]\n"

								print "\n\t[#]-----------------------------------------------------------[#]\n"


							# DISPLAY HOST-KEY-ALGORITHMS
							elif suppkey == 'host_key_algorithms':
								print "\n\t[#]------------------------[HOST-KEY-ALG]------------------------[#]\n"
								for algorithm in suppvalue:
									print "\t[*]{}".format(algorithm)
								print "\n\t[#]--------------------------------------------------------------[#]\n"



							# DISPLAY KEX-ALGORITHMS
							elif suppkey == 'kex_algorithms':
								print "\n\t[#]--------------------------[KEX-ALG]---------------------------[#]\n"
								for algorithm in suppvalue:
									print "\t[*]{}".format(algorithm)
								print "\n\t[#]--------------------------------------------------------------[#]\n"



							# DISPLAY SERVER-TO-CLIENT DATA
							elif suppkey == 'server_to_client':
								print "\n\t[#]--------------------[SERVER-->CLIENT]-------------------------[#]\n"
								for cli_to_serverk, cli_to_serverv in suppvalue.iteritems():


									# DISPLAY CIPHERS
									if cli_to_serverk   == 'ciphers':
										print "\n\t\t[#]----------------------[CIPHERS]-----------------------[#]\n"
										for cipher in cli_to_serverv:
											print "\t\t[*]{}".format(cipher)
										print "\n\t\t[#]------------------------------------------------------[#]\n"



									# DISPLAY COMPRESSIONS
									elif cli_to_serverk == 'compressions':
										print "\n\t\t[#]--------------------[COMPRESSIONS]--------------------[#]\n"
										for compression in cli_to_serverv:
											print "\t\t[*]{}".format(compression)
										print "\n\t\t[#]------------------------------------------------------[#]\n"


									# DISPLAY MACS
									elif cli_to_serverk == 'macs':
										print "\n\t\t[#]------------------------[MACS]------------------------[#]\n"
										for macs in cli_to_serverv:
											print "\t\t[*]{}".format(macs)
										print "\n\t\t[#]------------------------------------------------------[#]\n"


								print "\n\t[#]--------------------------------------------------------------[#]\n"
			print "\n[#]-------------------------------------------------------------------[#]\n\n"



	for key1, value1 in target.iteritems():
		# DISPLAY THE LOCATION
		if key1   == 'location':
			print '\n[#]---------------------------[LOCATION]------------------------------[#]\n'
			for lock, locv in value1.iteritems():
				print "\t[*]{} : {}".format(lock, locv)
			print "\n[#]-------------------------------------------------------------------[#]\n"

		# DISPLAY THE AUTONOMOUS-SYSTEM
		elif key1 == 'autonomous_system':
			print '\n[#]-------------------------[AUTONOMOUS-SYSTEM]-----------------------[#]\n'
			for systemk, systemv in value1.iteritems():
				print "\t[*]{} : {}".format(systemk, systemv)
			print "\n[#]-------------------------------------------------------------------[#]\n"


		elif key1 == 'ip':
			print "\t[*]{} : {}".format(key1, value1)

		elif key1 == 'metadata':
			print "\t[*]{} : {}".format(key1, value1)

		elif key1 == "updated_at":
			print "\t[*]{} : {}".format(key1, value1)



def Host_Main():
	try:
		target = raw_input("[*] Target to get data from: ")
		result = get_result(target)
		# print json.dumps(result, indent=4, sort_keys=True)
		# write_info_to_file("109.230.239.93")
	except Exception as e:
		print e

	while True:
		print"\n\n"
		print "[1] Show data."
		print "[2] Write data to file (more data than showed)."
		print "[3] Exit.\n"
		target_search_choice = int(raw_input("($)> "))

		if target_search_choice 	== 3:
			os.system('cls')
			break

		elif target_search_choice   == 1:
			os.system('cls')
			target_data(result)

		elif target_search_choice 	== 2:
			os.system('cls')
			write_info_to_file(result)

		else:
			print "[!] Invalid option, please enter a valid one !"