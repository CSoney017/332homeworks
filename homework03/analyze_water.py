#this is a test comment
def calc_turbidity(turb_data: list) -> float:
 """
 Will calculate the turbidity of the water sample based on the five most data points in the turb_data list

 Args:
   turb_data (list): list containing water sample quality data

 Returns:
   turb_sum (float): float that provides the current water turbidity

 """
   turb_sum = 0.0
   for i in range(len(turb_data)):
     print(len(turb_data))
     #cur_a0 = turb_data["calibration_constant"]
     #cur_I90 = turb_data['detector_current']
     #turb_sum = turb_sum + cur_a0 * cur_I90

   turb_sum = turb_sum / 5
   return turb_sum

def safe_time(turb_standard: float, decay_factor: float, avg_turb: float): # what return ???
   if avg_turb > turb_standard:
     print("Warning: Turbidity is above threshold for safe use.")
     time_safe = math.log(turb_standard/avg_turb, 1 - decay_factor)
     print("Minimum time to return below a safe threshod = ")

   else:
     print("Info: Turbidity is below threshold for safe use")
     print("Minimum time required to return below a safe threshold = 0 hours")

def main():

   import json
   import requests

   turb_standard = 1.0
   decay_factor = 0.02

   response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
   turb_data = response.json()

   calc_turb = calc_turbidity(turb_data)

if __name__ == '__main__':
   main()
