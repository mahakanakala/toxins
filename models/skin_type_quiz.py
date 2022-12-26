def skin_type_quiz():
  #SKIN TYPES
  skin_type = ""
  oily = 0
  dry = 0
  combination = 0
  sensitive = 0

  print("Answer the following questions to determine your skin type:")
  
  #Oily
  response = input("Do you have oily skin? (y/n) ")
  if response.lower() == "y":
    oily += 1
  elif response.lower() == "n":
    dry += 1
  
  #Dry
  response = input("Do you have dry skin? (y/n) ")
  if response.lower() == "y":
    dry += 1
  elif response.lower() == "n":
    oily += 1
  
  #Sensitive
  response = input("Do you have sensitive skin? (y/n) ")
  if response.lower() == "y":
    sensitive += 1
  elif response.lower() == "n":
    combination += 1
  
  #Combination
  response = input("Do you have combination skin? (y/n) ")
  if response.lower() == "y":
    combination += 1
  elif response.lower() == "n":
    sensitive += 1
  
  #Comparisons
  if oily > dry and oily > combination and oily > sensitive:
    skin_type = "oily"
  elif dry > oily and dry > combination and dry > sensitive:
    skin_type = "dry"
  elif combination > oily and combination > dry and combination > sensitive:
    skin_type = "combination"
  elif sensitive > oily and sensitive > dry and sensitive > combination:
    skin_type = "sensitive"
  
  #Result
  print(f"Based on your answers, it looks like you have {skin_type} skin.")

#running the program
skin_type_quiz()
