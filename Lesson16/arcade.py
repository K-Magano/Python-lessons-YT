import sys
from rps import rps
from guess_number import guess_number 

def play_game(name="PlayerOne"):
    welcome_back = False
 
    while True:
       if welcome_back == True:
         print(f"\n{name}, welcome back to Arcade Menu.")
  
       playerchoice = input(
      "\nPlease choose a game:\n = Rock Paper Scissors\n2 = Guess My Number \n\n Or press \"x\" to exit the Arcade\n\n"
   )

       if playerchoice not in ["1", "2", "x"]:
        print(f"\n{name}, Please enter 1 , 2 or x")
        return play_game(name)
    
       welcome_back = True 
       
       if playerchoice == "1":
           rock_paper_scissors = rps(name)
           rock_paper_scissors()
       elif playerchoice == "2":
           guess_my_number = guess_number(name)
           guess_my_number()
       else: 
          print("\nSee you net time!")
          sys.exit(f"Bye {name}👋🏽")
    