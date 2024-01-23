import random
print("welcome to rock, paper, scissor!")
choices = ["rock", "paper", "scissor"]
user_choice = input("enter your choice (rock, paper, scissor) : ")


while user_choice not in choices:
    print("invalid choice! please enter rock, paper, scissor : ")
    user_choice = input("enter your choice (rock, paper, scissor) : ").lower()
    
computer_choice = random.choice(choices)

print(f"you chose {user_choice} . computer chose {computer_choice}")

if  user_choice== computer_choice:
      print("it's a tie!")
elif(
    (user_choice=="rock" and computer_choice=="scissor") or
    (user_choice=="scissor" and computer_choice=="paper") or
    (user_choice=="paper" and computer_choice=="rock") 
    ):
      print("you win!")
else:
      print("you loss!")