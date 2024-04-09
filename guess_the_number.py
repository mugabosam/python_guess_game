import random
limit=int(input("Enter a number limit\n"))
def generate_random_number():
    name=input("Enter the player_name\n")
    print (f"Hello! {name}")
    print("______________________________")
def take_user_guess():
    print(f"I think of a number from {1} to {limit}")
def check_user(random_number,user_guess):
    random_number=random.randint(1,limit)
    tries=5
    count=1
    while count<=tries:
        user_guess=int(input("Your guesses:"))
        if random_number<user_guess:
            print("Too high")
        elif random_number>user_guess:
            print("Too low")
        elif random_number==user_guess:
            wins=0
            print(f"congratulations You guessed! with {count} Trials")  
            wins=wins+1
            print(f"you won {wins} games")
            return wins
        count +=1     
    else:
        print(f"sorry, You ran out of trials,the number was:{random_number}")    
        
def main():
    generate_random_number()
    random_number=0
    user_guess=0
    again="y" or "n"    
    while again.lower()=="y":
       take_user_guess()
       check_user(random_number,user_guess)
       again=input("would you like to play again?(y/n)")
       print()
    while again.lower()=="n":
       wins = wins
    print ("Bye!")
if __name__ == "__main__":
    main()                          