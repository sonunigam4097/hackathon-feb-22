from bs4 import BeautifulSoup

import re,requests


# handler = requests.session()


# url = 'https://google.com'

def isValidUrl(url):

    pattern = r"https?:\/\/.+\.[a-zA-Z]{2,4}"
    extract = re.findall(pattern,str(url))
    # print(extract)

    if extract:
        return extract[0]
    return None    



def getUrlResponses(urlist):
    # range1 = range(100,199)
    # range2 = range(200,299)
    # range3 = range(300,399)
    # range4 = range(400,499)
    # range5 = range(500,599)

    resplist = {
        "success":[],
        "fail":[],
        # "three":[],
        # "four":[],
        # "five":[],

    }


    for each in urlist:
        print(each)

        # sp =  requ
    # headers={"User-Agent":"Mozilla/5.0"}
        sp = requests.session()
        respcode = sp.get(each,headers={"User-Agent":"Mozilla/5.0","Accept-Language":"en-US"}).status_code
        sp.close()
        print(respcode)
        if respcode in range(200,399):
            resplist["success"].append(each)
        else:
            resplist["fail"].append(each)    
        # if respcode in range1 :
        #     list["one"].append(each)
        # elif respcode in range2 :
        #     list["two"].append(each)   
        # elif respcode in range3 :
        #     list["three"].append(each)   
        # elif respcode in range4 :
        #     list["four"].append(each)   
        # elif respcode in range5 :
        #     list["five"].append(each)                       

    return resplist



def fetchValidUrls(url):
    resp = requests.get(url)


    body = BeautifulSoup(resp.text,"html.parser")
    validurls = []
    for elem in body.findAll("a"):
        isvalidurl = isValidUrl(elem.get("href"))
        if isvalidurl is not None and len(validurls) < 5:
            validurls.append(isvalidurl)

    return validurls