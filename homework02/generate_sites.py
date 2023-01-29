#!/usr/bin/env python3

import json
import random

composition = ["stony", "iron", "stony-iron"] # creating a list of possible compositions to choose from later

sites_dict = {"sites":[]} # creating the dictionary sites_dict

counter = 1 #initializing counter which will also act as "site id" in the dictionary
while (counter <= 5): # while loop to initialize the values and keys inside the dictionary

 #randomly initializing the coordinates for lat & long with the specified range
   latitude = random.uniform(16,18)
   longitude = random.uniform(82, 84)
   comp_choice = random.choice(composition) #randomly choosing a composition from the composition list

   sites_dict["sites"].append( # append = add values and keys to the end of the dictionary
    {
     "site id" : counter,
     "latitude" : latitude,
     "longitude" : longitude,
     "composition" : comp_choice
    }
   )

   counter += 1

print(sites_dict)

#writing the sites_dict dictionary to a json file called meteorite_sites 
with open("meteorite_site.json", "w") as out:
   json.dump(sites_dict, out, indent = 2)
