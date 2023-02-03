import requests

from bs4 import BeautifulSoup

from func import *





# handler =  requests.session()


url ="https://google.co.in"
urlcollec = fetchValidUrls(url)        
urlresponses = getUrlResponses(urlcollec)

print(urlresponses)


# getUrlResponse(validurls)
# print(validurls)

# print(isValidUrl("https://sdag.com adsg"))



