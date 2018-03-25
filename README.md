# ShodaCensy

This is a tool that is written in python with the Shodan's API.
It is mainly focused to extract sensitive data from the Shodan's database for reconnaissance and to help you find what you are searching for.
## Features
#### Shodan
- [ 1 ] Exploit Search <br />
This feature is allowing you to search for known exploits based on your query(ex: apache,ssh).
The syntax of the query is the same as on the official Shodan's website. [Here](https://developer.shodan.io/api) is all the filters you can apply.
Currently, this feature only queries the ExploitDB and the MetasploitDB.
You can see the information of a specific exploit in the console, write the code to a file and see the code in the console.
- [ 2 ] Host Search <br />
This feature is allowing you to search for a specific ip address and get back usefull information.
You can see the data and write the data to a file, but take in consideration that the data is wrote to the file in json format.
- [ 3 ] Shodan Basic Search <br />
This feature is allowing you to search the Shodan database as you would on the site and see a summary of the potential devices that you are interested in. Also, you can see some more detailed information and write the html code to file if existing.
Besides that, it includes a facets search.
#### Censys
- [ 1 ] Host Search <br />
This feature is giving you the posibility to search for a specific ip address. Is likely the Shodan Host Search but with Censys you retrieve more information.
- [ 2 ] Censys Basic Search <br />
This feature will give you 1 page at a time with your specified query and some general information about the devices found. The query can contain the filters that are specified on their [official website](https://www.censys.io/overview#examples).

## What you need in order to run it?
#### Shodan
- A Shodan account and also an API key. You can create an account [here](https://account.shodan.io/register) and after you signed in, you can go [here](https://account.shodan.io/?language=en) to get your API key.
- You will also need to download the Shodan library for python. For that you can simply do a pip install:  ```pip install shodan```.
#### Censys
- A Censys account that will give you access to the [API ID](https://censys.io/account/api) and the [SECRET](https://censys.io/account/api). You can create an account [here](https://censys.io/register).
- You will also need to download the Censys library for python. For that you can simply do a pip install:  ```pip install censys```.

## Running it
After you cloned the repository, you just simply need to run the Shodax.py file as every other python script: ```python Shodax.py```. Now, you will get promped to enter your API ID, SECRET and API key. The first 2 are for Censys and the last is for Shodan. For the first 2, go to the official Censys website and click on [my account/API](https://censys.io/account/api). Just copy/paste those. After that, just go to the Shodans website and copy/paste the API key for your account. After you have entered you API ID, SECRET and API key, you will be promped in the main menu. Good job! Now you can start your searching!
Observation !!
Take in consideration that if you don't have a premium account, you can't use some of the filters and you have limited queries per day. More information can be found [here](https://censys.io/account/billing) and [here](https://developer.shodan.io/billing/signup).

## Bugs
This is project that I am stil working on, so if you find any bugs or have any ideas about new features and so on please brench, fork or just tell me about them.

## Upcoming features
- Streaming the Shodans Database
- Scanning with Shodan
- Checking if a host is a honeypot
- Adding more features with Censys.
