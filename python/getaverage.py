import os

print("Get average of list\n\nPlease separate list using ',' comma\nex: 10,15,16\n")

while True:
  
  list_string = input("List: ")

  try:
    make_list = list_string.split(",")
    float_list = [float(string) for string in make_list]
  except ValueError:
    os.system('clear')
    print("Invalid list. Please enter a list of numbers separated by commas.\n")
    continue

  sum_of_list = sum(float_list)
  list_length = len(float_list)

  average = sum_of_list / list_length
  
  os.system('clear')
  print(f"Average: {average}\n")
