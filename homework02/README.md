# Homework 02 -- No One JSON

*The purpose of this homework assignment is to familiarize ourselves with JSON files. JSON files are very versatible data structures
that are useful when exhanging information between other programs, including those written in different languages. JSON data
is similar to the python diciontary with its key:value pairs.* 

Part 1 makes us insert randomized data into a new JSON file using the `with open('meteorite_site.json', 'w') as out:' command.
The new JSON file has the site identification number, the latitude and longitude at which the meteorite is located, and it's composition. 
Using the `cat meteorite_site.json` command, we can see the data displayed in dictionary format. 

Part 2 has us call down a function and use the data to calculate time and distance. The robot will go from Mars to Meteorite 1, then
from Meteorite 1 to Meteorite 2, and so on until we get to Meteorite 5. Given the distance function in slack, we will use it to
calculate the distance from the first location to the second and calculate the distance and therefore time traveled. Depending on the 
composition of the meteorite, we can also calculate how long it took for the robot to sample it. All of this is listed out when 
using the `python3 calculate_trip.py` command. 

The hardest part of this homework was realizing there were functions such as random.choice() and round(). Before figuring out the
random.choice(), I was thinking of creating a list and randomly choosing a number from 0 - 2, with the number corresponding to the element
in the list. The random.choice() function saved me from writing a couple extra lines of code. The round() function for part 2 was 
difficult because I kept having to typecast variables from floats to strings vice versa to produce the result I wanted. 
