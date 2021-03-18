#!/usr/bin/env python

import automation_functions as my_auto





def main():

    #Bear Creek Perserve
    my_lat = '37.174535'
    my_lon = '-122.014821'

    #My Home
    my_lat='37.305470'
    my_lon='-121.935920'
    my_operation = True

    my_climacell_current = my_auto.ClimacellData()
    my_climacell_current.GetNewData(get_new_data_flag=my_operation, mlat=my_lat, mlon = my_lon, mtimesteps='&timesteps=current')
    my_climacell_current.PrintDataTemperaturePrecipitationProbabilityHumidityEpaIndex()

    my_climacell_15days_1h = my_auto.ClimacellData()
    my_climacell_15days_1h.GetNewData(get_new_data_flag=my_operation, mlat='37.180211', mlon='-122.014821', mtimesteps='&timesteps=1h')
    
    my_climacell_15days_1h.PrintDataTemperaturePrecipitationProbabilityHumidityEpaIndex()

    my_climacell_15days_1d = my_auto.ClimacellData()
    my_climacell_15days_1d.GetNewData(get_new_data_flag=my_operation, mlat='37.180211', mlon='-122.014821', mtimesteps='&timesteps=1d')
    
    my_climacell_15days_1d.PrintDataTemperaturePrecipitationProbabilityHumidity()
   
   

if __name__=='__main__':
    main()

"""

"""

