#!/usr/bin/env python3

def calc_turbidity(recent_data: list) -> float:
   """
   Will calculate the turbidity of the water sample based on the five most data points in the turb_data list

   Args:
   turb_data (list): list containing water sample quality data

   Returns:
   turb_sum (float): float that provides the current water turbidity

   """
   turb_sum = 0.0
   for i in range(5): # calculating the turbidity of the five most recent water samples
     cur_a0 = recent_data[i]["calibration_constant"]
     cur_I90 = recent_data[i]['detector_current']
     turb_sum = turb_sum + cur_a0 * cur_I90

   turb_sum = turb_sum / 5 # calculating average
   print("Average turbidity based on the most recent five measurements = ", turb_sum)
   return turb_sum

def safe_time(turb_standard: float, decay_factor: float, avg_turb: float) -> float:
   """
   Calculates the minimum time needed for water sample to be safe for use

   Args:
     turb_standard (float): threshold for safe water
     decay_factor (float): rate at which it decays, expressed as a decimal
     avg_turb (float) =  current turbidity calculated from function 'calc_turbidity'

   Returns:
     time_left (float) = minimum time needed for water sample to be safe for use
   """
   if avg_turb > turb_standard:

    time_left = 0

    while(avg_turb > turb_standard):
     time_left = time_left + 1
     print("Warning: Turbidity is above threshold for safe use.")
     time_safe = turb_standard*(1-decay_factor)**time_left
     print("Minimum time to return below a safe threshod = ", time_safe)
     break

   else:
     print("Info: Turbidity is below threshold for safe use")
     print("Minimum time required to return below a safe threshold = 0 hours")
   return time_safe

def main():

   import json
   import requests

   turb_standard = 1.0
   decay_factor = 0.02

   response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
   turb_data = response.json()
   recent_data = turb_data["turbidity_data"][-5:]

   avg_turb = calc_turbidity(recent_data)
   part_3 = safe_time(turb_standard, decay_factor, avg_turb)

if __name__ == '__main__':
   main()
