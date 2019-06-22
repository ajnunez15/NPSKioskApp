# NPSKiosk Web App
National Park Services Kiosk for Capital One MindSumo 2019 Challenge. Submission for the second round of the Capital One Software Engineering Summit. The challenge can be found [here](https://www.mindsumo.com/contests/national-park-api).

The final project can be found [here](https://npskiosk.herokuapp.com).

## List of Frameworks and APIs used
* [Django](https://www.djangoproject.com/) for backend
* [Bootstrap](https://getbootstrap.com/) for frontend
* [NPS API](https://www.nps.gov/subjects/developer/get-started.htm) to access National Park Services API
* [Requests](http://docs.python-requests.org/en/master/) to issue GET requests to other HTML pages

## Overview of each feature
### Required features
#### Keyword Search
* Tool to assist users in finding specific information, such as state and designation filtering, name and keyword search. Feauture would attempt to find all of the data that matches the keyword. This is useful for when Users know what to look for specifically.

#### Search destination by State
* Allows Users to look for a destination by states of interests and shows information on a selected destination along with any lesson plan available for the selected destination.

#### Search destination by Park  
* Quickly allows a user to find all the information they need with the name of the destination from the main menu.

## Challenges
* NPS API failed to request all 500 parks available in the database. This affects functionality since not all parks could be found through the main menu. This is why for some states it displays no destinations found. If NPS API can retrieve all of the data, app will work as normal without further changes. This limitation restricted me from being able to play with all of the data possible. 
* Majority of the challenges were faced with frontend and how to get the markup and CSS formatted to enhance UI.
