from analyze_water import calc_turbidity, safe_time
# importing the two functions created in the analyze_water file
<<<<<<< HEAD
import pytest
# importing library needed to do unit testing
=======
>>>>>>> 33b2f03e369823d9e8ec6483a2ada82cb48149be

def test_calc_turbidity(): # testing first function to verify that the result is the product of the two numbers
   assert calc_turbidity(1.0, 2.0) == 1.0 * 2.0
   assert calc_turbidity(8.5, 2.3) == 19.55

def test_safe_time(): #testing second function to verify that minimum time required is accurate
   assert safe_time(1.0) == 0 # number I came up with
   assert safe_time(1.1992) == 8.99 # number specified in the doc
