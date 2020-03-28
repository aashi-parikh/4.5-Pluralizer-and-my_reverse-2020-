def plural(word):
	''' this code produced by Aashi Parikh in lab 4.3'''
	'''Word is the string inputted by the user; this function takes the word 
    and makes it plural using the English grammar rules. It returns a string 
    that is the plural of the word.'''
	
	vowels = ['a', 'e', 'i', 'o', 'u']
	plural_word = ""
	
	if word[-1] == 's' or word[-2:] == 'ss' or word[-2:] == 'sh' or word[-2:] == 'ch' or word[-1] == 'x' or word[-1] == 'z':
		plural_word = word + 'es'
	elif word[-1] == 'y':
		if word[-2] in vowels:
			plural_word = word + 's'
		else:
			plural_word = word[0: -1] + 'ies'
	elif word[-1] == 'o':
		if word == 'photo' or word == 'piano' or word == 'halo':
			plural_word = word + 's'
		else:
			plural_word = word + 'es'
	else:
		plural_word = word + 's'
	return plural_word

def pluralizer(stringList):
    #USE plural
  '''stringList is the list of singular words inputted by the user. This 
  function takes each of the words in stringList, makes them plural, and 
  then adds them to a new list, plural_list. It returns plural_list at the
  end'''
  plural_list = []
  for item in stringList:
  	item = plural(item)
  	plural_list.append(item)
  return plural_list

fruit_list = ["apple", "cherry", "grape", "peach", "orange"]
print(pluralizer(fruit_list))



def my_reverse(string):
  '''String is the string to be reversed that is inputted by the user. This
  function takes the string and adds each character to a string in reverse order
  and then returns that string (reverse_string)'''
  reverse_string = ''
  i = -1
  while i > -((len(string)) + 1):
  	reverse_string += string[i]
  	i = i-1
  return reverse_string 

print(my_reverse('Aashi'))
  	
  
def reverser(string_list):
  '''contract'''
  reverse_list = []
  for item in string_list:
  	reverse_list.append(my_reverse(item))
  return reverse_list


fruit_list = ["apple", "cherry", "grape", "peach", "orange"]
print(reverser(fruit_list))

  
'''Use you defined functions below. 
You cannot receive full credit without doing this.'''
