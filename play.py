# class students:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
#     def __str__(self) -> str:
#         return(f'He is {self.name} and {self.age} years old')
    

# student1 = students('Anto', 20)
# student2 = students('Bett',18)
# student3 = students('Alfa',19)

# # print(student2)

# choice = input('what do you want to change: ')
# value = input('What do you want to input:')
# setattr(student2,choice,value)
# print(student2)
# print(getattr(student1,choice,'oopsie!'))

def guessing_game():
    
    guesses = 0
    winning_number = 7
    number_of_trials = 3
    while guesses != number_of_trials:
        guess = int(input('Make your guess: '))

        if guess == winning_number:

            print('You won') 
            break
        elif guess != winning_number & guesses != number_of_trials:
            print('please try again')               
        else:
            print('game over')
            break
        guesses += 1    
guessing_game()      





    

