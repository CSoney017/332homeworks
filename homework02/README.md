# Homework 02 -- No One JSON

*The purpose of this homework assignment is to familiarize ourselves with JSON files. JSON files are very versatible data structures
that are useful when exhanging information between other programs, including those written in different languages. JSON data
is similar to the python diciontary with its key:value pairs.* 

Part 1 makes us insert randomized data into a new JSON file using the `with open('meteorite_site.json', 'w') as out:` command.
The new JSON file contains the site identification number, the latitude and longitude at which the meteorite is located, and it's composition. 
Use the command `python3 generate_sites.py` to generate random data inserted into the JSON file. Using the `cat meteorite_site.json`
command, we can see the data in the JSON file displayed similar to dictionary format. 

Part 2 has us call down a function and use the data to calculate time and distance. The robot will go from Mars to Meteorite 1, then
from Meteorite 1 to Meteorite 2, and so on until we get to Meteorite 5. Given the distance function in slack, we will call it to
calculate the distance from the first location to the second and using the distance distance, we can determine how much time was spent travling. 
Depending on the composition of the meteorite, we can also understand how long it took for the robot to sample it. All of this is listed out when 
using the `python3 calculate_trip.py` command. 

