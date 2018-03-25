import shodan

def createAPI():
    API_KEY = raw_input('Enter yout API key: ')
    api = shodan.Shodan(API_KEY)
    return api

api = createAPI()
