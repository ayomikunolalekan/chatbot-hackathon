from datetime import datetime
import time

print("Welcome to Three's a charm.") 
time.sleep(2)
print("We hope you have fun!")
time.sleep(2)
#user input
user_name = input("Enter your username: ")
print(f"It's a pleasure to have you here {user_name}.")


time.sleep(1)
menu = ['1. What says the time', '2. Brain teaser(quiz)', '3. Treasure  Island game', '4. Exit']

while True:
  try:
    print('\n------------MENU-------------\n')
    for item in menu:
      print(item)

      
    userMenuChoice = int(input('What would you like to do, Please make a choice from the menu: '))

# Option 1: What says the time
    if userMenuChoice == 1:
      Time = datetime.now().strftime("%H:%M")
      print("The current time is ", Time)
      input('\nPress ENTER to continue')


# Option 2: Brain teasers
    elif userMenuChoice == 2:
      time.sleep(1)
      number_of_questions = 0
      score = 0
      print("Ready for a challenge? You have 10 questions to answer!   Be careful with your spellings - the answers are very specific. Let's have some fun!")
      
      answer = input("1. Who ended slave trade in Africa: ")
      number_of_questions += 1
      if answer.lower() == "Abraham Lincoln".lower(): #or "Abraham lincoln" or "abraham lincoln":
        score += 1
        print("You got it right")
      else:
        print("Oops,You got that wrong.\nThe correct answer is Abraham Lincoln ")
        score = score
      

      answer = input("2. Who ended the killing of twins in Nigeria: ")
      number_of_questions += 1
      if answer.lower() == "Mary Slessor".lower(): #or "mary slessor" or "Mary slessor":
        score += 1
        print("You got it right!")
      else:
        print("Oops, you got that wrong.\nThe correct answer is Mary Slessor")
        score = score

      
      answer = input("3. What is the capital of Rwanda: ")
      number_of_questions += 1
      if answer.lower() == "Kigali".lower(): #or "kigali" :
        score += 1
        print("You got it right!")
      else:
        print("Oops, you got that wrong.\nThe correct answer is Kigali")
        score = score
  

      answer = input("4. After Asia, what is the next largest continent: ")
      number_of_questions += 1
      if answer.lower() == "Africa".lower(): #or "africa":
        score += 1
        print("You got it right!")
      else:
        print("Oops, you got that wrong.\nThe correct answer is Africa.")
        score = score
  

      answer = input("5. What is the longest river in the world called: ")
      number_of_questions += 1
      if answer.lower() == "The Nile".lower(): #or "the nile" or "The nile":
        score += 1
        print("You got it right!")
      else:
        print("Oops, you got that wrong.\nThe correct answer is The Nile ")
        score = score
      

      answer = input("6. How many countries are in Africa: ")
      number_of_questions += 1
      if answer == "54":
        score += 1
        print("You got it right!")
      else:
        print("Oops, you got that wrong.\nThe correct answer is 54")
        score = score 
      

      answer = input("6.How many African countries start with the letter Z: ")
      number_of_questions += 1
      if answer == "2":
        score += 1
        print("You got it right!")
      else:
        score = score
        print("Oops, you got that wrong.\n The correct answer is 2")
  

      answer = input("8. What was the first search engine in the internet: ")
      number_of_questions += 1
      if answer.lower() == "Archie".lower():
        score += 1
        print("You got it right!")
      else:
        score = score 
        print("Oops, you got that wrong.\n The correct answer is Archie")
      

      answer = input("9. How many continents are in the world: ")
      number_of_questions += 1
      if answer == "7":
        score += 1
        print("You got it right!")
      else:
        score = score
        print("Oops, you got that wrong.\n The correct   answer is 7")
      

      answer = input("10. Os computer abbreviation usually means: ")
      number_of_questions += 1
      if answer.lower() == "Operating System".lower():
        score += 1
        print("You got it right!")
      else:
        score = score
        print("Oops, you got that wrong.\nThe correct answer is Operating system")
    
      if number_of_questions == 10:
        print(f"Congratulations on completing the brain teaser. Out of the 10 questions, you got {score}/10")


    
# Option 3: Treasure Island game
    elif userMenuChoice == 3: 
      print('''     *******************************************************************************
                |                   |                  |                     |
       _________|________________.=""_;=.______________|_____________________|_______
      |                   |  ,-"_,=""     `"=.|                  |
      |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
       _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
      |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
      |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
       _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
      |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
      |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
      ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
      /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
      ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
      /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
      ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
      /______/______/______/______/______/______/______/______/______/______/
      *******************************************************************************
      ''')
      print("Welcome to Treasure Island!")
      print("Your mission is to find the hidden treasure.")
      choice1 = input('You\'re at a crossroad, where do you wanna go? Type "Right" or "Left".\n').lower()
      if choice1 == "left":
        choice2 = input('You\'ve come to a river.There is an island the middle of the river. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
        if choice2 == "wait":
          choice3 = input("You have arrived at the island safely. There is a house with three different doors. Red,blue and yellow doors. Which one would you go with?\n")
          if choice3 == "red":
            print("You entered a room full of zombies. Game Over. ")
          elif choice3 == "yellow":
            print("You entered the room with fire. Game Over")
          elif choice3 == "blue":
            print("You made it! You win!")
          else:  
            print("You made the wrong choice,Game Over ")
        else:
          print("You have entered the forbidden path. Game Over.")
      else:
        print("Oops! You fell into a ditch. Game Over. ")
      

# Option 4: Exit
    elif userMenuChoice == 4:
      print("Goodbye for now")
      exit()
      break
    
    else:
      print("Please pick an option from the menu provided")
  except ValueError:
    print("Please input the right option")
