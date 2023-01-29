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

 counter = 0
 total_time = 0

 while (counter <= 4):
   #calculating the distance traveled and finding out how long it took to travel that distance
   # IS THIS SUPPOSED TO BE INSIDE THE WHILE LOOP??? WHY DO LAT_INIT EVERY TIME??? IS THAT TRUE DISTANCE?
   distance = calc_gcd(lat_init, long_init, sites_dict[counter]["latitude"], sites_dict[counter]["longitude"])
   travel_time = distance / speed

   #finding sample time
   if sites_dict[counter]["composition"] == "stony":
      sample_time = 1
   elif sites_dict[counter]["composition"] == "iron":
      sample_time = 2
   else:
      sample_time = 3
   # print(sites_dict[-1]["composition"]) -- ERROR WHEN CALLING ELEMENT 5
   total_time = total_time + sample_time + travel_time
   print("leg:", counter, ", time traveled:", travel_time, ", time to sample:", sample_time)
   counter += 1

 print("total time elapsed:", total_time)

if __name__ == "__main__":
   main()
