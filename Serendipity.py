import random

number=random.randint(0,100)

print(f"The number is {number}")

print("\n"*10)

print("*****WELCOME TO THE NUMBER GUESSING GAME*****")

print("I'm thinking a number between 1 to 100")

difficulty=input("Choose a difficulty ? 'hard' or 'easy' ::  ").lower()

if difficulty=="hard":
    
    lives=5
    
    print(f"You have {lives} attempt left to guess the number.")

    start=True
    
    while start:
        
        guess=int(input("Make a guess ::"))
        
        if guess!=number:
            lives-=1
            
        if lives==0:
            start=False
            print("***You Lose***")
            break
            
        if guess==number:
            start=False
            print("***You Won***")
            break
        
        if guess<number:
            print("Too Low")
            print("Guess Again")

            
        if guess>number:
            print("Too High")
            print("Guess Again")
            
        # print(f"You have {lives} attempt left to guess the number.") 
  
        print(f"You have {lives} attempt left to guess the number.") 

            
        
    print(f"The correct number was {number}")
   

if difficulty=="easy":
    
    lives=10
    
    print(f"You have {lives} attempt left to guess the number.")

    start=True
    
    while start:
        
        guess=int(input("Make a guess ::"))
        
        if guess!=number:
            lives-=1
        
               
        if lives==0:
            start=False
            print("You Lose")
            break
        
        if guess==number:
            start=False
            print("You Won")
            break
        
        if guess<number:
            print("Too Low")
            print("Guess Again")

            
        if guess>number:
            print("Too High")
            print("Guess Again")
            
        print(f"You have {lives} attempt left to guess the number.") 
            
        
    print(f"The correct number was {number}") 
    

# This code could have written in small amount by defining the functuion.

