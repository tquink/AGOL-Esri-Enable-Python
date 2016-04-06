import urllib
import json


def generateToken(username, password, portalUrl):
    '''Retrieves a token to be used with API requests.'''
    parameters = urllib.urlencode({'username' : username,'password' : password,'client' : 'referer','referer': portalUrl,'expiration': 60,'f' : 'json'})
    response = urllib.urlopen(portalUrl + '/sharing/rest/generateToken?', parameters).read()
    print portalUrl + '/sharing/rest/generateToken?', parameters
    try:
        jsonResponse = json.loads(response)
        if 'token' in jsonResponse:
            return jsonResponse['token']
        elif 'error' in jsonResponse:
            print jsonResponse['error']['message']
            for detail in jsonResponse['error']['details']:
                print detail
    except ValueError, e:
        print 'An unspecified error occurred.'
        print e

def getUsers(token, portalUrl, portalID):
	parameters = urllib.urlencode({'token' : token, 'f' : 'json', 'start' : 0, 'num' : 100})
	response = urllib.urlopen(portalUrl + '/sharing/rest/portals/'+portalID+'/users?', parameters).read()
	users = json.loads(response)
	return users

def updateUser(token, username, portalUrl):
	parameters = urllib.urlencode({'token' : token,'f' : 'json','userType': 'both'})
	response = urllib.urlopen(portalUrl + '/sharing/rest/community/users/'+username+'/update?', parameters).read()
	updatedEsri = json.loads(response)
	return updatedEsri

#### Replace the variables below with your admin username and password, AGOL URL, and AGOL ID from "My Organization"
username =  raw_input("Username: ") #<username>
password =  raw_input("Password: ") #<password>
portalURL = raw_input("Portal URL: ") #<portalurl>
portalID = raw_input("Portal ID: ") #<portalid>

token = generateToken(username, password, portalURL)
users = getUsers(token, portalURL, portalID)

for user in users['users']:
	if user['userType'] == 'arcgisonly':
		u = updateUser(token, user['username'], portalURL)
		if u['success'] == True:
			print user['username'], 'has been Esri enabled.'
		else: 
			print user['username'], 'has failed to update.'
