import random 

'''generating the random number'''
def random_guess():
    return random.randint(1, 100)

def guess_number():
    random_number = random_guess()
    
    while True:
       user_input = int(input('Enter number: '))
       
       if user_input < random_number:
           print('Too low, try again')

       elif user_input > random_number:
           print('Too high, try again')
    
       else:
            print(f'correct number, {random_number}')
            break

guess_number()      
