
# Homework 03: The World Has Turned and Left Me Turbid

This homework is split into 2 parts: one script calling functions that determine the time
it takes for a robot to collect meteorite samples. The first file `analyze_water.py`uses 
water quality data to calculate turbidity of the sample. After calling a function defined 
above the main, the script determines whether the sample is safe to use and needs extra time
to reach the safety threshold. The second file, `test_analyze_water.py`, contains the unit tests
to verify that the first file returns the correct calculations. 

The data used in this file can be found using the link https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json . 
It is also called in the `analyze_water.py` file through the command `   response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')'
This data is stored in the format of a JSON file called `turb_data`. The most recent data points, which also happens to be the last five, 
are stored in another file called `recent_data` which is then passed to the first function. 
A sample snippet of the data looks like this: 

`{
  "turbidity_data": [
    {
      "datetime": "2023-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.022,
      "detector_current": 1.137,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 0.975,
      "detector_current": 1.141,
      "analyzed_by": "C. Milligan"
    },'


To run the code located in the github repository 332homeworks/homework03, the repo must first be 
cloned. To retreive the output, `cd` into the directory and run the command `python3 analyze_water.py`. 
The output should be 3 sentences: the first sentence returning the average turbidity of the 
first five measurements, the second identifying if the water is safe to use or not, and the last one 
calculating the time required for the water to fall below the safety threshold if it has not done so already. 
Please ensure that you have installed the python libraries: requests and json. 

Here is a snippet of what the output should return: 
`Average turbidity based on the most recent five measurements =  1.1730472  NTU \n
Warning: Turbidity is above threshold for safe use.
Minimum time to return below a safe threshod =  0.98`

