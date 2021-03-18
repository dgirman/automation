# climacell api = 'kbZYTPGO6Xkw7EILNavbHZq20Ghfr4id'

import requests
import urllib.request
import json
from types import SimpleNamespace

#loads(param) is a function that converts a text string into a json object.
#dumps(param) is a function that converts a json data object into a text string. 
GETUPDATE = True
#GETUPDATE = False

if GETUPDATE:
    mkey = "kbZYTPGO6Xkw7EILNavbHZq20Ghfr4id"
    mlat ='37.305470'
    mlon='-121.935920'
    mlat ='37.180211'
    mlon = '-122.014821'

    mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType,particulateMatter25,particulateMatter10,pollutantO3,pollutantNO2,pollutantCO,pollutantSO2,epaIndex,epaPrimaryPollutant,epaHealthConcern,fireIndex"
    mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType"

    mtimesteps = '&timesteps=1d'

    murl = 'https://data.climacell.co/v4/timelines?location=' + mlat +','+ mlon + mfields + mtimesteps + '&units=metric&apikey=' + mkey



    home_id = 'location=60523c43f3a5600007047e6a'
    murl2 = 'https://data.climacell.co/v4/timelines?location=60523c43f3a5600007047e6a'+ '&fields=temperature,humidity&timesteps=current&units=Imperial&apikey=' + mkey

    murl3 = "https://data.climacell.co/v4/locations/locationId" +'&apikey=' + mkey


    #r = requests.get(murl)
    response = urllib.request.urlopen(murl)
    str_response = response.read().decode('utf-8')
    obj = json.loads(str_response)


    with open("data_file.json", "w") as write_file:
        json.dump(obj, write_file)
else:
    
    f = open("data_file.json", "r")
    obj = f.read()
    obj = json.loads(obj)
    
x=(obj["data"]["timelines"])

readings_dictionary = {}
list_results=[]
print(type(x)) #list
print(len(x))  #1

for i in range(len(x)):
    #print(type(x[i]))  #dict
    #print(len(x[i]))   #4 

    #print(type(x[i]['intervals']))   #list
    #print(x[i]['intervals'])

    l2 = x[i]['intervals']
    #print(l2)

    #print(len(l2))    #15
    #print('\n\n')
    for ii in range(len(l2)):
        #print(type(l2[ii]))
        #print(len(l2[ii]))

        #print(l2[ii])
        #print(l2[ii]['startTime'])
        #print(type(l2[ii]['startTime']))

        #print(l2[ii]['values'])
        #print(type(l2[ii]['values']))
        lll = l2[ii]['values']

        #print(l2[ii]['values']['temperature'])
        #print(type(l2[ii]['values']['temperature']))

        readings_dictionary= {}
        readings_dictionary['rtime'] = l2[ii]['startTime']
        for reading,rvalue in lll.items():
            #print(reading,":", rvalue)
            readings_dictionary[reading] = rvalue
        print(readings_dictionary)
        list_results.append(readings_dictionary)
print(list_results)
print(list_results[0]['rtime'])
print(list_results[10]['temperature'])

