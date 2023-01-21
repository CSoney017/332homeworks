import names

def printlist(list1):
   counter = 0
   while(counter < 5):
     print(list1[counter])
     print(len(list1[counter]))
     counter = counter + 1

list1 = ['null', 'null', 'null', 'null', 'null']

counter = 0
while(counter < 5):
   list1[counter] = names.get_full_name()
   counter = counter + 1

printlist(list1)
