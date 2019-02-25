import mechanicalsoup
import urllib
from urllib.parse import urlparse

#Crawls the given link to find more webpages
def link_discovery(browser, url_scheme, root_url):
    all_links = browser.get_current_page().find_all("a", href=True)
    good_links = []
    for link in all_links:
        if "http" not in link["href"] and len(link["href"]) > 1:
            good_links.append(url_scheme + "://" + root_url + \
            link["href"])
            
    return good_links

#Attempts to guess hidden pages from the given link using common words in
#hidden urls
def page_guessing(browser, text_file, root_url, url_scheme, links):
    url_types = [".php", ".htm", ".html", ".jsp"]
    words = []
    with open(text_file, "r") as file:
        for word in file:
            word = word.strip("\n")
            for extension in url_types:
                words.append(url_scheme + "://" + root_url + word + extension)

    pages = []
    for link in words:
        code = int(browser.open(link).status_code)
        if link not in links and code < 300:
            pages.append(link)

    return pages

#Obtains the request parameters (queries) from urls    
def parse_urls(root_url, urls):
    info = []
    for url in urls:
        if urlparse(url).query != "":
            info.append("Root: " + urlparse(url).scheme + "://" + root_url + \
                        "\tRequest " + "Parameter: " + urlparse(url).query)
    return info

#Displays the all information of a page's form parameters, if there are any
#parameters
def form_parameters(browser, links, root_url):
    params = []
    for link in links:
        page = browser.open(link)
        page_form = ""
        
        if browser.get_current_page().find_all("form") != []:
            form = browser.get_current_page().find("form")
            
            #Input field's "behavioral" info
            if form.has_attr("action"):
                page_form += "Link: " + link + "\nAction: " + \
                             form["action"]# + "\tMethod: " + form["method"]
                if form.has_attr("method"):
                    page_form += "\tMethod: " + form["method"]

                    #Input field's name
                    for form_input in browser.get_current_page().find_all("input"):
                        if form_input.has_attr("name"):
                            page_form += "\nInput Name: " + form_input["name"]

        if page_form != "":
            params.append(page_form + "\n")

    return params

#Displays the names and values of any cookies on the given link
def cookies(browser, root_url):
    cookies = []
    cookiejar = browser.get_cookiejar()
    for cookie in cookiejar:
        cookies.append("Name: " + cookie.name + ", Value: " + cookie.value)

    return cookies
