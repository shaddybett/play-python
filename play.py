class students:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return(f'He is {self.name} and {self.age} years old')
    

student1 = students('Anto', 20)
student2 = students('Bett',18)
student3 = students('Alfa',19)

print(student2)

choice = input('what do you want: ')
