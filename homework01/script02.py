import names

counter = 0

while(counter < 5):
   word = names.get_full_name()
   if len(word) == 9:
     print(word)
     counter = counter + 1
   else:
     pass
