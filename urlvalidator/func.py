from bs4 import BeautifulSoup

import re,requests





url = 'https://google.com'

def isValidUrl(url):

    pattern = r"https?:\/\/.+\.[a-zA-Z]{2,3}"
    extract = re.findall(pattern,url)
    # print(extract)

    if extract:
        return extract[0]
    return None    



def getUrlResponses(urlist):
    range1 = range(100,199)
    range2 = range(200,299)
    range3 = range(300,399)
    range4 = range(400,499)
    range5 = range(500,599)

    list = {
        "one":[],
        "two":[],
        "three":[],
        "four":[],
        "five":[],

    }

    for each in urlist:
        respcode = requests.get(each).status_code
        if respcode in range1 :
            list["one"].append(each)
        elif respcode in range2 :
            list["two"].append(each)   
        elif respcode in range3 :
            list["three"].append(each)   
        elif respcode in range4 :
            list["four"].append(each)   
        elif respcode in range5 :
            list["four"].append(each)                       

    return list



def fetchValidUrls(url):
    resp = requests.get(url)


    body = BeautifulSoup(resp.text,"html.parser")
    validurls = []
    for elem in body.findAll("a"):
        isvalidurl = isValidUrl(elem.get("href"))
        if isvalidurl is not None:
            validurls.append(isvalidurl)

    return validurls