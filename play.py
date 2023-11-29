class members:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'Her name is {self.name}'
m = members(name='sofia', age=21) 
print(m)       