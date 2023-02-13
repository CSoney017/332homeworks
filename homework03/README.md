
# Homework 03: The World Has Turned and Left Me Turbid

This homework is split into 2 parts: one script calling functions that determine the time
it takes for a robot to collect meteorite samples. The first file `analyze_water.py`uses 
water quality data to calculate turbidity of the sample. After calling a function defined 
above the main, the script determines whether the sample is safe to use and needs extra time
to reach the safety threshold. The second file, `test_analyze_water.py`, contains the unit tests
to verify that the first file returns the correct calculations. 

The data used in this file can be found using the link https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json . 
This data is stored in the format of a JSON file called `turb_data`. 

To run the code located in the github repository 332homeworks/homework03, the repo must first be 
cloned. To retreive the output, `cd` into the directory and run the command `python3 analyze_water.py`. 
The output should be 3 sentences: the first sentence returning the average turbidity of the 
first five measurements, the second identifying if the water is safe to use or not, and the last one 
calculating the time required for the water to fall below the safety threshold if it has not done so already. 

