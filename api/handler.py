import requests
import json
import os

BASEURL = "https://sxcu.net/api/"

def getAllDomains():
    return requests.get(BASEURL + "subdomains").json()

def getDomains(allDomains):
    domains = []
    for domain in allDomains:
        if domain["public"] and domain["domain"].count(".") == 1 and domain["domain"] != "sxcu.net":
            domains.append(domain["domain"])

    return domains

def checkDomain(check, allDomains):
    for domain in allDomains:
        if domain["domain"] == check:
            if domain["public"]:
                return True
    return False

def checkFile(filePath):
    if not filePath.endswith("png") or filePath.endswith("jpeg") or filePath.endswith("jpg"):
        return False
    if os.path.getsize(filePath) > 0x5F00000:
        return False
    return True

def checkSub(domain):
    return requests.get(BASEURL + "subdomains/check/" + domain).json()["exists"]

def checkSubPublic(domain):
    return requests.get(BASEURL + "subdomains/" + domain).json()["public"]

def uploadHandler(domain, filePath, token=""):

    print(domain)
    print(filePath)

    props = {
        "discord_hide_url": False
	}

    response = requests.post(domain + "api/files/create", files={"file": open(filePath, "rb").read()}, data={
        "token": token,
        "collection_token":"",
        "noembed": True,
        "og_properties" : json.dumps(props)

    })

    return response.json()

def deleteHandler(url):
    return requests.get(url).json()