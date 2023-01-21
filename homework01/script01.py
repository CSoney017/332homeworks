
with open('words', 'r') as f:
   words = f.read().splitlines()

words.sort(key = len, reverse = True) #capital T in true

for i in range(5):
   print(words[i])

