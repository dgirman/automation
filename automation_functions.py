import requests
import urllib.request
import json
from datetime import datetime
from dateutil import tz
import zulu 

class ClimacellData:
    """
    Get and manage Climacell data
    """
    def __init__(self):
        self.my_data_exist = False
        self.my_data = ''
        self.my_data_duration = '' 
        self.my_results = []
        self.my_lat = ''
        self.my_lon = ''

    def GetNewData(self,get_new_data_flag=False,mkey="kbZYTPGO6Xkw7EILNavbHZq20Ghfr4id",mlat='37.305470',mlon='-121.935920',mlocid='60523c43f3a5600007047e6a',mtimesteps='&timesteps=1d',munits='&units=imperial'):
        self.my_data_duration = mtimesteps
        self.my_lat = mlat
        self.my_lon = mlon

        #  print(self.my_data_duration)
        if self.my_data_duration == '&timesteps=1d':
            #mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType,particulateMatter25,particulateMatter10,pollutantO3,pollutantNO2,pollutantCO,pollutantSO2,epaIndex,epaPrimaryPollutant,epaHealthConcern,fireIndex"
            mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType"
 
        elif self.my_data_duration == '&timesteps=1h':
            #mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType,particulateMatter25,particulateMatter10,pollutantO3,pollutantNO2,pollutantCO,pollutantSO2,epaIndex,epaPrimaryPollutant,epaHealthConcern,fireIndex"
            mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType,particulateMatter25,particulateMatter10,pollutantO3,pollutantNO2,pollutantCO,pollutantSO2,epaIndex,epaPrimaryPollutant,epaHealthConcern,fireIndex"

        elif self.my_data_duration == '&timesteps=current':
            mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType"
            mfields = "&fields=temperature,humidity,pressureSurfaceLevel,visibility,windSpeed,windDirection,precipitationProbability,precipitationType,particulateMatter25,particulateMatter10,pollutantO3,pollutantNO2,pollutantCO,pollutantSO2,epaIndex,epaPrimaryPollutant,epaHealthConcern,fireIndex"

        else:
            print("my_data_duration value is unknown")
            return

        murl = 'https://data.climacell.co/v4/timelines?location=' + mlat +','+ mlon + mfields + mtimesteps + munits + '&apikey=' + mkey
        
        murl2 = 'https://data.climacell.co/v4/timelines?location=60523c43f3a5600007047e6a'+ '&fields=temperature,humidity&timesteps=current&units=Imperial&apikey=' + mkey
        murl3 = "https://data.climacell.co/v4/locations/locationId" +'&apikey=' + mkey
        self.mydata_exist = True

        if get_new_data_flag:
            response = urllib.request.urlopen(murl)
            str_response = response.read().decode('utf-8')
            obj = json.loads(str_response)

            if self.my_data_duration == '&timesteps=1d':
                with open("data_file_1d_days.json", "w") as write_file:
                    json.dump(obj, write_file)
            if self.my_data_duration == '&timesteps=current':
                with open("data_file_current_day.json", "w") as write_file:
                    json.dump(obj, write_file)
            if self.my_data_duration == '&timesteps=1h':
                with open("data_file_1h_days.json", "w") as write_file:
                    json.dump(obj, write_file)
        else:
            if self.my_data_duration == '&timesteps=1d':
                f = open("data_file_1d_days.json", "r")
            if self.my_data_duration == '&timesteps=current':
                f = open("data_file_current_day.json", "r")
            if self.my_data_duration == '&timesteps=1h':
                f = open("data_file_1h_days.json", "r")

            obj = f.read()
            obj = json.loads(obj)
        
        '''
        print(self.my_data_duration + '\n')    
        print(obj)
        print('\n\n' +"=============================" + '\n\n')
        '''

        self.my_data = obj 
        self.ProcessMyData()

        return 

    
    def ProcessMyData(self):
        '''
        Process data into a list
        '''

        x = self.my_data["data"]["timelines"]
        readings_dictionary = {}
        list_results=[]

        for i in range(len(x)):
            l2 = x[i]['intervals']
           
            for ii in range(len(l2)):
                lll = l2[ii]['values']
                readings_dictionary= {}
                readings_dictionary['rtime'] = l2[ii]['startTime']

                for reading,rvalue in lll.items():
                    readings_dictionary[reading] = rvalue

                list_results.append(readings_dictionary)

        self.my_results = list_results
    
    def PrintDataTemperaturePrecipitationProbabilityHumidity(self):
        '''
        Prints the date and the temperature data
        '''
        tab = {'': 4127, 'for': 4098, 'geek': 8637678}
        for val in range(len(self.my_results)):
            print(f"{self.ConvertClimacellTime(self.my_results[val]['rtime'])} {self.my_lat : >8} {self.my_lon : >8}  {self.my_results[val]['temperature'] : >5.2f}F  {self.my_results[val]['humidity'] :>5.2f}%  {self.my_results[val]['precipitationProbability'] : >5.2f}% ")

        print('\n\n')


    def PrintDataTemperaturePrecipitationProbabilityHumidityEpaIndex(self):
        '''
        Prints the date and the temperature data
        '''
        tab = {'': 4127, 'for': 4098, 'geek': 8637678}  
        for val in range(len(self.my_results)):
            print(f"{self.ConvertClimacellTime(self.my_results[val]['rtime']) } {self.my_lat : >8} {self.my_lon : >8}  {self.my_results[val]['temperature'] : >5.2f}F   {self.my_results[val]['humidity'] :>5.2f}%  {self.my_results[val]['precipitationProbability'] : >5.2f}%  {self.my_results[val]['epaIndex'] : >5.2f} ")
            #print('{0} {1} {2} -- {3:5.2f}F  {4:5.2f}%  {5:5.2f}%  {6:5.2f}'.format(self.ConvertClimacellTime(self.my_results[val]['rtime']), self.my_lat, self.my_lon, self.my_results[val]['temperature'], self.my_results[val]['humidity'], self.my_results[val]['precipitationProbability'], self.my_results[val]['epaIndex']))

        print('\n\n')

        
    def ConvertClimacellTime(self, my_time_to_convert):
        '''
        Convert Zulu time to Pacific Time
        input time is like: '2021-03-22T12:40:00Z'
        '''
       
        
        timeis = my_time_to_convert[0:-1]
        dt = zulu.parse('2021-03-22T03:10:00')# + 00:00') 
        dt = zulu.parse(timeis)# + 00:00') 
        local = dt.astimezone() 
        
        #print("Local timezone is", local) 
        
        pacific = dt.astimezone('US/Pacific') 
        #print("Pacific timezone is:", pacific) 
        return pacific


