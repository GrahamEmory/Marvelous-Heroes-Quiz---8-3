Heroes = {
    "AAA" : "Starlord",
    "AAB" : "Drax",
    "ABA" : "Black Panther",
    "ABB" : "Doctor Strange",
    "BAA" : "Winter Soldier",
    "BAB" : "Rocket Raccoon",
    "BBA" : "Captain America",
    "BBB" : "Iron Man",
    "CAA" : "Groot",
    "CAB" : "Hulk",
    "CBA" : "Spiderman",
    "CBB" : "Mantis",
    "DAA" : "Thanos",
    "DAB" : "Thor",
    "DBA" : "Hawkeye",
    "DBB" : "Black Widow"
}

name = input("Hello, what is your name?")
answer = input("Hello "+ name +"! Would you like to play? Y or N")

if answer.upper() == " Y":
  question1 = input("What color do you prefer?(Choose A or B) \n A) Blue \n B) Red")
  question2 = input("What activity would you much rather do with your friends?(Choose A or B) \n A) Go to the Movies \n B) Go shop at the mall")
  question3 = input("What is your favorite dessert?(Choose A or B) \n A) Ice Cream \n B) Cake")
  choice = question1 + question2 +question3
  wait = input("Are you ready to know what Marvel Hero you are most like?")
  if wait.upper() == " Y":
    print("Your Marvel Hero is " + Heroes[choice.upper()])
  else:
    print("Okay, suit yourself.")
else:
  print("Oh that's too bad. Come back again later.")    