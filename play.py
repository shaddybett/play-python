class members:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'Her name is {self.name} and she is {self.age} years old'
    
m = members(name='sofia', age=21) 
# print(m)    
# choice = input('Who is she: ')

# print(getattr(m,choice,'oops'))

choice = input('which value do you want to change: ')
value = input('what do you want it to be: ')

setattr(m,choice,value)
print(f'Her name is {members.name} and she is {members.age} years old')