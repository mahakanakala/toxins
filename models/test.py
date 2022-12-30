def skin_type_quiz():
  #SKIN TYPES
  skin_type = ""
  oily = 0
  dry = 0
  combination = 0
  sensitive = 0
  normal = 0

  print("Answer the following questions to determine your skin type:")
  
  #Oily
  print("Do you have oily skin? (mark all that apply)")
  
  oily_options = [
    "pores seem enlarged and are visible",
    "skin looks thicker and paler",
    "prone to various forms of acne, especially in the t- zone (forehead, nose and chin)",
    "skin appears shiny or greasy",
    "looks more plump and less aged",
  ]

  oily_count = 0
  for option in oily_options:
    response = input(f"{option} (y/n) ")
    while response.lower() != "y" and response.lower() != "n":
        print("Please enter a valid response (y/n)")
        response = input(f"{option} (y/n) ")
    if response.lower() == "y":
      oily_count += 1

  if oily_count > 0:
    oily += 1
  elif oily_count == 0:
    normal += 1
  
  #Dry
  print("Do you have dry skin? (mark all that apply)")
  dry_options = [
    "skin feels tight and brittle, lacks elasticity",
    "skin texture feels rough",
    "complexion looks dull and blotchy",
    "scaling, flaking, and itchiness",
    "prone to redness, irritation and infection",
    "barely visible pores",
    "chaffing and prone to cracking",
    "enhanced fine lines and wrinkles",
  ]
  dry_count = 0
  for option in dry_options:
    response = input(f"{option} (y/n) ")
    while response.lower() != "y" and response.lower() != "n":
        print("Please enter a valid response (y/n)")
        response = input(f"{option} (y/n) ")
    if response.lower() == "y":
      dry_count += 1

  if dry_count > 0:
    dry += 1
  elif dry_count == 0:
    normal += 1
    
  
  #Sensitive
  print("Do you have sensitive skin? (mark all that apply)")
  sensitive_options = [
    "easily flushes",
    "new products irritate skin",
    "feels itchy",
    "reacts to bad weather",
    "breaking out easily",
    "barely visible pores",
  ]
  sensitive_count = 0
  for option in sensitive_options:
    response = input(f"{option} (y/n) ")
    while response.lower() != "y" and response.lower() != "n":
        print("Please enter a valid response (y/n)")
        response = input(f"{option} (y/n) ")
    if response.lower() == "y":
      sensitive_count += 1

  if sensitive_count > 0:
    sensitive += 1
  elif sensitive_count == 0:
    normal += 1
  
  #Combination
  print("Do you have dry skin? (mark all that apply)")
  
  combination_options = [
    "oily skin centered around the chin, nose, and forehead",
    "especially prone to acne on the chin, nose, and forehead",
    "mouth, eyes, and cheeks may have dry or normal skin",
    "enlarged pores around chin, nose and forehead",
  ]
  combination_count = 0
  for option in combination_options:
    response = input(f"{option} (y/n) ")
    while response.lower() != "y" and response.lower() != "n":
        print("Please enter a valid response (y/n)")
        response = input(f"{option} (y/n) ")
    if response.lower() == "y":
      dry_count += 1

  if combination_count > 0:
    sensitive += 1
  elif combination_count == 0:
    normal += 1
  
  #Comparisons
  if oily > dry and oily > combination and oily > sensitive:
    skin_type = "oily"
  elif dry > oily and dry > combination and dry > sensitive:
    skin_type = "dry"
  elif combination > oily and combination > dry and combination > sensitive:
    skin_type = "combination"
  elif sensitive > oily and sensitive > dry and sensitive > combination:
    skin_type = "sensitive"
  else:
    skin_type = "normal"
  
  #Result
  print(f"Based on your answers, it looks like you have {skin_type} skin.")

#running the program
skin_type_quiz()
