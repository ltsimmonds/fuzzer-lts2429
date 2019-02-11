import argparse
import requests
from bs4 import BeautifulSoup

#Method for obtaining te csrf token ("user_token") that prevents
#a successful login attempt.
def csrf(html_text):
    text = BeautifulSoup(html_text, "html.parser")
    user_token = text.find("input", {"type" : "hidden"})["value"]
    return user_token

#Handles the hardcoding of the "dvwa" string in the command prompt/
parser = argparse.ArgumentParser( \
    description="Fuzzer for determining a web application's insecurities.")
parser.add_argument( \
    "--custom-auth", help="For specifying a webapp to fuzz.", choices="dvwa", \
    dest="auth")
args = parser.parse_args()

s = requests.session()

#If the user entered "--custom-auth=dvwa" then he gets logged into the site.
if args.auth == "dvwa":
    s = requests.Session()
    url = "http://127.0.0.1:10000/dvwa/login.php"

    site = s.get(url).text
    login = s.post(url, data = {"username":"admin", "password":"password", \
        "Login":"Login", "user_token":csrf(site)})

    #Prints html information of the DVWA site
    print(login.text)
    
elif args.auth == None:
    #PART 2 of fuzzer project
    print("Part 2")