###########################################################################################################
'''
TESTING 
'''

def Print_Data_test(self):
        '''
        Print data to test features
        '''

        x = self.my_data["data"]["timelines"]

        readings_dictionary = {}
        list_results=[]
        print(type(x)) #list
        print(len(x))  #1

        for i in range(len(x)):
            print(type(x[i]))  #dict
            print(len(x[i]))   #4 

            print(type(x[i]['intervals']))   #list
            print(x[i]['intervals'])

            l2 = x[i]['intervals']
            print(l2)

            print(len(l2))    #15
            print('\n\n')
            for ii in range(len(l2)):
                print(type(l2[ii]))
                print(len(l2[ii]))

                print(l2[ii])
                print(l2[ii]['startTime'])
                print(type(l2[ii]['startTime']))

                print(l2[ii]['values'])
                print(type(l2[ii]['values']))
                lll = l2[ii]['values']

                print(l2[ii]['values']['temperature'])
                print(type(l2[ii]['values']['temperature']))

                readings_dictionary= {}
                readings_dictionary['rtime'] = l2[ii]['startTime']
                for reading,rvalue in lll.items():
                    #print(reading,":", rvalue)
                    readings_dictionary[reading] = rvalue
                print(readings_dictionary)
                list_results.append(readings_dictionary)
        self.my_results = list_results

        print(list_results)
        print(list_results[0]['rtime'])
        print(list_results[10]['temperature'])

