#!/usr/bin/env python3

import json
import math

#great circle distance algorithm -- function given in slack

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( 3389.5 * d_sigma )

#stony = 1hour; iron = 2hours stony-iron = 3hours

"""
use the gcd function each time we call the json file, does the function calculate time as well?
   divide the distance by the speed of the rover to calculate the travel time
use the counter set to 1 -- while loop
use an if statement to determine what composition the meteorite is -- sample time
"""
def main():
 with open ('meteorite_site.json', 'r') as f:
   ms_data = json.load(f)

 sites_dict = ms_data["sites"]

 lat_init = 16.0 #starting latitude
 long_init = 82.0 # starting longitude
 speed = 10 # kilometers per hour -- max speed of the rover
 mars_radius = 3389.5 # kilometers

 counter = 1
 total_time = 0

 while (counter <= 5):
   print("leg:", counter)

   distance = calc_gcd(lat_init, long_init, sites_dict[counter]["latitude"], sites_dict[counter]["longitude"])
#   distance = sites_dict[counter]["latitude"]
   print(distance)
   travel_time = distance / speed
   print("travel time:", travel_time)

   if sites_dict[counter]["composition"] == "stony":
      sample_time = 1
   elif sites_dict[counter]["composition"] == "iron":
      sample_time = 2
   else:
      sample_time = 3

   print("sample time:", sample_time)

   counter += 1
   total_time = total_time + travel_time + sample_time
   print("total time traveled: ", total_time)

if __name__ == "__main__":
   main()
