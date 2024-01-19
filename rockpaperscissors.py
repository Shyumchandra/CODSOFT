import random

def get_user_choice():
    user_choice = input("Select rock, paper or scissor: ").lower()
    while user_choice not in ['rock','paper','scissor']:
        print("Invalid Choice!!! Please select a Valid Option")
        user_choice=input("Select rock, paper or scissor: ").lower()
    return user_choice             

def get_computer_choice():
    return random.choice(['rock','paper','scissor'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a Tie!'
    elif(user_choice == 'rock' and computer_choice == 'scissor') or\
        (user_choice == 'paper' and computer_choice == 'rock') or\
        (user_choice == 'scissor' and computer_choice == 'paper'):
        return 'You Win!!!'
    else:
        return 'You Lose!!!'        
    
def display_result(user_choice, computer_choice, result):
    print('You chose',user_choice,' - Computer chose',computer_choice)
    print(result)

def game():
    user_score=0;
    computer_score=0;
    
    while(True):
        user_choice=get_user_choice();
        computer_choice=get_computer_choice()
        
        result=winner(user_choice,computer_choice)
        display_result(user_choice, computer_choice, result)
        
        if result == 'You Win!!!':
            user_score += 1
        elif result == 'You Lose!!!':
            computer_score += 1
        
        print('Your score: ',user_score,' Computer score: ',computer_score)
        
        play_again = input("If you want to play again(Type Yes) or (Type No) :")
        if(play_again != 'Yes'):
                print("------Thank you for Playing!!!------")
                break
            
if __name__ == "__main__":
    print("-------Welcome to Rock-Paper-Scissor Game-------")
    game()          