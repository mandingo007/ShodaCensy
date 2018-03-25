import shodan
import os
import API
import sys

# Set the default encoding to UTF-8
reload(sys)
sys.setdefaultencoding("UTF-8")


#------------------------------------[DISPLAY FUNCTIONS]------------------------------------#

# Display the results to choose from 
def show_results(results):
    #os.system('cls')
    i = 1
    print "[#]------------------[RESULTS]------------------[#]\n\n"
    for result in results['matches']:
        print "[#]-----------[{}]-----------[#]\n".format(i)
        print "\tLOCATION: {}\n\tISP: {}\n\tIP: {}".format(result['location']['country_name'], result['isp'], result['ip_str'])
        print "\n[#]------------------------[#]\n"
        i += 1


# Display info for the specific device
def show_info(device_number, results):
    print "##########################################################\n"
    device = results_glob['matches'][device_number] # Get the device selected
    # Start displaying info about it
    for key, value in device.iteritems():
        # Display location data
        if key == 'location':
            print '[#]-----------[LOCATION]-----------[#]'
            for k, v in value.iteritems():
                print '[*] {} : {}'.format(k, v)
            print '[#]--------------------------------[#]\n'
        # Display http data
        elif key == 'http':
            print '[#]-----------[HTTP INFO]-----------[#]'
            for k, v in value.iteritems():
                if k == 'html':
                    continue
                print '[*] {} : {}'.format(k, v)
            print '[#]---------------------------------[#]\n'
        # Display ssh data
        elif key == 'ssh':
            print '[#]-----------[LOCATION]-----------[#]'
            for k, v in value.iteritems():
                print '[*] {} : {}'.format(k, v)
            print '[#]--------------------------------[#]\n'
        # Display shodan data
        elif key == '_shodan':
            print '[#]-----------[SHODAN INFO]-----------[#]'
            for k, v in value.iteritems():
                print '[*] {} : {}'.format(k, v)
            print '[#]-----------------------------------[#]\n'
        # Display regular data
        else:
            print "[*] {} : {}\n".format(key, value)
    print "##########################################################\n"


#------------------------------------[-S ARGUMENT]------------------------------------#

# Preparing for the normal search and features
results_glob = ''
count = 0
def normal_search(query = ''):
    global count
    global results_glob
    if count < 1:
        print "[+] Searching for your query..."
        results = API.api.search(query) # Search Shodan
        results_glob = results
        count += 1
    while True:
        show_results(results_glob) # Display list where you can decide what to do next
        print "[+] Enter 0 to go to main menu."
        try:
            dev_num = int(raw_input("[+] Enter the number of device: "))
            if dev_num == 0:
               break
            else:
                device_choice(dev_num, results_glob) # Go to 2nd menu
                break
        except ValueError:
            os.system('cls')
            print "[!] Enter a valid option please !"




# Second menu for the -S choice
def device_choice(device_number, results):
    # Begin 2nd menu
    while True:
        print '\n[1] Get html code to file.'
        print '[2] General Information.'
        print '[3] Go back to choose another device.\n'

        try:
            choice = int(raw_input('($)> '))
            os.system('cls')
            if choice == 1:
                try:
                    filename = raw_input('[+] Enter the filename: ')
                    data     = results_glob['matches'][device_number] # Get the device object
                    htmlcode = ""
                    # Iterate over items in devie
                    for key, value in data.iteritems():
                        if key == 'http': # Check for http key
                            for k, v in value.iteritems():
                                if k == 'html': # Check for html key
                                    htmlcode += v # Store html code
                    try:
                        with open(filename, 'w') as outf:
                            outf.write(htmlcode) # Write the html code to file
                            outf.close() # Close the file
                        print '[+] Done you can see the html code in the {} file.'.format(filename)
                    except TypeError:
                        print "[!] Something went wrong and the code couldn't be saved to file !"
                except Exception:
                    print "[!] Enter a valid command please !" 
            elif choice == 2:
                show_info(device_number, results_glob) # Display info about device
            elif choice == 3:
                normal_search()
                break
        except ValueError:
            print "[!] Enter a valid option please !"

#------------------------------------[-F ARGUMENT]------------------------------------#

def facets_search(query):
    # The list of properties we want summary information on
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',

        # We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
        # default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 3),
    ]

    FACET_TITLES = {
        'org': '[#]-----Top 5 Organizations-----[#]',
        'domain': '[#]-----Top 5 Domains-----[#]',
        'port': '[#]-----Top 5 Ports-----[#]',
        'asn': '[#]-----Top 5 Autonomous Systems-----[#]',
        'country': '[#]-----Top 3 Countries-----[#]',
    }
    try:
        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        print "[+] Searching for your query..."
        result = API.api.count(query, facets=FACETS)
        os.system('cls')
        print '[*] Shodan Summary Information'
        print '[*] Query: %s' % query
        print '[*] Total Results: %s\n' % result['total']

        # Print the summary info from the facets
        for facet in result['facets']:
            print FACET_TITLES[facet]

            for term in result['facets'][facet]:
                print '[*] %s: %s' % (term['value'], term['count'])

            # Print an empty line between summary info
            print ''
        print "##########################################################\n"

    except Exception, e:
        print 'Error: %s' % e


def Shodan_Search_Main():
    while True:
        print """\n\n
      /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$        /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
     /$$__  $$| $$  | $$ /$$__  $$| $$__  $$ /$$__  $$| $$$ | $$       /$$__  $$| $$_____/ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$
    | $$  \__/| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$| $$      | $$  \__/| $$      | $$  \ $$| $$  \ $$| $$  \__/| $$  | $$
    |  $$$$$$ | $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$$| $$ $$ $$      |  $$$$$$ | $$$$$   | $$$$$$$$| $$$$$$$/| $$      | $$$$$$$$
     \____  $$| $$__  $$| $$  | $$| $$  | $$| $$__  $$| $$  $$$$       \____  $$| $$__/   | $$__  $$| $$__  $$| $$      | $$__  $$
     /$$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$\  $$$       /$$  \ $$| $$      | $$  | $$| $$  \ $$| $$    $$| $$  | $$
    |  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/| $$  | $$| $$ \  $$      |  $$$$$$/| $$$$$$$$| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$
     \______/ |__/  |__/ \______/ |_______/ |__/  |__/|__/  \__/       \______/ |________/|__/  |__/|__/  |__/ \______/ |__/  |__/
 \n\n"""
        # Display main menu
        print "[#]-------------[INFO]------------[#]\n"
        print "   [S]earch basic query."
        print "   [F]acets query(summary info)."
        print "   [Q]uit."
        print "\n[#]------------------------------[#]\n"

        # Get the first choice
        choice = raw_input('($)>')
        choice = choice.split(' ')

        # Setup variables
        bsearch = ''
        qtags = ''
        qfacets = ''
        exit = ''

        # Check for arguments
        for c in choice:
            if c == 'S':
                bsearch = c
            if c == 'F':
                qfacets = c
            if c == 'Q':
                exit = c

        # Logic for arguments
        if exit:
            os.system('cls')
            break
        if bsearch:
            try:
                query = raw_input('[+] Enter your query: ')
                normal_search(query) # Normal search
            except Exception:
                print "[!] Enter a valid query please !"
        if qfacets:
            try:
                query = raw_input('[+] Enter your query: ')
                facets_search(query)
            except Exception:
                print "[!] Enter a valid query please !"


# API = createAPI()
# Shodan_Search_Main()
