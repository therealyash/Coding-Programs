#String appending and changing

def pig_latin(text):
  say = " "
  new_list = []
  # Separate the text into words
  words = text.split()
  print(words)
  for word in words:
  	    # Create the pig latin word and add it to the list & Turn the list back into a phrase
    new_word = word[1:len(word)] + word[0]  + "ay"
    new_list.append(new_word)
    

  return say.join(new_list)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"