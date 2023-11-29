class members:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'Her name is {self.name} and she is {self.age} years old'
    
m = members(name='sofia', age=21) 

print(m.name)
print(m.age)
# print(m)    
choice = input('Who is she: ')

print(setattr(m,choice,'oops'))