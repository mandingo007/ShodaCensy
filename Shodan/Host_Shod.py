import sys
import API
import os
import json

# Set the default encoding to UTF-8
reload(sys)
sys.setdefaultencoding("UTF-8")

def show_info(host):
    i = 0
    # Iterate over the items
    for key, value in host.iteritems():
        if key == 'data': # Check for key data
            for service in value: # Iterate over services
                print '\n[#]----------------------------[SERVICE {}]---------------------[#]\n'.format(i)
                for k, v in service.iteritems():
                    if k == 'html': # Check for html code
                        continue
                    elif k == 'ssl':
                        print "\n\t[#]-----------------------[SSL INFO]---------------------------[#]\n"
                        for sslkey, sslvalue in v.iteritems():
                            if sslkey == 'dhparams':
                                try:
                                    for k,v in sslvalue.iteritems():
                                        print '\t[*] {} : {}'.format(k, v)
                                except AttributeError:
                                    print "\t[!]The key have a value of None !"
                            elif sslkey == 'cert':
                                print '\n\t\t[#]--------------[CERTIFICATE INFO]---------------[#]\n'
                                for k,v in sslvalue.iteritems():
                                    print '\t\t[*] {} : {}'.format(k, v)
                                print "\n\t\t[#]---------------------------------------------[#]\n"
                        print "\n\t[#]--------------------------------------------------------[#]\n"
                    elif k == 'smb':
                        print "\n\t[#]-----------------------[SMB INFO]---------------------------[#]\n"
                        for smbkey, smbvalue in v.iteritems():
                            if smbkey == 'shares':
                                for item in smbvalue:
                                    for k, v in item.iteritems():
                                        print "\t[*] {} : {}".format(k, v)
                            elif smbkey == 'raw':
                                continue
                            else:
                                print "\t[*] {} : {}".format(smbkey, smbvalue)

                    # Displays optional info (key u'opt')
                    elif k == 'opts':
                        print "\n\t[#]-------------------[OPTIONAL INFO]-----------------[#]\n"
                        try:
                            for optk, optv in v.iteritems():
                                for opt1k, opt1v in optv.iteritems():
                                    if opt1k == 'kex':
                                        for hexk, hexv in opt1v.iteritems():
                                            print '\t[*] {} : {}'.format(hexk, hexv)
                                    else:
                                        print '\t[*] {} : {}'.format(opt1k, opt1v)
                        except Exception:
                            print 'None'
                        print "\n\t[#]---------------------------------------------------[#]\n"
                    # Displays shodan info (key u'_shodan')
                    elif k == '_shodan':
                        print "\n\t[#]-----------------------[SHODAN]--------------------[#]\n"
                        for sk, sv in v.iteritems():
                            print '\t[*] {} : {}'.format(sk, sv)
                        print "\n\t[#]---------------------------------------------------[#]\n"
                    # Displays location info (key u'location')
                    elif k == 'location':
                        print "\n\t[#]----------------------[LOCATION]-------------------[#]\n"
                        for lk, lv in v.iteritems():
                            print '\t[*] {} : {}'.format(lk, lv)
                        print "\n\t[#]---------------------------------------------------[#]\n"
                    # Displays http headers and info (key u'http')
                    elif k == 'http':
                        print "\n\t[#]-------------------------[HTTP]--------------------[#]\n"
                        for hk, hv in v.iteritems():
                            if hk == 'html':
                                continue
                            if hk  == 'components':
                                continue
                            # Displays components of the html page
                            try:
                                if hk == 'components':
                                    print "\n\t\t[#]--------------[COMPONENTS]---------------[#]\n"
                                    for ck, cv in hv.iteritems():
                                        print '\t\t[*] {} : {}'.format(ck, cv)
                                    print "\n\t\t[#]-----------------------------------------[#]\n"
                            except Exception:
                                print 'None'
                            print '\t[*] {} : {}'.format(hk, hv)
                        print "\n\t[#]---------------------------------------------------[#]\n"
                    # Displays ssh info
                    elif k == 'ssh':
                        print "\n\t[#]-------------------------[SSH]---------------------[#]\n"
                        try:
                            for sshk, sshv in v.iteritems():
                                if sshk == 'kex':
                                    for hexk, hexv in sshv.iteritems():
                                        print '\t[*] {} : {}'.format(hexk, hexv)
                                else:
                                    print '\t[*] {} : {}'.format(sshk, sshv)
                        except Exception:
                            print 'None'
                        print "\n\t[#]---------------------------------------------------[#]\n"
                    else:
                        print '\t[*] {} : {}'.format(k, v)
                i += 1
                print '\n'
            print '\n'
        else:
            print '[*] {} : {}'.format(key, value)
    print "##########################################################\n"

def data_to_file(host):
    filename = raw_input("[+] Enter the name of the file you want to save data on: ")
    print "[+] Writing to file..."
    try:
        with open(filename, 'w') as f:
            json.dump(host, f, indent=4, sort_keys=True)
            print "[+] Done! You can see your data in the {} file.".format(filename)
    except Exception as e:
        print "[!] Something went wrong couldn't write to file..."

def Host_Main():
    print """\n\n
     /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$$        /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
    | $$  | $$ /$$__  $$ /$$__  $$|__  $$__/       /$$__  $$| $$_____/ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$
    | $$  | $$| $$  \ $$| $$  \__/   | $$         | $$  \__/| $$      | $$  \ $$| $$  \ $$| $$  \__/| $$  | $$
    | $$$$$$$$| $$  | $$|  $$$$$$    | $$         |  $$$$$$ | $$$$$   | $$$$$$$$| $$$$$$$/| $$      | $$$$$$$$
    | $$__  $$| $$  | $$ \____  $$   | $$          \____  $$| $$__/   | $$__  $$| $$__  $$| $$      | $$__  $$
    | $$  | $$| $$  | $$ /$$  \ $$   | $$          /$$  \ $$| $$      | $$  | $$| $$  \ $$| $$    $$| $$  | $$
    | $$  | $$|  $$$$$$/|  $$$$$$/   | $$         |  $$$$$$/| $$$$$$$$| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$
    |__/  |__/ \______/  \______/    |__/          \______/ |________/|__/  |__/|__/  |__/ \______/ |__/  |__/
\n\n"""
    try:
        host = raw_input("[+] Enter the host you want information on: ")
        print "[+] Getting data for the ip..."
        result = API.api.host(host)

        while True:
            print "\n[1] Show data."
            print "[2] Write data to file (get more information than showed)."
            print "[3] Quit"
            choice = int(raw_input("($)> "))

            if choice == 3:
                os.system('cls')
                break
            elif choice == 1:
                os.system('cls')
                show_info(result)
            elif choice == 2:
                os.system('cls')
                data_to_file(result)

    except Exception:
        print "[!] Host could't be found!\n"
