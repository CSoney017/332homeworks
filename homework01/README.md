
Homework 01 

This homework tests us on our understanding of the Python language. 

The first exercise asks us to print out the five longest words in the 'words'
file. While we discovered a solution to this question in class, it also 
introduced us to opening and reading a file. 

Using a python function called 'sort', we filed each name by
length. However, the sort function ordered the names from least
to greatest in terms of the number of character, so we had to
reverse it to get the result we wanted. Finally, to present our
solution, we printed out a list with the five longest names. 

The second exercise does not require us to open a file, but instead wants to 
improve our understanding of modules, specifically the 'names' module. With
this question, we are to sort and print out five names that are exactly
eight characters each (nine including the space between the first and last
name).

For this problem, I initialized a counter variable to 0, and using a while
loop, set another variable 'word' to names.get_full_name, and used an if
statement to deduce if the full name was 9 characters long. If yes, I would
increase the value of the counter by 1 and print out the name. If not, I
used the 'pass' function to do nothing.  

The last question is similar to the second one in that it also uses the 'names'
module, but this time we are simply determining the length of the name. To
solve this exercise, I created a function that would take in a list from the
main program as a parameter, and using a counter variable, I made it so that
it would print out the element and it's length using the len() function.

Then, in the main, I initialized a list with 5 elements all set to the
string 'null', and then using a while loop and another counter variable, 
initialized each element to a random name given by the function: 
name.get_full_name(). I finally called the function at the very end of the 
program outside of the while loop.   

