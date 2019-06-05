from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .data import alerts, articles, campgrounds, events, lessonPlans
from .data import newsReleases, parks, people, places, visitorCenters
from .data import queryParks, queryAlerts, queryArticles, queryCampgrounds, queryEvents
from .data import queryLessonplans, queryNewsreleases, queryPeople, queryPlaces, queryVisitorcenters
from .data import parkCodeAlerts, parkCodeArticles, parkCodeEvents, parkCodeNewsreleases, parkCodeLessonplans
from .data import parkCodePeople, parkCodePlaces
from .forms import HomeForm
from pprint import pprint

#pprint(campgrounds)
states = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado",
          "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho",
          "Illinois",
          "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
          "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
          "Puerto Rico",
          "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
          "Vermont", "Virgin Islands", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

statesAbbrev = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU",
                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC",
                "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA", "WV", "WI", "WY"]

def handler404(request, exception):
    form = HomeForm
    context = {
        'form': form
    }
    return render(request, 'Errors/404.html', context, status=404)

def handler500(request):
    form = HomeForm
    context = {
        'form': form
    }
    return render(request, 'Errors/500.html', context, status=500)

def home(request):
    form = HomeForm()
    #print("Total Parks: ", parks['total'], parks['limit'])
    parksData = parks['data']

    #Oddly when retrieving data from the api by state, we are only given a list of 51 parks.
    #Only 5 of them are National Parks.
    #However, if you look up let us National Park through our website search bar, you would get about 89 results from
    #the api as the search bar uses the query function from api.
    '''count = 0
    for park in parksData:
        if(park['designation'] == "National Park"):
            print(park['states'], park['fullName'])
            count=count+1
    print(count)'''

    statesLowAbbrev = [x.lower() for x in statesAbbrev]
    zipped = zip(statesLowAbbrev, states)

    context = {
        'form': form,
        'zipped': zipped,
        'parksData': parksData
    }
    return render(request, 'NPSKiosk/index.html', context)

def query(request):
    form = HomeForm(request.POST)
    text = ''
    alertSearchData = []
    articleSearchData = []
    campgroundSearchData = []
    eventSearchData = []
    lessonplanSearchData = []
    newsreleaseSearchData = []
    parkSearchData = []
    peopleSearchData = []
    placeSearchData = []
    visitorcenterSearchData = []

    totalSearchAlerts = 0
    totalSearchArticles = 0
    totalSearchCampgrounds = 0
    totalSearchEvents = 0
    totalSearchLessonplans = 0
    totalSearchNewsreleases = 0
    totalSearchParks = 0
    totalSearchPeople = 0
    totalSearchPlaces = 0
    totalSearchVisitorceters = 0

    if(form.is_valid()):
        text = form.cleaned_data['search']

        alertResults = queryAlerts(text)
        totalSearchAlerts = alertResults['total']
        alertSearchData = alertResults['data']

        articleResults = queryArticles(text)
        totalSearchArticles = articleResults['total']
        articleSearchData = articleResults['data']

        campgroundResults = queryCampgrounds(text)
        totalSearchCampgrounds = campgroundResults['total']
        campgroundSearchData = campgroundResults['data']

        eventResults = queryEvents(text)
        totalSearchEvents = eventResults['total']
        eventSearchData = eventResults['data']

        lessonplanResults = queryLessonplans(text)
        totalSearchLessonplans = lessonplanResults['total']
        lessonplanSearchData = lessonplanResults['data']

        newsreleaseResults = queryNewsreleases(text)
        totalSearchNewsreleases = newsreleaseResults['total']
        newsreleaseSearchData = newsreleaseResults['data']

        parkResults = queryParks(text)
        totalSearchParks = parkResults['total']
        parkSearchData = parkResults['data']

        peopleResults = queryPeople(text)
        totalSearchPeople = peopleResults['total']
        peopleSearchData = peopleResults['data']

        placeResults = queryPlaces(text)
        totalSearchPlaces = placeResults['total']
        placeSearchData = placeResults['data']

        visitorcentersResults = queryVisitorcenters(text)
        totalSearchVisitorceters = visitorcentersResults['total']
        visitorcenterSearchData = visitorcentersResults['data']
        pprint(visitorcenterSearchData)

    form = HomeForm()

    context = {
        'form': form,
        'text': text,

        'alertSearchData': alertSearchData,
        'totalSearchAlerts': totalSearchAlerts,

        'articleSearchData': articleSearchData,
        'totalSearchArticles': totalSearchArticles,

        'totalSearchCampgrounds': totalSearchCampgrounds,
        'campgroundSearchData': campgroundSearchData,

        'totalSearchEvents': totalSearchEvents,
        'eventSearchData': eventSearchData,

        'totalSearchLessonplans': totalSearchLessonplans,
        'lessonplanSearchData': lessonplanSearchData,

        'totalSearchNewsreleases': totalSearchNewsreleases,
        'newsreleaseSearchData': newsreleaseSearchData,

        'parkSearchData': parkSearchData,
        'totalSearchParks': totalSearchParks,

        'totalSearchPeople': totalSearchPeople,
        'peopleSearchData': peopleSearchData,

        'totalSearchPlaces': totalSearchPlaces,
        'placeSearchData': placeSearchData,

        'totalSearchVisitorcenters': totalSearchVisitorceters,
        'visitorcenterSearchData': visitorcenterSearchData
    }
    return render(request, 'NPSKiosk/query.html', context)

def state(request, stateCode):
    form = HomeForm()

    stateCodeUpper = stateCode.upper()
    statesLowAbbrev = [x.lower() for x in statesAbbrev]
    # check first to make sure state arg is valid code else throw error code
    state = states[statesLowAbbrev.index(stateCode)]
    parksData = parks['data']
    print("Total Parks: ", parks['total'], parks['limit'])
    count = 0
    for park in parksData:
        print(park['fullName'])
        count = count+1
    print("Count is ", count)
    pprint(parks)
    #Park by State---------
    parksByState = []
    for park in parksData:
        #print(stateCodeUpper, " in ", park['states'])
        if(stateCodeUpper in park['states']):
            parksByState.append(park)

    if(len(parksByState) == 0):
        parksByState = None
    #print(parksByState)
    #search = queryParks('Martin Luther')
    #print(search)
    #-----------

    context = {
        'form': form,
        'state': state,
        'stateCodeUpper': stateCodeUpper,
        'parksByState': parksByState
    }
    return render(request, 'NPSKiosk/state.html', context)

def selected_destination(request, parkCode):
    '''form = HomeForm(request.POST)
    if(form.is_valid()):
        return query(request)'''
    form = HomeForm()

    #Find park with that park code
    destParkData = []
    parksData = parks['data']
    for park in parksData:
        if(park['parkCode'] == parkCode):
            destParkData = park

    #Get all alerts, articles, events, and news releases related to this selected park
    destAlerts = parkCodeAlerts(parkCode)
    destArticles = parkCodeArticles(parkCode)
    destEvents = parkCodeEvents(parkCode)
    destNewsreleases = parkCodeNewsreleases(parkCode)
    destLessonplans = parkCodeLessonplans(parkCode)
    destPeople = parkCodePeople(parkCode)
    destPlaces = parkCodePlaces(parkCode)
    pprint(destNewsreleases)
    context = {
        'form': form,
        'destParkData': destParkData,
        'destAlerts': destAlerts,
        'destArticles': destArticles,
        'destEvents': destEvents,
        'destNewsreleases': destNewsreleases,
        'destLessonplans': destLessonplans,
        'destPeople': destPeople,
        'destPlaces': destPlaces
    }
    return render(request, 'NPSKiosk/destination.html', context)
