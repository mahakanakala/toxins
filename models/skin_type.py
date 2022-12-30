def skin_type_quiz():
  # SKIN TYPES
  skin_type = ""
  scores = {
      "oily": 0,
      "dry": 0,
      "combination": 0,
      "sensitive": 0,
      "normal": 0
  }

  print("Answer the following questions to determine your skin type:")

  options = [
      ("Do you have oily skin? (mark all that apply)", "oily"),
      ("Do you have dry skin? (mark all that apply)", "dry"),
      ("Do you have sensitive skin? (mark all that apply)", "sensitive"),
      ("Do you have combination skin? (mark all that apply)", "combination")
  ]

  for question, skin_type in options:
      print(question)
      count = 0
      options = [
          "pores seem enlarged and are visible",
          "skin looks thicker and paler",
          "prone to various forms of acne, especially in the t- zone (forehead, nose and chin)",
          "skin appears shiny or greasy",
          "looks more plump and less aged",
          "skin feels tight and brittle, lacks elasticity",
          "skin texture feels rough",
          "complexion looks dull and blotchy",
          "scaling, flaking, and itchiness",
          "prone to redness, irritation and infection",
          "barely visible pores",
          "chaffing and prone to cracking",
          "enhanced fine lines and wrinkles",
          "easily flushes",
          "new products irritate skin",
          "feels itchy",
          "reacts to bad weather",
          "breaking out easily",
          "oily skin centered around the chin, nose, and forehead",
          "especially prone to acne on the chin, nose, and forehead",
          "mouth, eyes, and cheeks may have dry or normal skin",
          "enlarged pores around chin, nose and forehead"
      ]

      for option in options:
          response = input(f"{option} (y/n) ")
          while response.lower() != "y" and response.lower() != "n":
              print("Please enter a valid response (y/n)")
              response = input(f"{option} (y/n) ")
          if response.lower() == "y":
              count += 1

      if count > 0:
          scores[skin_type] += 1
      else:
          scores["normal"] += 1

  # Determine skin type
  skin_type = max(scores, key=scores.get)

  # Result
  print(f"Based on your answers, it looks like you have {skin_type} skin.")

# Running the program
skin_type_quiz()
