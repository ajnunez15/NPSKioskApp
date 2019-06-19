import requests
import json
import os

alerts = None
articles = None
campgrounds = None
events = None
lessonPlans = None
newsReleases = None
parks = None
people = None
places = None
visitorCenters = None

#api_token = os.getenv("APIKEY") reads APIKEY from .env locally
api_token = os.environ['APIKEY']
print(api_token)
headers = {'X-Api-Key': api_token}

def getAlerts(alerts):
    if(alerts is None):
        api_url_base = 'https://developer.nps.gov/api/v1/alerts'
        response = requests.get(api_url_base, headers=headers)

        if(response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Alerts] failed")
            return None
    return alerts

def queryAlerts(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/alerts?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodeAlerts(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/alerts?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getArticles(articles):
    if (articles is None):
        api_url_base = 'https://developer.nps.gov/api/v1/articles'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Articles] failed")
            return None
    return articles

def queryArticles(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/articles?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodeArticles(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/articles?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getCampgrounds(campgrounds):
    if (campgrounds is None):
        api_url_base = 'https://developer.nps.gov/api/v1/campgrounds'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Campgrounds] failed")
            return None
    return campgrounds

def queryCampgrounds(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/campgrounds?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getEvents(events):
    if (events is None):
        api_url_base = 'https://developer.nps.gov/api/v1/events'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Events] failed")
            return None
    return events

def queryEvents(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/events?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodeEvents(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/events?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getLessonPlans(lessonsPlans):
    if (lessonPlans is None):
        api_url_base = 'https://developer.nps.gov/api/v1/lessonplans'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Lesson Plans] failed")
            return None
    return lessonPlans

def queryLessonplans(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/lessonplans?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodeLessonplans(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/lessonplans?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getNewsReleases(newsReleases):
    if (newsReleases is None):
        api_url_base = 'https://developer.nps.gov/api/v1/newsreleases'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [News Releases] failed")
            return None
    return newsReleases

def queryNewsreleases(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/newsreleases?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodeNewsreleases(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/newsreleases?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getParks(parks):
    if (parks is None):
        api_url_base = 'https://developer.nps.gov/api/v1/parks'
        response = requests.get(api_url_base, headers=headers)
        print(response)
        print(response.status_code)
        print(response.headers)
        print(response.encoding)
        print(response.text)
        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Parks] failed")
            return None
    return parks

def queryParks(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/parks?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None


def getPeople(people):
    if (people is None):
        api_url_base = 'https://developer.nps.gov/api/v1/people'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [people] failed")
            return None
    return people

def queryPeople(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/people?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodePeople(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/people?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getPlaces(places):
    if (places is None):
        api_url_base = 'https://developer.nps.gov/api/v1/places'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [places] failed")
            return None
    return places

def queryPlaces(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/places?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def parkCodePlaces(parkCode):
    q = parkCode
    api_url_base = 'https://developer.nps.gov/api/v1/places?parkCode='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

def getVisitorCenters(visitorCenters):
    if (visitorCenters is None):
        api_url_base = 'https://developer.nps.gov/api/v1/visitorcenters'
        response = requests.get(api_url_base, headers=headers)

        if (response.status_code == 200):
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Requesting [Visitor Centers] failed")
            return None
    return visitorCenters

def queryVisitorcenters(queryString):
    q = queryString
    api_url_base = 'https://developer.nps.gov/api/v1/visitorcenters?q='
    response = requests.get(api_url_base+q,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        print("Querying failed")
        return None

#alerts = getAlerts(alerts)
#print("Retrieved [Alerts]")
#articles = getAlerts(articles)
##print("Retrieved [Articles]")
#campgrounds = getCampgrounds(campgrounds)
#print("Retrieved [Campgrounds]")
#events = getEvents(events)
#print("Retrieved [Events]")
#lessonPlans = getLessonPlans(lessonPlans)
#print("Retrieved [Lesson Plans]")
#newsReleases = getNewsReleases(newsReleases)
#print("Retrieved [News Releases]")
parks = getParks(parks)
#print("Retrieved [Parks]")
#people = getPeople(people)
#print("Retrieved [People]")
#visitorCenters = getVisitorCenters(visitorCenters)
#print("Retrieved [Visitor Centers]")