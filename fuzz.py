import argparse
import mechanicalsoup
import discover
from urllib.parse import urlparse
from urllib.parse import urlsplit

#Handles the arguments of the command prompt entry
parser = argparse.ArgumentParser( \
    description="Fuzzer for determining a web application's insecurities.")
parser.add_argument(\
    "commands", help="Either 'discover' or 'test', to specify the fuzzer's" +
    "use.")
parser.add_argument(\
    "url", help="A required root to a web application for fuzz testing.")
parser.add_argument( \
    "--custom-auth", help="For specifying a webapp to fuzz.", dest = "auth")
parser.add_argument(\
    "--common-words", metavar= "file", help="A .txt file that contains a" + \
    "list of common words to check a web application for, when using the" + \
    "fuzzer to 'discover'", dest = "common_words")
args = parser.parse_args()

#Given a url (and the DVWA specification to login), this method takes
#the user to the url provided, and provides an informative output of the
#fuzzer's discoveries( and tests.)
def authenticate():
    browser = mechanicalsoup.StatefulBrowser(
        soup_config = {"features" : "lxml"})
    url = args.url

    print("\nFor this url: " + url)

    if args.auth == "dvwa":
        url = "http://127.0.0.1:10000/dvwa/login.php"
        browser.open(url)

        browser.select_form("form")
        browser["username"] = "admin"
        browser["password"] = "password"
        browser.submit_selected()

        path = urlsplit(url).path.split("/")
        root_url = urlsplit(url).netloc + "/" + path[1] +"/"
        url_scheme = urlsplit(url).scheme
        
    else:
        browser.open(url)

        path = urlsplit(url).path.split("/")
        root_url = urlsplit(url).netloc + "/"
        url_scheme = urlsplit(url).scheme

    #print(browser.get_current_page())

    links = [url]
    if args.commands == "discover":
        #Outputs the links discovery from the root page
        discovered_links = discover.link_discovery(browser, url_scheme, root_url)
        print("\n\nLinks Discovered: ")
        for link in discovered_links:
            links.append(link)
            print(link)

        #Outputs the pages guessed from a .txt file of common words
        file = args.common_words
        guesses = discover.page_guessing(browser, file, root_url, url_scheme, links)
        print("\n\nPages Guessed: ")
        for guess in guesses:
            if guess not in links:
                links.append(guess)
                print(guess)

        #Outputs the root and request parameters of all links discovered or
        #guessed that contain at least one request parameter in the url
        print("\n\nUrl Request Info:")
        url_info = discover.parse_urls(root_url, links)
        for url in url_info:
            print(url)

        #Outputs the all of the input parameters and the associated attributes
        #of the parameters for all of the dicovered and guessed links
        form_params = discover.form_parameters(browser, links, root_url)
        print("\n\nForm Parameters: ")
        for param in form_params:
            print(param)

        #Outputs the name and value of any cookies in the web application
        cookies = discover.cookies(browser, root_url)
        print("\nCookies: ")
        for cookie in cookies:
            print(cookie)
        
authenticate()
