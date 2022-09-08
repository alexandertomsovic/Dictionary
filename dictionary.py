# Made by Alex Tomsovic
# linktr.ee/alextomsovic
# A.R.T. Corp

from PyDictionary import PyDictionary
import sys 
from colorama import Fore


def clearpage():
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  
dictionary = PyDictionary()

user_input = str(input("Enter a word:" + Fore.LIGHTGREEN_EX + " "))

word = dictionary.meaning(user_input) # Definition dictionary

dict_length = len(word.keys()) # Total number of definition types (noun, verb, etc)
all_pairs = list(word.items()) # Makes a list with each dictionary item

print(dict_length)
if dict_length == 0:
  print("'" + Fore.RED + user_input + "' is not a valid word.")
elif dict_length == 1:
  first_pair = all_pairs[0] # First pair
  first_word_type_str = Fore.CYAN + str(first_pair[0]) + Fore.WHITE + "\n"
  
  first_joined_word_list = "\n- ".join(first_pair[1]) # Turns iist of definitons into a string 
  first_definiton_list = "- " + first_joined_word_list  # Adds a '-' to the first definiton

  clearpage()
  clearpage()
  clearpage()

  print(Fore.LIGHTGREEN_EX + user_input.capitalize() + Fore.WHITE + " | " + first_word_type_str + Fore.WHITE + "")
  print(first_definiton_list)

elif dict_length == 2:
  first_pair = all_pairs[0] # First pair
  second_pair = all_pairs[1] # Seconnd pair

  first_word_type_str = Fore.CYAN + str(first_pair[0]) + Fore.WHITE + "\n"
  second_word_type_str = Fore.CYAN + str(second_pair[0]) + Fore.WHITE + "\n"

  first_joined_word_list = "\n- ".join(first_pair[1]) # Turns iist of definitons into a string 
  first_definiton_list = "- " + first_joined_word_list  # Adds a '-' to the first definiton
  
  second_joined_word_list = "\n- ".join(second_pair[1]) # Turns iist of definitons into a string 
  second_definiton_list = "- " + second_joined_word_list  # Adds a '-' to the first definiton
  
  clearpage()
  clearpage()

  print(Fore.LIGHTGREEN_EX + user_input.capitalize() + Fore.WHITE + " | " + first_word_type_str + Fore.WHITE + "")
  print(first_definiton_list)
  
  print("\n" + Fore.LIGHTGREEN_EX +  user_input.capitalize() + Fore.WHITE + " | " + second_word_type_str + Fore.WHITE + "")
  print(second_definiton_list)

elif dict_length == 3:
  first_pair = all_pairs[0] # First pair
  second_pair = all_pairs[1] # Seconnd pair
  third_pair = all_pairs[2] # Third pair

  first_word_type_str = Fore.CYAN + str(first_pair[0]) + Fore.WHITE + "\n"
  second_word_type_str = Fore.CYAN + str(second_pair[0]) + Fore.WHITE + "\n"
  third_word_type_str = Fore.CYAN + str(second_pair[0]) + Fore.WHITE + "\n"

  first_joined_word_list = "\n- ".join(first_pair[1]) # Turns iist of definitons into a string 
  first_definiton_list = "- " + first_joined_word_list  # Adds a '-' to the first definiton
  
  second_joined_word_list = "\n- ".join(second_pair[1]) # Turns iist of definitons into a string 
  second_definiton_list = "- " + second_joined_word_list  # Adds a '-' to the first definiton

  third_joined_word_list = "\n- ".join(third_pair[1]) # Turns iist of definitons into a string 
  third_definiton_list = "- " + third_joined_word_list  # Adds a '-' to the first definiton
  
  clearpage()
  clearpage()
  clearpage()
  
  print(Fore.LIGHTGREEN_EX + user_input.capitalize() + Fore.WHITE + " | " + first_word_type_str + Fore.WHITE + "")
  print(first_definiton_list)
  
  print("\n" + Fore.LIGHTGREEN_EX +  user_input.capitalize() + Fore.WHITE + " | " + second_word_type_str + Fore.WHITE + "")
  print(second_definiton_list)

  print("\n" + Fore.LIGHTGREEN_EX +  user_input.capitalize() + Fore.WHITE + " | " + third_word_type_str + Fore.WHITE + "")
  print(third_definiton_list)
